[Ravensgrib](https://www.ravensgrib.com)

A PHP based web site with user functionality.



### ravensgrib versions
(v0.0.1) Current development version.

Version specified in README, CHANGELOG, commit tag, and webroot/config.php



### Documentation

Installation of dependencies etc for debian based systems:
(This assumes a running http server with PHP 5 support).

apt-get install redis-server
apt-get install libsodium-dev
sudo apt-get install php-pear # For PECL (PHP Extension Community Library).
sudo apt-get install php5-dev # Required by libsodium-php
pecl install libsodium
You should add "extension=libsodium.so" to apache2/php.ini under "Dynamic Extensions" header. You may want to add it to /etc/php5/cli too.

/etc/php5/cli/php.ini is for the CLI PHP program, which you found by running php on the terminal.

/etc/php5/cgi/php.ini is for the php-cgi system which isn't specifically used in this setup.

/etc/php5/apache2/php.ini is for the PHP plugin used by Apache. This is the one you need to edit for changes to be applied for your Apache setup.
sudo /etc/init.d/apache2 restart


Clone the repository to your htdocs and view the webroot/index.php with browser.

Enhancements, pollyfills and addons are in the assets folder under either css or js.



### Requirements
HTTP server with PHP. Apache recommended
Redis database	# For user info and data storage
libsodium # For password hashing and salting for security
libsodium-php # A binding for PHP to use the C-library of libsodium.



### Current Features:
General functinality:
Specs and options:



### Bugs, known Issues and missing Features:

Please report an issue if one is found.

Functionality:
Specs and options:
Security:
	User login. Delay for login attempt needs to always be the same regardless of weather username exsists in db or not.
Code, style and performance:



### Licence

GNU General Public License v3.0 only

LICENCE for details.

http://spdx.org/licenses/

Copyright (c) 2016 A.K. Weeks



### Sources, inspiration and notes

Recommends: [Free DNS](https://freedns.afraid.org/)

#### Websites


#### Manuals
