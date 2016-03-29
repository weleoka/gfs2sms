The World Meteorological Organization (WMO) Commission for Basic Systems (CBS) met in 1985 to create the GRIB (GRIdded Binary) format. The WGDM in February 1994, after major changes, approved revision 1 of the GRIB format. GRIB Edition 2 format was approved in 2003 at Geneva.



### gfs2sms versions
(v0.0.1) Current development version.

Version specified in README, CHANGELOG, commit tag, gfs2sms_config.py and webroot/config.php



### Requirements
Python v2.7
GRIB API v1.14



### Overview
gfs2sms has two parts. 

Firstly gfs2sms is server and gateway between free grib providers and users of the gfs2sms service. The gfs2sms server will gather user requested data out of GFS GRIB files and fit it into the gfs2sms protocol for forwarding to clients. 

Secondly gfs2sms is a client which can decode the gfs2sms protocol. The client is optimised for running on any device and can accept the encoded data to be cut-and-paste:ed or be forwarded from other software automatically. The client can then decode the data and display in human readable format, either text based or graphically such as in a digital image.

Clients who stand to benefit from these services are those which are in ultra-low, ultra-restricted bandwidth situations. Fore example where the GSM 160 character SMS is the sole channel of communication. The gfs2sms protocol is an overlay for the GSM SMS standard to allow data transfer following extremely strict, pre-defined, formatting.

There is a web server for handling user accounts and access to the gfs2sms server.


### Installation
1. Git clone or download archive and extract.
2. Make gfs2sms.py executable
3. Run as shell script "./gfs2sms.py" in a terminal.


### Usage documentation

When invoking applications using PHP's exec() it may be useful to include "2>&1" (stderr to stdout) at the end of your command so fault codes/text will be passed back to the invoking application instead of dissapearing.

Web server setup:
Because of the processing of data is done by external programs which are called by apache, the apache user permissions need to be changed.

One solution is using sudo
(the example program here is to run wgrib from PHP):
~~~~~~~~~~~~~~~~~~~~~~~~~~~~ .bash
exec('sudo -u myuser wgrib');
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You will obviously need to setup sudo to allow the user running your webserver to invoke it (apache usually has the user www-data). Edit the sudoers file with visudo. You can use something like to prevent Apache from being able to run other commands and only the wgrib command. [More about visudo](https://www.garron.me/en/linux/visudo-command-sudoers-file-sudo-default-editor.html):

~~~~~~~~~~~~~~~~~~~~~~~~~~~~ {.bash #example-1}
www-data ALL=(www-data) NOPASSWD: /etc/wgrib, /etc/wgrib2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Another solution, not recommended. This will work but hrm,hrm. security-wise it's a big bad no no. Do it anyway? O.K. change /etc/apache2/envvars:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~ {.bash #example-2}
#export APACHE_RUN_USER=www-data #comment this line out.
export APACHE_RUN_USER=admin # add this line, change "admin" to relevant user.
#export APACHE_RUN_GROUP=www-data # do the same for the group, comment this out.
export APACHE_RUN_GROUP=admin # add this line, change "admin" to relevant user.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~





### Developer info
The execution when gfs2sms.py is run is to call readParameters() which parses commandline parameters, if present. After that it calls startpoint().

About logging:
The logger module is called directly from gfs2sms modules and classes but also from __main__. 

The logging module is handled by the function gfs2sms.logging_tools.initialiseLogging()


~~~~~~~~~~~~~~~~~~~~~~~~~~~~ {.python #logging}
logging.debug('All systems operational')
logging.info('Airspeed 300 knots')
logging.warn('Low on fuel')
logging.error('No fuel. Trying to glide.')
logging.critical('Glide attempt failed. About to crash.')
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
More on the [above example](https://pingbacks.wordpress.com/2010/12/21/python-logging-tutorial/)



### Current Features:
General functinality:
Specs and options:



### Bugs, known Issues and missing Features:

Please report an issue if one is found.

Functionality:
Specs and options:
Security:
Code, style and performance:



### Contributing

If you'd like to contribute to gfs2sms's development, start by forking the GitHub repo:

https://github.com/weleoka/gfs2sms.git

Have a look at the known issues and missing features and take a pick or find something else that needs doing. Check out developer info in README.md too.

The best way to get your changes merged is as follows:

1. Clone your fork
2. Hack away
3. If you are adding significant new functionality, document it in the README
4. Do not change the version number, I will do that on my end
5. Push the repo up to GitHub
6. Send a pull request to [weleoka/gfs2sms](https://github.com/weleoka/gfs2sms)



### Licence

GNU General Public License v3.0 only

LICENCE for details.

http://spdx.org/licenses/

Copyright (c) 2016 A.K. Weeks



### Sources, inspiration and notes



#### Websites
http://forecast2phone.com/
http://www.libpng.org/pub/png/



#### Manuals
http://www.wmo.int/pages/prog/www/WDM/Guides/Guide-binary-2.html
http://weather.unisys.com/wxp/Appendices/Formats/GRIB.html
http://www.nws.noaa.gov/mdl/degrib/txtview.php?file=degrib.txt&dir=base