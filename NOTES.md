To do:

add assertions to class constructor.
assert (Temperature >= 0),"Colder than absolute zero!"
If the expression is false, Python raises an AssertionError exception.
If the assertion fails, Python uses ArgumentExpression as the argument for the AssertionError. AssertionError exceptions can be caught and handled like any other exception using the try-except statement,
Assertions will be optimised out by interpreter if so desired.

if x is a value set via a user interface or from an external source, an exception is best.
If x is only set by your own code in the same program, go with an assertion.

* Implement the redis database for user accounts.
- Link from php for user creation.
- Link from gfs2sms to handle email API requests.

* Implement statistics module for tracking requests and bandwidth usage.

* Enable oAuth2 for imaplib connection. See email.py for info.
- See module email.py what to do for googles API.

* Extract data points u & v values from saildocs grib.
- using wgrib

* Look at explorerSE API for auto-messaging with SMS.

===
Questions:
How to change dictionary = {'a': 'free', 'b': 'me', 'c': 'now'} into 
function(a=free, b=me, c=now)

str = ""
for key in dictionary.keys:
    str += "$key = $dictionary['key'], "
print (str)



### NOTES and stuff:

#### SMS GSM and Android notes
Generally an SMS is restricted to 160 (7 bit) characters or 140 (8 bit) characters.
Unicode SMS support (70 characters in length).

http://codetheory.in/android-sms/
https://mobiforge.com/design-development/sms-messaging-android

SMS Gateways and APIs:
https://sites.google.com/a/tellustalk.com/english/api
http://www.bulksms.com/products/sms-api.htm
http://www.smsglobal.com/rest-api/
https://smsgateway.me/  // Turn your android into an SMS gateway API.
https://www.cellsynt.com/sv/sms/priser    // SE
inleed.se/sms-api/   // SE


#### General web API notes
Use runscope to test the routing API output of email provider.
https://www.runscope.com/


#### Email SMTP IMAP
OAuth, Google API, GMail and Google App Engine:
https://github.com/charlierguo/gmail
https://developers.google.com/identity/protocols/OAuth2


#### GRIB and GRIB software notes
X is known as shortName = 10u (the 10 makes for base ten is a guess)
Y is known as shortName = 10v
https://software.ecmwf.int/wiki/display/GRIB/What+is+GRIB-API
https://github.com/erget/PythonicGRIB
WGRIB commands:
./wgrib -s sample.grb | grep ":12hr fcst:" | ./wgrib -i -text sample.grb -o outfile
./wgrib -s -d 1 sample.grb | ./wgrib -i -text sample.grb -o outfile1
wgrib -s tg03.grb | grep "24hr fcst" | wgrib -i -grib tg03.grb -o aaa.grb



#### GRIB_API by notes
I had to move the default installed files .py from 
/usr/local/lib/python2.7/site-packages/grib_api
to
/usr/local/lib/python2.7/dist-packages/
to load the module properly.

http://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_1p00.pl?file=gfs.t12z.pgrb2.1p00.f012&lev_10_m_above_ground=on&var_UGRD=on&var_VGRD=on&leftlon=0&rightlon=360&toplat=90&bottomlat=-90&dir=%2Fgfs.2016013112

http://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_1p00.pl?file=gfs.t00z.pgrb2.1p00.f000&lev_10_m_above_ground=on&var_UGRD=on&var_VGRD=on
&dir=%2Fgfs.${YYYYMMDD}00" -o gfs.t00z.pgrb2.1p00.f000

Description   Filename  Cycles Available
2.5 Degree  gfs.tCCz.pgrbfFFF.2p5deg.grib2  00,06,12,18 UTC
1.0 Degree  gfs.tCCz.pgrbfFFF.grib2   00,06,12,18 UTC
0.5 Degree  gfs.tCCz.mastergrb2fFFF.grib2 (combination of pgrb2f and pgrb2bf)   00,06,12,18 UTC








#### Python notes
math.atan2(y, x)
    Return atan(y / x), in radians. The result is between -pi and pi. The vector in the plane from the origin to point (x, y) makes this angle with the positive X axis. The point of atan2() is that the signs of both inputs are known to it, so it can compute the correct quadrant for the angle. For example, atan(1) and atan2(1, 1) are both pi/4, but atan2(-1, -1) is -3*pi/4. Usee math.degree to convert it from radians to degrees.

  * Need CGI best practices and security know how.

To run for example wgrib from python.
https://docs.python.org/2/library/subprocess.html
https://jimmyg.org/blog/2009/working-with-python-subprocess.html



