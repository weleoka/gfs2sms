""" gfs2sms helper functions

Contains:
	function readParameters. 
		Reads flags/parameters from commandline,
		and modifies gfs2sms config dictionary accordingly.
"""

import getopt
import logging
import logging.config
import gfs2sms.config as configFile


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

