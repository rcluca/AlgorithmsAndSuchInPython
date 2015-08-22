import imaplib, email, re
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
imap_pass = input("Please enter password: ")

## open a connection 
imap = imaplib.IMAP4_SSL(imap_host)

## login
imap.login(imap_user, imap_pass)

## select a specific folder
status, data = imap.select('Flight Deal')

## retrieve and print all messages
msg = ""
typ, data = imap.search(None, 'ALL')
for num in data[0].split():

    # get message
    typ, data = imap.fetch(num, '(RFC822)')
    
    # parse message into required info
    msg = data[0][1]
    match = re.search(r"You are receiving this email because you elected to receive emails from", msg)
    if (match != None):
        msg = msg[match.regs[0][1]:]
    match = re.search(r"http://theflightdeal.us3.list-manage1.com", msg)
    if (match != None):
        msg = msg[:match.regs[0][0]]
    msg = msg.replace("\r\n", "").replace("=2C", ", ")
    msg = re.sub("http:.* ","",msg)
    
    msgList = msg.split("*")
    
    for m in msgList:
        subMsg1 = m.split("=E2=80=93")
        for sm1 in subMsg1:
            sm1 = sm1.replace("=", "")
            print sm1
    
imap.close()
imap.logout()