import traceback
import sys
 
from grib_api import *
 
INPUT='../tg02.grb'
VERBOSE=1 # verbose error reporting
 
def example():
    f = open(INPUT)
 
    mcount = gribapi.grib_count_in_file(f)
    gid_list = [gribapi.grib_new_from_file(f) for i in range(mcount)]
 
    f.close()
 
    keys = [
        'Ni',
        'Nj',
        'latitudeOfFirstGridPointInDegrees',
        'longitudeOfFirstGridPointInDegrees',
        'latitudeOfLastGridPointInDegrees',
        'longitudeOfLastGridPointInDegrees',
        'jDirectionIncrementInDegrees',
        'iDirectionIncrementInDegrees',
        ]
 
    for i in range(mcount):
        gid = gid_list[i]
 
        print "processing message number",i+1
 
        for key in keys:
            print '%s=%g' % (key,gribapi.grib_get(gid,key))
 
        print 'There are %d, average is %g, min is %g, max is %g' % (
                  gribapi.grib_get_size(gid,'values'),
                  gribapi.grib_get(gid,'average'),
                  gribapi.grib_get(gid,'min'),
                  gribapi.grib_get(gid,'max')
               )
 
        print '-'*100
 
        gribapi.grib_release(gid)
 
 
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