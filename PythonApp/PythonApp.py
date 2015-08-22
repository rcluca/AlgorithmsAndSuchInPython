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

class FlightInfo():
    date = ""
    airline = ""
    price = 0
    departingCities = []
    destinationCities = []

    def __init__(self):
        self.departingCities = []
        self.destinationCities = []

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

## retrieve and print all unread messages
msg = ""
typ, data = imap.search(None, '(UNSEEN)')

## create an empty list to store FlightInfo objects
allFlights = []

for num in data[0].split():

    try:

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

        # use list splicing to remove : from end then regex to replace everything before the space before date
        date = re.sub(".* ","",msgList[0][:len(msgList[0])-1])

        for m in msgList[2:]:
            subMsg1 = m.split("=E2=80=93")
        
            idx = 0
            first = subMsg1[0].replace("=", "").strip()

            # skip if Fare Gone
            if (first[:11] != "[FARE GONE]"):

                # initialize flight object
                flight = FlightInfo()
                flight.date = date

                # jump to next index if first index is "The Shorthaul"
                if (first == "The Shorthaul"):
                    idx += 1

                # get airline
                flight.airline = subMsg1[idx].replace("=", "").strip()
                idx += 1
        
                # get price and departing cities
                priceCityMsg = subMsg1[idx].split(":")
                flight.price = int(priceCityMsg[0].replace(r"$", "").strip())
                departingCitiesList = priceCityMsg[1].replace(r"=", "").split(r"/")
                for city in departingCitiesList:
                    flight.departingCities.append(city.strip())
                idx += 1

                # get destination
                destinationCitiesList = subMsg1[idx].replace(r"==2E", "").replace(r"=", "").replace(r".", "").replace(r"(and vice versa)", "").replace(r" Roundtrip,  including all Taxes", "").split(r"/")
                for city in destinationCitiesList:
                    flight.destinationCities.append(city.strip())

                # add flight object to running list
                allFlights.append(flight)

    except:
        pass
   
imap.close()
imap.logout()

for flight in allFlights:
    print flight.date, flight.price