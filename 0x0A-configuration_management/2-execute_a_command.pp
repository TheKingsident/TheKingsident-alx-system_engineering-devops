# Kills a process named killmenow
exec { 'kill-process':
  command => 'pkill -f killmenow',
  path    => ['/bin/', '/usr/bin'],
  onlyif  => 'pgrep -f killmenow',
}
