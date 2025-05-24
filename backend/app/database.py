import psycopg2
import os
# Connect to your PostgreSQL DB
# conn = psycopg2.connect(
#     dbname="testdb",
#     user="postgres",
#     password="zh051005",
#     host="localhost",  # or your host
#     port="5432"         # default PostgreSQL port
# )

def get_connection():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),  
        port=os.getenv("DB_PORT")    
    )


def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS invoices (
            id SERIAL PRIMARY KEY,
            date DATE,
            amount REAL
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

def insert_invoice(data):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO invoices (date, amount) VALUES (%s, %s)", (data['date'], data['amount']))
    conn.commit()
    cur.close()
    conn.close()

def delete_invoice(id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"DELETE FROM invoices WHERE id = {id}")
    conn.commit()
    cur.close()
    conn.close()

def get_all_invoices():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, date, amount FROM invoices")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [
        {"id": row[0], "date": row[1], "amount": float(row[2])} for row in rows
    ]
