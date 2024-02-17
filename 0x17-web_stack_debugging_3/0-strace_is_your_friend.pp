# Correct file extension to solve server error

$target_file = '/var/www/html/wp-settings.php'

exec{ 'correction':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}


file_line { 'correct_class_wp_locale_reference':
  ensure => present,
  path   => $target_file,
  match  => '^.*class-wp-locale.phpp.*$',
  line   => 'require_once(ABSPATH . WPINC . "/class-wp-locale.php");',
}
