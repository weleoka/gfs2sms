""" Configuration file for gfs2sms and gfs2sms utilities package.

basic settings define general configuration and info.
	- name: program name.
	- version: program version.
	- author: developer name.
	- contributors: various people who have contributed to development.
	- author_email: developer email_in
	- bug_reports: bugg repport submissions.
	- logging_level: basic/advanced. This effects the logging module and sets handlers, filters and loggers.
		Recommended level is basic for the time being.

email_in settings define server and account details as well as connection properties.
	- server: the URL of the IMAP server.
	- port: the port used for establishing IMAP connection. SSL default is 993. Can be set to None.
	- timeout: how many seconds before the timeout exception is thrown by socket module.
	- email: the user email.
	- password: user password (note the dangers of having this in plaintext)
	- ssl: set to true or false for SSL vs non-SSL connection.

basicLog settings define how the programs logging function behaves.
	- level: levels are critical, error, warning, info, debug and none.
	- file: set to /dev/stdout or to a logfile name.
	- format: the formatting of an entry.
	- dateformat: the timestamp of a log entry.

advLog settings define how the programs logging function behaves. 
This is for usage in the logging.config.dictConf() function for configuring the python standard logging module.
"""

basic = {
'name': 'gfs2sms',
'version': '0.0.1',
'author': 'weleoka',
'contributors': '',
'author_email': 'none@none.now',
'bug_reports': 'none@none.now',
'logging_level': 'basic' # Set to basic (or advanced - not operational)
}

email_in = {
'server': 'imap.gmail.com', 
'port': 993,
'timeout': 5,
'email': '@gmail.com',
'password': '',
'ssl': True
}

from gfs2sms import logging_tools
statistics = {
'data_categories': ['mail', 'binary', 'headers', 'request'],
'volume_data_in': 'make function read from log file',
'volume_data_out': 'make function read from log file'
}

basicLog = {
'level': 'debug',
'file': '/dev/stdout',	#set to /dev/stdout to print to cosole or pipe.
'format': '%(asctime)s <%(name)s> %(levelname)s %(message)s',
'dateformat': '%m/%d/%Y %I:%M:%S %p'
}

advLog = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
	'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'default': {
            'format': '%(asctime)s <%(name)s> %(levelname)s %(message)s'
        }
    },
    'filters': {
        'myfilter': {
            '()': logging_tools.MyFilter,
            'param': 'noshow'
        }
    },
    'handlers': {
        'data_in':{
            # The values below are popped from this dictionary and
            # used to create the handler, set the handler's level and
            # its formatter.
            '()': logging_tools.owned_file_handler,
            'level':'DEBUG',
            'formatter': 'default',
            # The values below are passed to the handler creator callable
            # as keyword arguments.
            'owner': ['pulse', 'pulse'],
            'filename': 'chowntest.log',
            'mode': 'w',
            'encoding': 'utf-8'
        },
        'console': {
            'class': 'logging.StreamHandler',
            'filters': ['myfilter']
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'gfs2sms.logging_tools.AdminEmailHandler',
            'filters': ['special']
        },
    },
    'loggers': {
        'root': {
            'handlers':['file'],
            'propagate': False,
            'level':'INFO'
        },
        'default': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False
        },
        'myproject.custom': {
            'handlers': ['console', 'mail_admins'],
            'level': 'INFO',
            'filters': ['special']
        }
    }
}