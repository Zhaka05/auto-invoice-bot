import os
import imaplib
import email
from email.header import decode_header

def download_invoices(imap_user, imap_pass):
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(imap_user, imap_pass)
    mail.select("inbox")

    status, messages = mail.search(None, 'SUBJECT "Invoice"')
    for num in messages[0].split():
        status, data = mail.fetch(num, "(RFC822)")
        msg = email.message_from_bytes(data[0][1])
        for part in msg.walk():
            if part.get_content_type() == "application/pdf":
                filename = part.get_filename()
                if filename:
                    with open(f"invoices/{filename}", "wb") as f:
                        f.write(part.get_payload(decode=True))