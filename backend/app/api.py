from flask import Flask, jsonify
from database import get_all_invoices, init_db

app = Flask(__name__)

@app.route("/api/invoices")
def invoices():
    return jsonify(get_all_invoices())

if __name__ == "__main__":
    init_db()
    app.run(debug=True)