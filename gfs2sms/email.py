#!/usr/bin/env python3
""" IMAP connection class.

Contains:
Class email_in representing a connection to a remote server using the IMAP protocol.
"""
import imaplib
import socket
import logging

# Not a secure login google complaining:
# If you want to avoid this error without compromising your account's security, use OAuth to authenticate.
#https://developers.google.com/gmail/xoauth2_protoco
#Python sample code that shows the use of XOAUTH2 with imaplib.
#https://code.google.com/p/google-mail-oauth2-tools/wiki/OAuth2DotPyRunThrough
#You should consider enabling  two-step verification on your account to make it more secure.
#https://www.google.com/landing/2step/
#If you do, you can use an App Password to connect to IMAP.
#https://support.google.com/accounts/answer/185833
# The gmail IMAP API does not allow polling more than 1 time every 10 minutes. But maybe it can support IDLE.
# IMAP IDLE - like a push service.
# http://www.isode.com/whitepapers/imap-idle.html
# http://stackoverflow.com/questions/18103278/how-to-check-whether-imap-idle-works
#https://yuji.wordpress.com/2011/06/22/python-imaplib-imap-example-with-gmail/



class Email_in:
    """ IMAP connection class.

    Class representing a connection to a remote server using the IMAP protocol.
    """


    def __init__ (self, conf):
        """ Constructor for IMAP connection class .

        Define the object attributes according to dictionary passed in.

        parameters:
            self
            conf: A dictionary containing configuration parameters.
                email_in = {
                    'server': 'imap.gmail.com', 
                    'port': 993,
                    'timeout': 5,
                    'email': '@gmail.com',
                    'password': '',
                    'ssl': True
                }


        return:
            void
        """
        name = '.'.join([__name__, self.__class__.__name__])
 
        # Make a logger for this class.
        self.logger = logging.getLogger(name)
        self.verbose = conf.basic['verbose']
        self.strict = conf.basic['strict']

        self.args = conf.email_in
        self.server = self.args['server']
        self.port = self.args['port']
        self.timeout = self.args['timeout']  # This attribute may be superflous.
        self.email = self.args['email']
        self.password = self.args['password']
        self.ssl = self.args['ssl']

        socket.setdefaulttimeout(self.timeout)



    def connectIMAP (self):
        """ Initiate IMAP connection

        Method which runs through IMAP connection and authentification process

        Further examples:
        http://www.programcreek.com/python/example/2875/imaplib.IMAP4_SSL

        parameters:
            self: class instance.

        return:
            boolean: success 0, fail 1.
        """
        if self.ssl:
            self.logger.info ("Connecting with SSL to %s ..." % (self.server))
            self.imapType = imaplib.IMAP4_SSL

        else:
            self.logger.info ("Connecting unsecurely to %s ..." % (self.server))
            self.imapType = imaplib.IMAP4

        # Call imaplib.IMAP4 or IMAP4_SSL methods.
        self.imap = self.imapType(self.server, self.port)

        try:
            typ, accountDetails = self.imap.login(self.email, self.password)
            self.state = self.imap.select()
            print(typ)
            print(accountDetails)
            if typ != 'OK':
                print('Not able to sign in!')
                raise

        except imaplib.IMAP4.error, Argument:
            self.logger.exception("imaplib.IMAP4: %s " % (Argument))
            if self.verbose:
                traceback.print_exc(file=sys.stderr)
            if self.strict:
                raise Exception("imaplib.IMAP4 error %s")
            return False

        except socket.error as serr:

            if serr.errno == errno.ECONNREFUSED:
                self.logger.exception("Incorrect username/password for %s" % self.email)
                if self.verbose:
                    traceback.print_exc(file=sys.stderr)
                if self.strict:
                    raise Exception("Incorrect username/password for %s" % self.email)
                return False

            if serr.errno == errno.ECONNRESET:
                self.logger.exception("Connection reset by server")
                if self.verbose:
                    traceback.print_exc(file=sys.stderr)
                if self.strict:
                    raise Exception("Connection reset by server")
                return False

            # Not the error we are looking for, re-raise.
            self.logger.exception("Unhandled error: ")
            raise serr

        else:
            # If no exceptions were thrown all is probably O.K. return True.
            return True



    def closeIMAP (self):
        """ Close IMAP connection

        Method to close the IMAP connection.

        parameters:
            self: object. Class instance

        return:
            void
        """
        self.imap.logout()
        self.logger.info ("Closed connection to %s ..." % (self.server))


# Method to download mail with attatchments
    def GetMailWithAttachments(resumeFile):
        """ Retrieve email using IMAP.

        Download an eMail with attatchments.

        parameters:
            self: object. Class instance.
            resumeFile: 

        return:
            void
        """
        self.imap = self.imap
        self.imap.select('[Gmail]/All Mail')
        typ, data = self.imap.search(None, '(X-GM-RAW "has:attachment")')
        # typ, data = self.imap.search(None, 'ALL')
        if typ != 'OK':
            print('Error searching Inbox.')
            raise

        # Iterating over all emails
        for msgId in data[0].split():
            NewMsgIDs.add(msgId)
            typ, messageParts = self.imap.fetch(msgId, '(RFC822)')
            if typ != 'OK':
                print('Error fetching mail.')
                raise
            emailBody = messageParts[0][1]
            if msgId not in ProcessedMsgIDs:
                yield email.message_from_string(emailBody)
                ProcessedMsgIDs.add(msgId)
                with open(resumeFile, "a") as resume:
                    resume.write('{id},'.format(id=msgId))




        # mail.list()

        # # Out: list of "folders" aka labels in gmail.
        # mail.select("inbox") # connect to inbox.

        # # result, data = mail.search(None, "ALL")
        # result, data = mail.uid('search', None, "ALL") # search and return uids instead
         
        # ids = data[0] # data is a list.
        # id_list = ids.split() # ids is a space separated string
        # #latest_email_id = id_list[-1] # get the latest
        # latest_email_uid = data[0].split()[-1]
         
        # #result, data = mail.fetch(latest_email_id, "(RFC822)") # fetch the email body (RFC822) for the given ID
        # result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')

        # raw_email = data[0][1] # here's the body, which is raw text of the whole email
        # # including headers and alternate payloads

        # print ("EMAIL: %s", raw_email)
