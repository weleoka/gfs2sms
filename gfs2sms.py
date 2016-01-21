import traceback
import sys
import math

from grib_api.gribapi import *

INPUT='../testgrib2.grb'
VERBOSE=1 # verbose error reporting


def get_wind_spd_kts(x, y):
    spd_mps = math.hypot(x, y)
    return spd_mps * 1.943844 # The constant for calculating kts from m/s.


def get_wind_spd_mps(x, y):
    return math.hypot(x, y)


def get_wind_dir_degrees(x, y):
    radians = math.atan2(y, x)
    return math.degrees(radians)


def example():
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