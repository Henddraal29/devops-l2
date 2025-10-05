from flask import Flask
import os, psycopg2

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello DevOps by Hendra"

@app.route("/db")
def db():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),
        user=os.getenv("POSTGRES_USER", "postgres"),
        password=os.getenv("POSTGRES_PASSWORD", "secret"),
        dbname=os.getenv("POSTGRES_DB", "appdb"),
    )
    cur = conn.cursor()
    cur.execute("SELECT 1")
    cur.fetchone()
    cur.close()
    conn.close()
    return "DB OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
