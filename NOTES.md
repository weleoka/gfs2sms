To do:

* PHP & Apache & Web server
- visudo permissions and custom user for apache.
- Let's Encrypt signed SSL certificate.
(https://www.digitalocean.com/community/tutorials/how-to-create-a-ssl-certificate-on-apache-for-ubuntu-14-04)
(https://www.digitalocean.com/community/tutorials/how-to-secure-apache-with-let-s-encrypt-on-ubuntu-14-04)
- User password hash and salt.
(https://crackstation.net/hashing-security.htm)


* Database Redis (https://www.quora.com/Why-use-Redis)
- data persistance levels AOF + RDB. redis.conf
- cron job for hourly and daily snapshots of the RDB file.
(Different folders on server, and transfer your snapshots using SCP (part of SSH) to far servers (VPS's).
- SSL pipe from clients to server. 
(ngrok creates a secure public URL (https://yourapp.ngrok.io) to your local webserver on your machine.)
Use spiped or another SSL tunnelling software in order to encrypt traffic between Redis servers and Redis clients if your environment requires encryption.
- Configure redis init script for autostart
http://redis.io/topics/quickstart


* Email IMAP Python
- Get some Continous Integration and tests.
- Send email.
- Recieve email with attatchment.
- Enable OAuth2 (read in module email.py).


* Redis database user accounts.
- Web form for user creation.
- Database
  - ID
  - Name
  - Email
  - Email2
  - Password
  - Date joined
  - Profile


* Redis data and file tracking.
  - ID
  - User
  - Position
  - Time
  - Answered

(* Implement statistics module for tracking requests and bandwidth usage.)


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

#### APACHE2
DocumentRoot and apache user in:
sudo nano /etc/apache2/sites-available/000-default.conf
sudo nano /etc/apache2/apache2.conf
sudo nano /etc/apache2/envvars
sudo /etc/init.d/apache2 restart

<VirtualHost xxx.xxx.xxx.xxx>
ServerAdmin abceedy@xxx.xxx.xxx.xxx
DocumentRoot  /usr/local/apache2/htdocs/example_site2
ServerName  www.example-site2.com
ErrorLog  /usr/local/apache2/logs/site2_error_log 
TransferLog /var/log/proftpd/transfer.log
ExtendedLog /var/log/proftpd/full.log ALL
DefaultRoot /var/www/digitalgoods
User                    apache
Group                   apache
AllowOverwrite          yes
MaxLoginAttempts        3
RequireValidShell       no
</VirtualHost>


#### REDIS
Clean up:
redis-cli flushall
FLUSHDB - Removes data from your connection's CURRENT database.
FLUSHALL - Removes data from ALL databases.

#### SMS GSM and Android notes
Generally an SMS is restricted to 160 (7 bit) characters or 140 (8 bit) characters.
Unicode SMS support (70 characters in length).

http://codetheory.in/android-sms/
https://mobiforge.com/design-development/sms-messaging-android



#### SMS Gateways and APIs:
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
https://cloud.google.com/appengine/docs/python/mail/receivingmail # inbound email with appengine
www.socketlabs.com
www.elasticemail.com



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



#### Free GRIB providers - http://www.euronav.co.uk/Weather/gribfiles.htm
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


#### GnuPG, signatures and encryption
gpg --import certificate.txt
gpg --edit-key 1DCBDC01B44427C7 lsign #Signing the key if you trust it
gpg --list-keys
gpg foo.zip.sig # .sig is a detatched signature file. GnuPG will assume the file to check has the same name minus the ".sig".




#### MISCELLANEOUS notes
What is the difference between a vector and a scalar?

• Vectors have both, a magnitude and direction, but scalars have magnitude only.

• Vector equality occurs only when both the magnitude and the direction of two vectors of the same type are the same, but in the case of scalars, equality of magnitude is sufficient.

• Scalars of the same type can be added just as real numbers, but the addition of vectors should be done using the polygon law.



#### WGRIB and TOOLS
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
