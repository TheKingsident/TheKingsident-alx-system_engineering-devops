# Manifest that installs NGINX and configures it accordingly
# Ensure NGINX is installed
package { 'nginx':
  ensure => installed,
}

# Create a custom 404 page HTML file
file { '/var/www/html/custom_404.html':
  ensure  => file,
  content => "Ceci n'est pas une page\n",
  require => Package['nginx'], # Ensures NGINX is installed before creating the file
}

# Configure NGINX for custom page, redirect, and custom 404 error page
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => "
server {
    listen 80;

    # Custom 404 page
    error_page 404 /custom_404.html;
    
    location = /custom_404.html {
        root /var/www/html;
        internal;
    }

    location / {
        try_files \$uri \$uri/ =404;
        add_header X-Served-By ${hostname};
    }

    location /static/ {
        root /var/www/html;
    }

    location /redirect_me {
        return 301 http://google.com;
    }

    # Return Hello World for the root URL
    location = / {
        return 200 'Hello World!\\n';
        add_header X-Served-By ${hostname};
    }
}
",
  require => Package['nginx'], # Ensures NGINX is installed before modifying the config
  notify  => Service['nginx'], # Notifies NGINX service to reload if the file changes
}

# Ensure NGINX service is running and enabled
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'], # Reloads NGINX if the config file changes
}
