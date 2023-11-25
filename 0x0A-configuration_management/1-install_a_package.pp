# install a package using puppet

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip'
}

package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip'
}