Logger.debug(msg, *args, **kwargs)

    Logs a message with level DEBUG on this logger. The msg is the message format string, and the args are the arguments which are merged into msg using the string formatting operator. (Note that this means that you can use keywords in the format string, together with a single dictionary argument.)

    There are two keyword arguments in kwargs which are inspected: exc_info which, if it does not evaluate as false, causes exception information to be added to the logging message. If an exception tuple (in the format returned by sys.exc_info()) is provided, it is used; otherwise, sys.exc_info() is called to get the exception information.

    The second keyword argument is extra which can be used to pass a dictionary which is used to populate the __dict__ of the LogRecord created for the logging event with user-defined attributes. These custom attributes can then be used as you like. For example, they could be incorporated into logged messages. For example:

    FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
    logging.basicConfig(format=FORMAT)
    d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
    logger = logging.getLogger('tcpserver')
    logger.warning('Protocol problem: %s', 'connection reset', extra=d)

    would print something like

    2006-02-08 22:20:02,165 192.168.0.1 fbloggs  Protocol problem: connection reset

    The keys in the dictionary passed in extra should not clash with the keys used by the logging system. (See the Formatter documentation for more information on which keys are used by the logging system.)

    If you choose to use these attributes in logged messages, you need to exercise some care. In the above example, for instance, the Formatter has been set up with a format string which expects ‘clientip’ and ‘user’ in the attribute dictionary of the LogRecord. If these are missing, the message will not be logged because a string formatting exception will occur. So in this case, you always need to pass the extra dictionary with these keys.

    While this might be annoying, this feature is intended for use in specialized circumstances, such as multi-threaded servers where the same code executes in many contexts, and interesting conditions which arise are dependent on this context (such as remote client IP address and authenticated user name, in the above example). In such circumstances, it is likely that specialized Formatters would be used with particular Handlers.

Logger.info(msg, *args, **kwargs)
    Logs a message with level INFO on this logger. The arguments are interpreted as for debug().

Logger.warning(msg, *args, **kwargs)
    Logs a message with level WARNING on this logger. The arguments are interpreted as for debug().

Logger.error(msg, *args, **kwargs)
    Logs a message with level ERROR on this logger. The arguments are interpreted as for debug().

Logger.critical(msg, *args, **kwargs)
    Logs a message with level CRITICAL on this logger. The arguments are interpreted as for debug().

Logger.log(lvl, msg, *args, **kwargs)
    Logs a message with integer level lvl on this logger. The other arguments are interpreted as for debug().

Logger.exception(msg, *args, **kwargs)
    Logs a message with level ERROR on this logger. The arguments are interpreted as for debug(), except that any passed exc_info is not inspected. Exception info is always added to the logging message. This method should only be called from an exception handler.






#### Free GRIB providers http://www.euronav.co.uk/Weather/gribfiles.htm
GMN GRIB CoverageGlobal Marine Networks (GMN), the leader in marine weather services, now offers 7 day wind forecasts of the world as a free public service via its GRIB Mail Robot. These forecasts are generated daily at 0015, 0615, 1215, 1815 GMT. Select areas or a custom LAT/LONG area possible to request with email.
http://www.globalmarinenet.com/free-grib-files-provided-by-global-marine-networks/
Norwegian Weather Service GRIBS: om.yr.no/verdata/grib/
Mediterranean high-res GRIBs: http://openskiron.org/en


