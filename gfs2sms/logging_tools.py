from __future__ import unicode_literals

import json
import logging
import config as configFile



# This next bit is to ensure the script runs unchanged on 2.x and 3.x
try:
    unicode

except NameError:
    unicode = str

class Encoder(json.JSONEncoder):


    def default(self, o):

        if isinstance(o, set):

            return tuple(o)

        elif isinstance(o, unicode):

            return o.encode('unicode_escape').decode('ascii')

        return super(Encoder, self).default(o)




# Custom formatter classes

class StructuredMessage(object):
    # usage:
    # ### Using custom logging helper class to output structured log entry.
    # _ = StructuredMessage   # optional, to improve readability
    # logging.info(_('message 1', set_value=set([1, 2, 3]), snowman='\u2603'))


    def __init__(self, message, **kwargs):
        self.message = message
        self.kwargs = kwargs


    def __str__(self):
        s = Encoder().encode(self.kwargs)

        return '%s >>> %s' % (self.message, s)



class OneLineExceptionFormatter(logging.Formatter):


    def formatException(self, exc_info):
        """
        Format an exception so that it prints on a single line.
        """
        result = super(OneLineExceptionFormatter, self).formatException(exc_info)

        return repr(result) # or format into one line however you want to

    def format(self, record):
        s = super(OneLineExceptionFormatter, self).format(record)
        if record.exc_text:
            s = s.replace('\n', '') + '|'

        return s



def initialiseLogging ():

    if configFile.basic['logging_level'] == 'basic':
        logargs = configFile.basicLog
        logargs['level'] = getattr(logging, logargs['level'].upper(), None)
        
        if isinstance(logargs['level'], int):
            logging.basicConfig(
            level=logargs['level'],
            file=logargs['file'],
            format=logargs['format'],
            dateformat=logargs['dateformat'])
        
        else:
        
            raise ValueError('Invalid basicLog level: %s' % logargs['level'])

    elif configFile.basic['logging_level'] == 'advanced':
        # # Set dictonary configured logging (advanced) according to configFile.advLog
        # logargs = configFile.advLog
        # logging.config.dictConfig(logargs)
        raise ValueError('Invalid logging_level in configFile: %s' % (configFile.basic['logging_level']))

    return True


# Custom logging handlers
def owned_file_handler (filename, mode='a', encoding=None, owner=None):

    if owner:

        import os, pwd, grp
        # convert user and group names to uid and gid
        uid = pwd.getpwnam(owner[0]).pw_uid
        gid = grp.getgrnam(owner[1]).gr_gid
        owner = (uid, gid)

        if not os.path.exists(filename):
            open(filename, 'a').close()
        os.chown(filename, *owner)

    return logging.FileHandler(filename, mode, encoding)



def stats_data_in_handler (volume=None, category=None):

    if category in configFile.statistics['data_categories']:
        print ("Recording %s" % (category))

    pass


def stats_data_out_handler (volume=None, category=None):

    pass



# Custom logging filters
class MyFilter(logging.Filter):


    def __init__(self, param=None):
        self.param = param


    def filter(self, record):

        if self.param is None:
            allow = True

        else:
            allow = self.param not in record.msg

        if allow:
            record.msg = 'changed: ' + record.msg

        return allow