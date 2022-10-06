# Fix files user limit

exec { 'Cuantity of files that can open the user holberton':
  comamnd  => 'sed -ir \'s/nofile [0-9]+$/nofile 5000/' limits.conf',
  user     => 'root',
  provider => 'shell',
  path     => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
