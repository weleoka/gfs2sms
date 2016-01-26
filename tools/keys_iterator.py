import traceback
import sys
 
from grib_api import gribapi
 
INPUT='../tg02.grb'
VERBOSE=1 # verbose error reporting
 
def example():
    f = open(INPUT)
 
    while 1:
        gid = gribapi.grib_new_from_file(f)
        if gid is None: break
 
        iterid = gribapi.grib_keys_iterator_new(gid,'ls')
 
        # Different types of keys can be skipped
        # grib_skip_computed(iterid)
        # grib_skip_coded(iterid)
        # grib_skip_edition_specific(iterid)
        # grib_skip_duplicates(iterid)
        # grib_skip_read_only(iterid)
        # grib_skip_function(iterid)
 
        while gribapi.grib_keys_iterator_next(iterid):
            keyname = gribapi.grib_keys_iterator_get_name(iterid)
            keyval = gribapi.grib_get_string(iterid,keyname)
            print "%s = %s" % (keyname,keyval)
 
        gribapi.grib_keys_iterator_delete(iterid)
        gribapi.grib_release(gid)

        print "- - -"
 
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