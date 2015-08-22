import imaplib
from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

imap_host = "imap.mail.yahoo.com"
imap_user = "rc_luca@yahoo.com"
imap_pass = input()

## open a connection 
imap = imaplib.IMAP4_SSL(imap_host)

## login
imap.login(imap_user, imap_pass)

## get status for the mailbox (folder) INBOX
folderStatus, UnseenInfo = imap.status('INBOX', "(UNSEEN)")

print folderStatus

NotReadCounter = int(UnseenInfo[0].split()[2].strip(').,]'))
print NotReadCounter

### create a new folder
#status, createFolder_response = imap.create('myFolders.xyz')

### folders list
#status, folder_list = imap.list()

### list sub-folders
#status, sub_folder_list = imap.list(directory='insd')

## select a specific folder
status, data = imap.select('Flight Deal')

### searching current folder using title keywords 
#status, messages = imap.search(None, '(SUBJECT "Work Report")')
 
### fetching message header by  using message( ID)
#status, msg_header = imap.fetch('1', '(BODY.PEEK[HEADER])')

### fetching the full message ( ID=1)
#status, AllTheMessage= imap.fetch('1', '(RFC822)')

### moving/copying messages around folders
#status, messages  = imap.copy(msg_ids, 'myFolders.xyz')
#status, messages  = imap.move(msg_ids, 'otherFolder')

typ, data = imap.search(None, 'ALL')
for num in data[0].split():
    typ, data = imap.fetch(num, '(RFC822)')
    print 'Message %s\n%s\n' % (num, strip_tags(data[0][1]))

imap.close()
imap.logout()