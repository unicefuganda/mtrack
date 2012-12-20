class mtrac {
  package { "python-pip":
    ensure => present,
  }

  package { "python-dev":
    ensure => present,
  }

  # exec { "pip-modules":
  #   require => [Class["postgres"], Package["python-pip"], Package["python-dev"]],
  #   command => "/usr/bin/pip install -r /vagrant/pip-requires.txt",
  #   timeout => 0,
  # }
  
  # exec { "restoredb":
  #     require => [Class["postgres"], Exec["pip-modules"]],
  #     command => "/usr/bin/sudo -u postgres -c \"/usr/bin/pg_restore -d $dbname /vagrant/$dumpfile\"",
  #     timeout => 0,
  #     returns => [0, 1],
  #   }
  # 
  #   exec { "runserver":
  #     require => Exec["restoredb"],
  #     command => "/vagrant/mtrack_project/manage.py runserver &",
  #   }
}