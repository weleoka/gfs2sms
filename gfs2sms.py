#!/usr/bin/env python
# Copyright 2016 (c) Kai Weeks.
# See LICENSE for details.
"""
Main app to connect an email snd/rcv functionality and retrieve data out of attatchments of GFS GRIB2 files.
The data will then be formatted to fit it into the gfs2sms protocol. 
It also interacts with web API services to forward the data to various devices.

Please report any issues to weleoka at github.
"""

import sys, os, getopt

# This makes sure that developers don't have to set up their environment
# specially in order to run gfs2sms.
# It is only a developer convenience.  By the time gfs2sms is actually installed somewhere,
# the environment should already be set up properly without the help of this linking.
sys.path.append(os.path.abspath('vendor'))
# print (sys.path)

import logging
import logging.config
#from gfs2sms.logging_tools import StructuredMessage

# Library for working with GRIB files.
# import gribapi

import gfs2sms.config as configFile
import gfs2sms.logging_tools
from gfs2sms import wind_tools as w_t
from gfs2sms.email import Email_in


# Set logging according to parameters from config file.
gfs2sms.logging_tools.initialiseLogging()



def readParameters (argv):
    """ Commandline parameter parser.

    Function to parse parameters from commandline and modify gfs2sms config dictionary accordingly.
    Note that fail and success in this function is not passed to program logger or log file.

    parameters:
        argv

    returns:
        void
    """
    logging.info ("Reading command line parameters...")

    try:
      opts, args = getopt.getopt(argv,"he:p:",["help", "email=","password="])
    except getopt.GetoptError:
      print ('gfs2sms: unrecognized option.\nTry gfs2sms --help for more information.')
      logging.exception("Invalid commandline option: %s" % str(argv))
      sys.exit(2)

    for opt, arg in opts:
      if opt in ("-h", "--help"):
         print 'usage: ./gfs2sms.py -e <email> -p <password>'
         sys.exit()
      elif opt in ("-e", "--email"):
         configFile.email_in['email'] = arg
      elif opt in ("-p", "--password"):
         configFile.email_in['password'] = arg

    print 'found parameter email: ', configFile.email_in['email']
    print 'found parameter password: ', configFile.email_in['password']
    # Read from commandline file param or stdin.
    # import fileinput # https://docs.python.org/2/library/fileinput.html
    # for line in fileinput.input(): 
    #    INPUT = line



def startpoint ():
    """ Gfs2sms startpoint function

    The function from which all else takes place.

    parameters:
        void

    returns:
        boolean: success 0, fail 1.
    """

    # Create email_in instance
    email_in = Email_in(configFile)

    res = email_in.connectIMAP()

    if res:
        email_in.closeIMAP()   


    else:
        logging.info ("Failed to establish IMAP connection to %s" % email_in.server)
        return(1)



if __name__ == "__main__":

    logging.info ("Started gfs2sms.")

    # Read parameters from command line, if present, to modify configuration.
    if len(sys.argv[1:]) > 0:
        readParameters(sys.argv[1:])

    # Call main/startpoint function.
    sys.exit(startpoint())



    # More configuration.

    #INPUT='../data/tg02.grb'# This will come dynamically from classes in email module

    # def example():
    #     grib_processor = "vendor/wgrib2";
    #     output_file = "../data/processed/usernameLATLONG";
    #     command = grib_processor + " -s -d 1 " + grib_file + " | " + grib_processor + " -i -text " + grib_file + " -o " + output_file;

    #     # subprocess.call(['./test.sh'])

    #     print w_t.get_wind_spd_kts(10, 12)
    #     # pv = {}
    #     # index_keys = ["rec","shortName","level","stepRange"]
    #     # index = grib_index_new_from_file(INPUT,index_keys)
    #     # for rec in grib_index_get(index,'rec'):
    #     #     grib_index_select(index,'rec',rec)
    #     #     gid = grib_new_from_index(index)
    #     #     print gid
    #     #     pv = grib_get_array(gid,'rec')
    #     # grib_release(gid)
    #     # grib_index_release(index)

    #     f = open(INPUT)
    #     gid = grib_new_from_file(f)
    #     msg_count = grib_count_in_file (f)
    #     print (msg_count)

    #     values = grib_get_values(gid)
    #     for i in xrange(len(values)):
    #         print "%d %.10e" % (i+1,values[i])

    #     print '%d values found in %s' % (len(values),INPUT)

    #     for key in ('max','min','average'):
    #         print '%s=%.10e' % (key,grib_get(gid,key))

    #     grib_release(gid)
    #     f.close()


    # def main():
    #     try:
    #         example()
    #     except GribInternalError,err:
    #         if VERBOSE:
    #             traceback.print_exc(file=sys.stderr)
    #         else:
    #             print >>sys.stderr,err.msg

    #         return 1