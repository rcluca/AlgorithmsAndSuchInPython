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
imap_pass = input()

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
    msg = msg[match.regs[0][1]:]
    match = re.search(r"http://theflightdeal.us3.list-manage1.com", msg)
    msg = msg[:match.regs[0][0]]
    msg = msg.replace("\r\n", "").replace("=2C", ", ")
    
    msgList = msg.split("*")
    
    for m in msgList[2:]:
        subMsg1 = m.split("=E2=80=93")
        for sm1 in subMsg1:
            sm1 = sm1.replace("=", "")
            print sm1
    
imap.close()
imap.logout()


# Th=
#e Flight Deal
#Deals for 07/02/2015:
#* Save the Date: The Flight Deal Team NYC Meet & Greet =E2=80=93 Tuesday=
#=2C August 4th=2C 2015
#* Air France =E2=80=93 $742: Phoenix / Dallas / Miami / Philadelphia / Cha=
#rlotte / St. Louis =E2=80=93 Skopje=2C Macedonia. Roundtrip=2C including a=
#ll Taxes
#* Air Canada =E2=80=93 $715: San Francisco =E2=80=93 Seoul=2C South Korea.=
# Roundtrip=2C including all Taxes
#* American =E2=80=93 $225: Philadelphia =E2=80=93 Salt Lake City=2C Utah (=
#and vice versa). Roundtrip=2C including all Taxes
#* Aeromexico =E2=80=93 $318: Boston =E2=80=93 Cabo San Lucas=2C Mexico. Ro=
#undtrip=2C including all Taxes
#* American =E2=80=93 $812: Los Angeles =E2=80=93 Barcelona=2C Spain. Round=
#trip=2C including all Taxes
#* The Shorthaul =E2=80=93 United =E2=80=93 $146: Chicago =E2=80=93 Fort La=
#uderdale (and vice versa). Roundtrip=2C including all Taxes
#* United =E2=80=93 $821: Newark =E2=80=93 Jakarta=2C Indonesia. Roundtrip=
#=2C including all Taxes
#* KLM =E2=80=93 $577: Washington D.C. =E2=80=93 St. Petersburg=2C Russia.=
# Roundtrip=2C including all Taxes
#* Copa =E2=80=93 $202: Washington D.C.  =E2=80=93 San Salvador=2C El Salva=
#dor. Roundtrip=2C including all Taxes
#* [FARE GONE] Alaska =E2=80=93 $196: Baltimore =E2=80=93 Los Angeles (and=
# vice versa). Roundtrip=2C including all Taxes