#!/usr/bin/env python
"""
Module to fish data out of GFS GRIB files and fit it into the gfs2sms protocol.

Please report any issues to weleoka@github.com
"""

import traceback
import sys

from grib_api.gribapi import *
from gfs2sms_utils import wind_tools as wt

INPUT='tg02.grb'
VERBOSE=1 # verbose error reporting


def example():
    # print wt.get_wind_spd_kts(10, 12)
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
    sys.exit(main())