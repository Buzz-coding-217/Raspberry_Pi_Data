#import smtplib

#Email Variables
#SMTP_SERVER = 'smtp.gmail.com' #Email Server (don't change!)
#SMTP_PORT = 587 #Server Port (don't change!)
#GMAIL_USERNAME = 'smartshop.3765@gmail.com' #change this to match your gmail account
#GMAIL_PASSWORD = 'poiu@0987'  #change this to match your gmail app-password

#class Emailer:
    #def sendmail(self, recipient, subject, content):

        #Create Headers
        #headers = ["From: " + GMAIL_USERNAME, "Subject: " + subject, "To: " + recipient,
                   #"MIME-Version: 1.0", "Content-Type: text/html"]
        #headers = "\r\n".join(headers)

        #Connect to Gmail Server
        #session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        #session.ehlo()
        #session.starttls()
        #session.ehlo()

        #Login to Gmail
        #session.login(GMAIL_USERNAME, GMAIL_PASSWORD)

        #Send Email & Exit
        #session.sendmail(GMAIL_USERNAME, recipient, headers + "\r\n\r\n" + content)
        #session.quit
        
#sender = Emailer()

#sendTo = 'smartshop.3765@gmail.com'
#emailSubject = "Hello World"
#emailContent = "This is a test of my Emailer Class"

#print("1")

#Sends an email to the "sendTo" address with the specified "emailSubject" as the subject and "emailContent" as the email content.
#sender.sendmail(sendTo, emailSubject, emailContent)
import smtplib
smtpUser = 'smartshop.3765@gmail.com'
smtpPass = 'wyajvfhlobjyrtmd'
toAdd = 'smartshop.3765@gmail.com'
fromAdd = smtpUser
subject = 'TEST EMAIL using PYTHON'
header = 'To: ' + toAdd + '\n' + 'From: ' + fromAdd + '\n' + 'Subject: ' + subject
body = 'From PYTHON Program sending EMAIL'
print(header + '\n' + body)
s = smtplib.SMTP('smtp.gmail.com',587)
s.ehlo()
s.starttls()
s.ehlo()
s.login(smtpUser, smtpPass)
print("Login Successfull")
s.sendmail(fromAdd, toAdd, header + 'In\n' + body)

s.quit()