# Add the holberton user to the sudo group
user { 'holberton':
  ensure => present,
}

group { 'sudo':
  ensure  => present,
  members => ['holberton'],
}

# Allow members of the sudo group to execute commands without a password
file { '/etc/sudoers':
  ensure       => file,
  content      => "# This file is managed by Puppet. DO NOT EDIT.\n\n%sudo ALL=(ALL:ALL) NOPASSWD: ALL\n",
  mode         => '0440',
  owner        => 'root',
  group        => 'root',
  validate_cmd => 'visudo -cf %',
}
