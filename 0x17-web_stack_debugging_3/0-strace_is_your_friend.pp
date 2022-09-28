# Fix Apache2 Error by a bad importation

exec {'fix typo phpp in configuration file':
  command  => 'sed -i "s/phpp/php/" /var/www/html/wp-settings.php',
  user     => 'root',
  provider => 'shell',
  path     => '/usr/local/bin/:/bin:/usr/sbin'
}
