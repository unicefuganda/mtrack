class mtrac {

  exec { "update":
    command => "apt-get update",
    path => "/usr/bin/"
  }

  package { "python-pip":
    ensure => present,
  }

  package { "python-dev":
    ensure => present,
  }

  package { "libxml2-dev":
    require => Command['update'],
    ensure => present,
  }

  package { "libxslt-dev":
    require => Command['update'],
    ensure => present,
  }

  package { "python-lxml":
    require => Package['libxslt-dev', 'libxml2-dev'],
    ensure => present,
  }
}
