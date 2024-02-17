# Correct file extension to solve server error

$target_file = '/var/www/html/wp-settings.php'

exec{ 'correction':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
