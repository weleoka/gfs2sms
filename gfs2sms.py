#!/usr/bin/env python
# Copyright 2016 (c) Kai Weeks.
# See LICENSE for details.
"""
Main app to connect an email snd/rcv functionality and retrieve data out of attatchments of GFS GRIB2 files.
The data will then be formatted to fit it into the gfs2sms protocol.
It also interacts with web API services to forward the data to various devices.

Please report any issues to weleoka at github.
"""

import sys, os

# This makes sure that developers don't have to set up their environment specially in order to run gfs2sms. It is only a developer convenience.  By the time gfs2sms is actually installed somewhere, the environment should already be set up properly without the help of this linking.
sys.path.append(os.path.abspath('vendor'))
# print (sys.path)

# logging module
import logging
import logging.config

# Library for working with GRIB files.
# import gribapi

#gfs2sms dependencies
from gfs2sms import config as configFile
from gfs2sms import logging_tools
from gfs2sms import utils
# from gfs2sms import wind_tools as w_t
from gfs2sms import email


def startpoint ():
    """ Gfs2sms startpoint function.

    The function from which all else takes place.

    parameters:
        void

    returns:
        boolean: success 0, fail 1.
    """

    # Create IMAP instance.
    IMAP = email.Email_in(configFile)

    # Call connect method.
    IMAP.connectIMAP()

    # Call close method.
    IMAP.closeIMAP()

    return(0)


if __name__ == "__main__":

    # Set logging according to parameters from config file.
    try:
        logging_tools.initialiseLogging()
        logging.info ("Started gfs2sms.")
    except ValueError:
        print ("Error: problem initialising logging module.")

    # Read parameters from command line, if present, to modify configuration.
    if len(sys.argv[1:]) > 0:
        utils.readParameters(sys.argv[1:])

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