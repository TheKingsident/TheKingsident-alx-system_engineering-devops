# Add the holberton user to the sudo group
user { 'holberton':
  ensure => present,
}

group { 'sudo':
  members => ['holberton'],
}

# Update sudoers file to allow members of the sudo group to execute commands without a password
file { '/etc/sudoers':
  content => template('yourmodule/sudoers.erb'),
  mode    => '0440',
  owner   => 'root',
  group   => 'root',
  notify  => Exec['validate_sudoers'],
}

exec { 'validate_sudoers':
  command     => 'visudo -c',
  refreshonly => true,
  subscribe   => File['/etc/sudoers'],
}
