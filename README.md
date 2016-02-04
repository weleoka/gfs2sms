The World Meteorological Organization (WMO) Commission for Basic Systems (CBS) met in 1985 to create the GRIB (GRIdded Binary) format. The WGDM in February 1994, after major changes, approved revision 1 of the GRIB format. GRIB Edition 2 format was approved in 2003 at Geneva.



### gfs2sms versions
(v0.0.1) Current development version.

Version specified in README, CHANGELOG, commit tag and gfs2sms_config.py



### Requirements
Python v2.7
GRIB API v1.14



### Overview
gfs2sms has two parts. 

Firstly gfs2sms is a web server and gateway between free grib providers and users of the gfs2sms service. The gfs2sms server will gather user requested data out of GFS GRIB files and fit it into the gfs2sms protocol for forwarding to clients. 

Secondly gfs2sms is a client which can decode the gfs2sms protocol. The client is optimised for running on any device and can accept the encoded data to be cut-and-paste:ed or be forwarded from other software automatically. The client can then decode the data and display in human readable format, either text based or graphically such as in a digital image.

Clients who stand to benefit from these services are those which are in ultra-low, ultra-restricted bandwidth situations. Fore example where the GSM 160 character SMS is the sole channel of communication. The gfs2sms protocol is an overlay for the GSM SMS standard to allow data transfer following extremely strict, pre-defined, formatting.



### Installation
1. Git clone or download archive and extract.
2. Make gfs2sms.py executable
3. Run as shell script "./gfs2sms.py" in a terminal.



### Usage



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

Have a look at the known issues and missing features and take a pick or find something else that needs doing.

The best way to get your changes merged is as follows:

1. Clone your fork
2. Hack away
3. If you are adding significant new functionality, document it in the README
4. Do not change the version number, I will do that on my end
5. Push the repo up to GitHub
6. Send a pull request to [weleoka/gfs2sms](https://github.com/weleoka/gfs2sms)



### Licence

GNU GENERAL PUBLIC LICENSE

LICENCE for details.

Copyright (c) 2016 A.K. Weeks



### Sources, inspiration and notes



#### Websites
http://forecast2phone.com/
http://www.libpng.org/pub/png/



#### Manuals
http://www.wmo.int/pages/prog/www/WDM/Guides/Guide-binary-2.html
http://weather.unisys.com/wxp/Appendices/Formats/GRIB.html
http://www.nws.noaa.gov/mdl/degrib/txtview.php?file=degrib.txt&dir=base