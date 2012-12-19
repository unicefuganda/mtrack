#
# Cookbook Name:: postgresql
# Recipe:: server
#
# Author:: Brad Montgomery (<bmontgomery@coroutine.com>)
# Author:: Joshua Timberman (<joshua@opscode.com>)
# Author:: Lamont Granquist (<lamont@opscode.com>)#
# Copyright 2009-2011, Opscode, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

include_recipe "postgresql::client"

node.default[:postgresql][:ssl] = "true"

package "postgresql"

service "postgresql" do
  service_name "postgresql"
  supports :restart => true, :status => true, :reload => true
  action :nothing
end

postgresql_conf_source = "debian.postgresql_91.conf.erb"

template "#{node[:postgresql][:dir]}/postgresql.conf" do
  source postgresql_conf_source
  owner "postgres"
  group "postgres"
  mode 0600
  notifies :restart, resources(:service => "postgresql")
end

if node[:postgresql][:standby]
  # This goes in the data directory; where data is stored
  node_name = Chef::Config[:node_name]
  master_ip = node[:postgresql][:master_ip]
  template "/var/lib/postgresql/#{node[:postgresql][:version]}/main/recovery.conf" do
    source "recovery.conf.erb"
    owner "postgres"
    group "postgres"
    mode 0600
    variables(
    :primary_conninfo => "host=#{master_ip} application_name=#{node_name}",
    :trigger_file => "/var/lib/postgresql/#{node[:postgresql][:version]}/main/trigger"
    )
    notifies :restart, resources(:service => "postgresql")
  end
end

# Copy data files from master to standby. Should only happen once.
if node[:postgresql][:master] && (not node[:postgresql][:standby_ips].empty?)
  node[:postgresql][:standby_ips].each do |address|
    bash "Copy Master data files to Standby" do
      user "root"
      cwd "/var/lib/postgresql/#{node[:postgresql][:version]}/main/"
      code <<-EOH
      invoke-rc.d postgresql stop
      rsync -av --exclude=pg_xlog * #{address}:/var/lib/postgresql/#{node[:postgresql][:version]}/main/
      touch .initial_transfer_complete
      invoke-rc.d postgresql start
      EOH
      not_if do
        File.exists?("/var/lib/postgresql/#{node[:postgresql][:version]}/main/.initial_transfer_complete")
      end
    end
  end
end
