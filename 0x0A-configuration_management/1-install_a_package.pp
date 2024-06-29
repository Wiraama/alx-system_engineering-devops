#!/usr/bin/pup
# installing flast from pip3

package {'python3-pip':
  ensure => 'installed',
}

package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}
