# Configures the ssh config file
file_line { 'ssh_config_myserverFromAlx':
  path  => '/home/cakemurderer/.ssh/config',
  line  => 'Host myserverFromAlx',
  match => '^Host myserverFromAlx$',
}
file_line { 'ssh_config_myserverFromAlx_hostname':
  path    => '/home/cakemurderer/.ssh/config',
  line    => '    HostName 54.236.27.95',
  match   => '^    HostName \S+',
  require => File_line['ssh_config_myserverFromAlx'],
}
file_line { 'ssh_config_myserverFromAlx_user':
  path    => '/home/cakemurderer/.ssh/config',
  line    => '    User ubuntu',
  match   => '^    User \S+',
  require => File_line['ssh_config_myserverFromAlx_hostname'],
}
file_line { 'ssh_config_myserverFromAlx_identityfile':
  path    => '/home/cakemurderer/.ssh/config',
  line    => '    IdentityFile ~/.ssh/school',
  match   => '^    IdentityFile \S+',
  require => File_line['ssh_config_myserverFromAlx_user'],
}
file_line { 'ssh_config_myserverFromAlx_passwordauth':
  path    => '/home/cakemurderer/.ssh/config',
  line    => '    PasswordAuthentication no',
  match   => '^    PasswordAuthentication',
  require => File_line['ssh_config_myserverFromAlx_identityfile'],
}
