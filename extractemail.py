import imaplib,email
import time
import datetime as dt
from os import path
from datetime import timezone

user="sachinbst41@gmail.com"
password="utkarsh@123"
imap_url ="imap.gmail.com"

def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None,True)
date_time = dt.datetime.now()
f=open("gmail_time.txt","r")
a=f.read()
f.close()

a= dt.datetime.strptime(a,'%a,%d,%b,%Y,%H:%M:%S %Z')

date_time.replace(tzinfo=timezone.utc)

date_time=date_time.replace(tzinfo=timezone.utc).isoformat()

date_time=dt.datetime.strptime(date_time,'%Y-%m-%dT%H:%M:%S.%f%z')

lastDayDateTime = date_time -a

con = imaplib.IMAP4_SSL(imap_url)
con.login(user,password)
con.select('INBOX')
dates = (dt.datetime.now()-lastDayDateTime).strptime('%d-%b-%Y')
resp,items = con.uid('search', None,'(SENTSINCE {date})'.format(date=dates))
a = items
b=a[0].decode('utf-8')
b=b.split(" ")
f1= open("gmail_mails.txt","w+")

for value in b:
    late=int(value)-801
    late =str(late)
    result,data =con.fetch(late,'(RFC822)')
    raw = email.message_from_bytes(data[0][1])
    print(raw['Date'])
    print(raw['From'])
    print(raw['Body'])
    f1.write('Date = '+ raw['Date'] + ' ')
    f1.write('From = '+ raw['From'] + ' ')
    f1.write('Subject = '+ raw['Subject'] + ' ')
    f1.write('Body = '+ str(get_body(raw)) + ' ')
    f1.write(' ')
f1.close()
f2= open("gmail_time.txt","w+")
f2.write(raw['Date'])
f2.close()












