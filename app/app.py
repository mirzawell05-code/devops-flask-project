from flask import Flask
import psycopg2
import os
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)


@app.route("/")
def home():
    return "DevOps Flask Project is running!"


@app.route("/health")
def health():
    return {"status": "ok"}


@app.route("/users")
def users():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    cur = conn.cursor()
    cur.execute("SELECT name FROM users;")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return {"users": [row[0] for row in rows]}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    