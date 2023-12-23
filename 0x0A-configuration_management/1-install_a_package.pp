# Check if Python 3.8.10 or above is installed
exec { 'check-python-version':
  command => 'apt-get install -y python3.8',
  onlyif  => 'test $(python3 --version | cut -d" " -f2 | cut -d"." -f1,2) != "3.8"',
  path    => ['/bin', '/usr/bin'],
}

# Ensure Python 3 package is present
package { 'python3':
  ensure  => installed,
  require => Exec['check-python-version'],
}

# Check if Werkzeug 2.1.1 is installed
exec { 'check-werkzeug-version':
  command => 'pip3 install werkzeug==2.1.1',
  unless  => 'pip3 freeze | grep -q "Werkzeug==2.1.1"',
  path    => ['/bin', '/usr/bin'],
  require => Package['python3'],
}

# Installs Flask 2.1.0
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Exec['check-werkzeug-version'],
}
