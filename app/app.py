import os
from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)


def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),
        database=os.getenv("DB_NAME", "devopsdb"),
        user=os.getenv("DB_USER", "devopsuser"),
        password=os.getenv("DB_PASSWORD", "devopspassword"),
    )
    return conn


@app.route("/")
def index():
    return jsonify({"message": "Welcome to DevOps Flask App!"})


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


@app.route("/users")
def users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, username FROM users;")
    users_data = cur.fetchall()
    cur.close()
    conn.close()

    users_list = [{"id": u[0], "username": u[1]} for u in users_data]
    return jsonify(users_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    #fix