// http://www.globalmarinenet.com/free-grib-file-downloads/#download
```JAVASCRIPT
function build_url(region,data,dataset)
{
   if (typeof(dataset)==='undefined') dataset = 'nww3';
   var url;
   url = "http://gribs2.gmn-usa.com/cgi-bin/weather_fetch.pl?parameter=";
   url = url.concat(data,"&#038;days=7");
   url = url.replace("#038;","");
   url = url.concat("&#038;region=",region);
   url = url.replace("#038;","");
   url = url.concat("&#038;dataset=",dataset);
   url = url.replace("#038;","");
//alert(url); 
   window.location.href = url;
}

´´´


#### MISCELLANEOUS notes
What is the difference between a vector and a scalar?

• Vectors have both, a magnitude and direction, but scalars have magnitude only.

• Vector equality occurs only when both the magnitude and the direction of two vectors of the same type are the same, but in the case of scalars, equality of magnitude is sufficient.

• Scalars of the same type can be added just as real numbers, but the addition of vectors should be done using the polygon law.


--- Keys for GFS grib


wgrib -V (verbose):
rec 1:0:date 2016012106 UGRD kpds5=33 kpds6=105 kpds7=10 levels=(0,10) grid=255 10 m above gnd anl:
  UGRD=u wind [m/s]
  timerange 10 P1 0 P2 0 TimeU 1  nx 6 ny 6 GDS grid 0 num_in_ave 0 missing 0
  center 7 subcenter 0 process 81 Table 2 scan: WE:NS winds(N/S) 
  latlon: lat  60.000000 to 50.000000 by -2.000000  nxny 36
          long 10.000000 to 20.000000 by 2.000000, (6 x 6) scan 0 mode 128 bdsgrid 1
  min/max data -3.5 4.94  num bits 13  BDS_Ref -3272  DecScale 2 BinScale 0
rec 6:715:date 2016012106 VGRD kpds5=34 kpds6=105 kpds7=10 levels=(0,10) grid=255 10 m above gnd anl:
  VGRD=v wind [m/s]
  timerange 10 P1 0 P2 0 TimeU 1  nx 6 ny 6 GDS grid 0 num_in_ave 0 missing 0
  center 7 subcenter 0 process 81 Table 2 scan: WE:NS winds(N/S) 
  latlon: lat  60.000000 to 50.000000 by -2.000000  nxny 36
          long 10.000000 to 20.000000 by 2.000000, (6 x 6) scan 0 mode 128 bdsgrid 1
  min/max data -7.96 1.02  num bits 13  BDS_Ref -2353  DecScale 2 BinScale 0
rec 7:858:date 2016012106 VGRD kpds5=34 kpds6=105 kpds7=10 levels=(0,10) grid=255 10 m above gnd 24hr fcst:
  VGRD=v wind [m/s]
  timerange 10 P1 0 P2 24 TimeU 1  nx 6 ny 6 GDS grid 0 num_in_ave 0 missing 0
  center 7 subcenter 0 process 96 Table 2 scan: WE:NS winds(N/S) 
  latlon: lat  60.000000 to 50.000000 by -2.000000  nxny 36
          long 10.000000 to 20.000000 by 2.000000, (6 x 6) scan 0 mode 128 bdsgrid 1
  min/max data -5.77 6.9  num bits 13  BDS_Ref -2707  DecScale 2 BinScale 0




keys_iterator.py
edition = 1
centre = kwbc
typeOfLevel = heightAboveGround
level = 10
dataDate = 20160121
stepRange = 24
shortName = 10v
packingType = grid_simple
gridType = regular_ll



wgrib
1:0:d=16012106:UGRD:kpds5=33:kpds6=105:kpds7=10:TR=10:P1=0:P2=0:TimeU=1:10 m above:anl:NAve=0
2:143:d=16012106:UGRD:kpds5=33:kpds6=105:kpds7=10:TR=10:P1=0:P2=24:TimeU=1:10 m above gnd:24hr fcst:NAve=0
3:286:d=16012106:UGRD:kpds5=33:kpds6=105:kpds7=10:TR=10:P1=0:P2=48:TimeU=1:10 m above gnd:48hr fcst:NAve=0
4:429:d=16012106:UGRD:kpds5=33:kpds6=105:kpds7=10:TR=10:P1=0:P2=72:TimeU=1:10 m above gnd:72hr fcst:NAve=0
5:572:d=16012106:UGRD:kpds5=33:kpds6=105:kpds7=10:TR=10:P1=0:P2=96:TimeU=1:10 m above gnd:96hr fcst:NAve=0
6:715:d=16012106:VGRD:kpds5=34:kpds6=105:kpds7=10:TR=10:P1=0:P2=0:TimeU=1:10 m above gnd:anl:NAve=0
7:858:d=16012106:VGRD:kpds5=34:kpds6=105:kpds7=10:TR=10:P1=0:P2=24:TimeU=1:10 m above gnd:24hr fcst:NAve=0
8:1001:d=16012106:VGRD:kpds5=34:kpds6=105:kpds7=10:TR=10:P1=0:P2=48:TimeU=1:10 m above gnd:48hr fcst:NAve=0
9:1144:d=16012106:VGRD:kpds5=34:kpds6=105:kpds7=10:TR=10:P1=0:P2=72:TimeU=1:10 m above gnd:72hr fcst:NAve=0
10:1287:d=16012106:VGRD:kpds5=34:kpds6=105:kpds7=10:TR=10:P1=0:P2=96:TimeU=1:10 m above gnd:96hr fcst:NAve=0