from flask import Flask, render_template, request, redirect, url_for, session
import logging
import os

app = Flask(__name__)
app.secret_key = "forensics_secret_key"

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

# Configure logging
logging.basicConfig(
    filename="logs/login.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# Dummy credentials (INTENTIONALLY SIMPLE — good for forensics)
USERNAME = "admin"
PASSWORD = "password123"


@app.route("/", methods=["GET"])
def index():
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == USERNAME and password == PASSWORD:
            session["user"] = username
            logging.info(f"SUCCESS login from IP {request.remote_addr}")
            return redirect(url_for("dashboard"))
        else:
            logging.info(f"FAILED login from IP {request.remote_addr}")
            return render_template("login.html", error="Invalid credentials")

    # GET request → show login page
    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    if "user" in session:
        return render_template("dashboard.html", user=session["user"])

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("user", None)
    logging.info("User logged out")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)