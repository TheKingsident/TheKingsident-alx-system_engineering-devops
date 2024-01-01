# Retrieve the home directory path of the user running Puppet
$user_home = $::home

# Configures the ssh config file
file_line { 'ssh_config_myserverFromAlx':
  path  => "${user_home}/.ssh/config",
  line  => 'Host myserverFromAlx',
  match => '^Host myserverFromAlx$',
}
file_line { 'ssh_config_myserverFromAlx_hostname':
  path    => "${user_home}/.ssh/config",
  line    => '    HostName 54.236.27.95',
  match   => '^    HostName \S+',
  require => File_line['ssh_config_myserverFromAlx'],
}
file_line { 'ssh_config_myserverFromAlx_user':
  path    => "${user_home}/.ssh/config",
  line    => '    User ubuntu',
  match   => '^    User \S+',
  require => File_line['ssh_config_myserverFromAlx_hostname'],
}
file_line { 'ssh_config_myserverFromAlx_identityfile':
  path    => "${user_home}/.ssh/config",
  line    => '    IdentityFile ~/.ssh/school',
  match   => '^    IdentityFile \S+',
  require => File_line['ssh_config_myserverFromAlx_user'],
}
file_line { 'ssh_config_myserverFromAlx_passwordauth':
  path    => "${user_home}/.ssh/config",
  line    => '    PasswordAuthentication no',
  match   => '^    PasswordAuthentication',
  require => File_line['ssh_config_myserverFromAlx_identityfile'],
}
