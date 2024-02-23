# Lets holberton user log in and open files

exec { 'increases-hard-limit':
  command => "sed -i '/^holberton hard/s/4/50000/' /etc/security/limits.conf",
  path    => ['/usr/local/bin/', '/bin/'],
  onlyif  => "grep '^holberton hard' /etc/security/limits.conf | grep -q '4'",
}

exec { 'increases-soft-limit':
  command => "sed -i '/^holberton soft/s/5/50000/' /etc/security/limits.conf",
  path    => ['/usr/local/bin/', '/bin/'],
  onlyif  => "grep '^holberton soft' /etc/security/limits.conf | grep -q '5'",
}
