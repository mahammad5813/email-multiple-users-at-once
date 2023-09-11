import smtplib
from email.message import EmailMessage
email_sender = 'senderexample@organization.edu.uk'
email_password = "password"
email_receiver_list = ['recmail1@gmail.com', "recmail2@gmail.com", 'recmail3@gmail.com']

subject = "Subject"
body = '''
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum
'''
for email_receiver in email_receiver_list:
    mailserver = smtplib.SMTP('smtp.office365.com',587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.login(email_sender, email_password)
    #Adding a newline before the body text fixes the missing message body
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject


    em.set_content(body)

    mailserver.sendmail(email_sender, email_receiver, em.as_string())
    mailserver.quit()
