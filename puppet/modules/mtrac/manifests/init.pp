class mtrac {
  package { "python-pip":
    ensure => present,
  }

  package { "python-dev":
    ensure => present,
  }


  package { "python-lxml":
    ensure => present,
  }
}
