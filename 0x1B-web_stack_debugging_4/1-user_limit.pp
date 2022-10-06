# Fix files user limit

exec { 'Fix limit':
  command  => 'sed -ri \'s/nofile [0-9]+$/nofile 5000/\' /etc/security/limits.conf',
  user     => 'root',
  provider => 'shell',
  path     => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
