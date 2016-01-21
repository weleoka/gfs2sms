import traceback
import sys

from grib_api import gribapi

INPUT='../testgrib.grb'
VERBOSE=1 # verbose error reporting

def example():
    f = open(INPUT)
    gid = gribapi.grib_new_from_file(f)

    values = gribapi.grib_get_values(gid)
    for i in xrange(len(values)):
        print "%d %.10e" % (i+1,values[i])

    print '%d values found in %s' % (len(values),INPUT)

    for key in ('max','min','average'):
        print '%s=%.10e' % (key,gribapi.grib_get(gid,key))

    gribapi.grib_release(gid)
    f.close()

def main():
    try:
        example()
    except gribapi.GribInternalError,err:
        if VERBOSE:
            traceback.print_exc(file=sys.stderr)
        else:
            print >>sys.stderr,err.msg

        return 1

if __name__ == "__main__":
    sys.exit(main())