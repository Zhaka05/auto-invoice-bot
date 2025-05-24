import re
import PyPDF2

def extract_invoice_data(filepath):
    with open(filepath, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = "\n".join([page.extract_text() for page in reader.pages])

    date = re.search(r"Date: (\d{2}/\d{2}/\d{4})", text)
    amount = re.search(r"Amount: \$(\d+\.\d{2})", text)
    return {
        "date": date.group(1) if date else "",
        "amount": amount.group(1) if amount else ""
    }
