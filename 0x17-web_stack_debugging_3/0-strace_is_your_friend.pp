# Correct file extension to solve server error

$target_file = '/var/www/html/wp-settings.php'

file_line { 'correct_class_wp_locale_reference':
  ensure => present,
  path   => $target_file,
  match  => '^.*class-wp-locale.phpp.*$',
  line   => 'require_once(ABSPATH . WPINC . "/class-wp-locale.php");',
}
