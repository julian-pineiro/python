import os
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email.mime.image import MIMEImage
#Needs review soon

sent_from = 'my-mail@mail.com'
to = 'destination@mail.com'
subject = 'Subject'  
body = ''
img_data = open("invitados/"+name+".png", 'rb').read()
msg = MIMEMultipart()
msg['Subject'] = 'your-subject' #
msg['From'] = 'your@gmail.com' #
msg['To'] = mail # Check this 3 lines. MIMEMultipart functions
                #Unused in this module temporarily
text = MIMEText("Text of the e-mail")
msg.attach(text)
image = MIMEImage(img_data, name=os.path.basename("image_path.jpg"))
msg.attach(image)

#Send
try:  
    server = smtplib.SMTP_SSL('smtp.gmail.com')
    server.ehlo()
    print("Trying to log in...\n")
    server.login('your@gmail.com', 'your-password')
    print("Logged in sucessufully!\n")
    print("Sending...\n")
    server.sendmail(sent_from, to, msg.as_string())
    server.close()
    print ('Email sent!')
    
except:  
    print ('Check Internet Connection... Something went wrong! :(')

