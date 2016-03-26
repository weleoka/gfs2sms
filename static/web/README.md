# [Ravensgrib](https://www.ravensgrib.com)

A PHP based web site.


## Quickstart

Requires a HTTP server with PHP. Apache recommended
Redis database	# For user info and data storage
libsodium # For password hashing and salting for security
libsodium-php # A binding for PHP to use the C-library of libsodium.


For debian based systems:
apt-get install redis-server
apt-get install libsodium-dev
sudo apt-get install php-pear # For PECL.
sudo apt-get install php5-dev # Required by libsodium-php
pecl install libsodium
You should add "extension=libsodium.so" to apache2/php.ini under "Dynamic Extensions" header. You may want to add it to /etc/php5/cli too.

/etc/php5/cli/php.ini is for the CLI PHP program, which you found by running php on the terminal.

/etc/php5/cgi/php.ini is for the php-cgi system which isn't specifically used in this setup.

/etc/php5/apache2/php.ini is for the PHP plugin used by Apache. This is the one you need to edit for changes to be applied for your Apache setup.
sudo /etc/init.d/apache2 restart



Clone the repository to your htdocs and view the webroot/index.php with browser.


Enhancements, pollyfills and addons are in the assets folder under either css or js.


## Documentation

Currently the site is for development purposes. The CSS uses a pre-compiler; LESS, and currently that is done with a client-side javascript-based compiler. Obviously a production site has minimised CSS, and probably files combined for minimum HTTP requests.


There is also simple script using jQuery to lazy-load pictures only on WVP (Wide View Port) devices.


### Licence etc.

Copyright (c) 2015 Kai Weeks.



Recommends: [Free DNS](https://freedns.afraid.org/)