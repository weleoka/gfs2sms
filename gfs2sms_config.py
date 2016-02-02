## Configuration file for gfs2sms
#
# email_in settings define server and account details as well as connection properties.
#	- server: the URL of the IMAP server.
#	- port: the port used for establishing IMAP connection. SSL default is 993. Can be set to None.
#	- timeout: how many seconds before the timeout exception is thrown by socket module.
#	- email: the user email.
#	- password: user password (note the dangers of having this in plaintext)
#	- ssl: set to true or false for SSL vs non-SSL connection.
#
# log settings define how the programs logging function behaves.
#	- level: levels are critical, error, warning, info, debug and none.
#	- file: set to /dev/stdout or to a logfile name.
#	- format: the formatting of an entry.
#	- dateformat: the timestamp of a log entry.
#

email_in = {
'server': 'imap.gmail.com', 
'port': 993,
'timeout': 5,
'email': '@gmail.com',
'password': '',
'ssl': True
}

log = {
'level': 'debug',
'file': '/dev/stdout',	#set to /dev/stdout to print to 
'format': '%(asctime)s <%(name)s> %(levelname)s %(message)s',
'dateformat': '%m/%d/%Y %I:%M:%S %p'
}