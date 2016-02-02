#!/usr/bin/env python
"""
Module to fish data out of GFS GRIB2 files and fit it into the gfs2sms protocol.

Please report any issues to weleoka at github.
"""

import traceback
import sys
import fileinput # https://docs.python.org/2/library/fileinput.html
import subprocess
import logging

import gribapi
import imaplib
import gfs2sms_config as conf
from gfs2sms_utils import wind_tools as w_t
from gfs2sms_utils.email import Email_in

logging.basicConfig(level = logging.DEBUG)
logging.basicConfig(filename=conf.general['logfile'], format = conf.general['logformat'], datefmt = conf.general['logdateformat'])
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')

VERBOSE=1 # verbose error reporting
INPUT='../data/tg02.grb'

# Read from commandline file param or stdin.
# for line in fileinput.input(): 
#    INPUT = line

def example():
    grib_processor = "vendor/wgrib2";
    output_file = "../data/processed/usernameLATLONG";
    command = grib_processor + " -s -d 1 " + grib_file + " | " + grib_processor + " -i -text " + grib_file + " -o " + output_file;

    # subprocess.call(['./test.sh'])

    print w_t.get_wind_spd_kts(10, 12)
    # pv = {}
    # index_keys = ["rec","shortName","level","stepRange"]
    # index = grib_index_new_from_file(INPUT,index_keys)
    # for rec in grib_index_get(index,'rec'):
    #     grib_index_select(index,'rec',rec)
    #     gid = grib_new_from_index(index)
    #     print gid
    #     pv = grib_get_array(gid,'rec')
    # grib_release(gid)
    # grib_index_release(index)

    f = open(INPUT)
    gid = grib_new_from_file(f)
    msg_count = grib_count_in_file (f)
    print (msg_count)

    values = grib_get_values(gid)
    for i in xrange(len(values)):
        print "%d %.10e" % (i+1,values[i])

    print '%d values found in %s' % (len(values),INPUT)

    for key in ('max','min','average'):
        print '%s=%.10e' % (key,grib_get(gid,key))

    grib_release(gid)
    f.close()


def main():
    try:
        example()
    except GribInternalError,err:
        if VERBOSE:
            traceback.print_exc(file=sys.stderr)
        else:
            print >>sys.stderr,err.msg

        return 1

if __name__ == "__main__":

    Email_in(conf.email_in)

    sys.exit()
    #sys.exit(main())