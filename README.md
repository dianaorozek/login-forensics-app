# Login Forensics App

A cybersecurity forensics project built with Python and Flask that simulates a login system and logs all authentication activity for forensic analysis.

## Overview

This app demonstrates how login events can be monitored and recorded for digital forensics purposes. It captures successful and failed login attempts along with the originating IP address and timestamp.

Built as part of the Digital Forensics course at the Faculty of Computer Science and Engineering, Ss. Cyril and Methodius University, Skopje.

## Features

- Simulated login/logout system using Flask
- Logs every login attempt (success and failure) with IP address and timestamp
- Structured log files for forensic analysis
- Simple dashboard for authenticated users

## Tech Stack

- Python 3
- Flask
- HTML/Jinja2 Templates
- Python logging module

## Installation

git clone https://github.com/dianaorozek/login-forensics-app.git
cd login-forensics-app
pip install flask
python app.py

Then open your browser at http://127.0.0.1:5000

Demo credentials: username: admin, password: password123

## Disclaimer

This app uses intentionally simple credentials and is designed strictly for educational and forensics demonstration purposes. Do not use in production.

## License

MIT
