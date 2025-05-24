import os
from email_reader import download_invoices
from pdf_parser import extract_invoice_data
from database import insert_invoice, init_db

def process_invoices():
    EMAIL = os.getenv("EMAIL_USER")
    PASSWORD = os.getenv("EMAIL_PASSWORD")

    # 1. Download new invoices from email
    download_invoices(EMAIL, PASSWORD)

    # 2. Go through each PDF file in 'invoices/'
    for filename in os.listdir("invoices"):
        if filename.endswith(".pdf"):
            filepath = os.path.join("invoices", filename)
            data = extract_invoice_data(filepath)

            if data["date"] and data["amount"]:
                insert_invoice(data)
                print(f"Inserted: {data}")
            else:
                print(f"Skipped: {filename} — Missing data")

if __name__ == "__main__":
    init_db()
    process_invoices()
