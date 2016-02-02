#!/usr/bin/env python3
import imaplib
import socket

#http://www.programcreek.com/python/example/2875/imaplib.IMAP4_SSL

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

    def __init__(self, args):
        self.server = args['server']
        self.port = args['port']
        self.timeout = args['timeout']
        self.email = args['email']
        self.password = args['password']

        socket.setdefaulttimeout(self.timeout)


        if args['ssl']:
            print("Connecting with SSL to %s ..." % (self.server))
            self.imap = imaplib.IMAP4_SSL
        else:
            print ("Connecting unsecurely to %s ..." % (self.server))
            self.imap = imaplib.IMAP4

        imap = self.imap(self.server, self.port)

        try:
            imap.login(self.email, self.password)
            self.state = imap.select()
        except imaplib.IMAP4.error:
            raise Exception("Incorrect username/password for %s" % self.email)
        except socket.error as serr:
            if serr.errno == errno.ECONNREFUSED:
                raise Exception("Connection refused. Check server configuration.")
            if serr.errno == errno.ECONNRESET:                
                raise Exception("Incorrect username/password for %s" % self.email)
            # Not the error we are looking for, re-raise
            raise serr

        imap.logout()

        print ("Created IMAP Reader for %s" % self.email)

   

# print ("Connecting to %s" %(conf.username))
# mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
# mail.login(conf.username, conf.pswd)
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



    def GetMailWithAttachments(userName, password, resumeFile):
        imapSession = imaplib.IMAP4_SSL('imap.gmail.com')
        typ, accountDetails = imapSession.login(userName, password)

        print(typ)
        print(accountDetails)
        if typ != 'OK':
            print('Not able to sign in!')
            raise

        imapSession.select('[Gmail]/All Mail')
        typ, data = imapSession.search(None, '(X-GM-RAW "has:attachment")')
        # typ, data = imapSession.search(None, 'ALL')
        if typ != 'OK':
            print('Error searching Inbox.')
            raise

        # Iterating over all emails
        for msgId in data[0].split():
            NewMsgIDs.add(msgId)
            typ, messageParts = imapSession.fetch(msgId, '(RFC822)')
            if typ != 'OK':
                print('Error fetching mail.')
                raise
            emailBody = messageParts[0][1]
            if msgId not in ProcessedMsgIDs:
                yield email.message_from_string(emailBody)
                ProcessedMsgIDs.add(msgId)
                with open(resumeFile, "a") as resume:
                    resume.write('{id},'.format(id=msgId))

        imapSession.close()
        imapSession.logout()

