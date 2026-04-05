from flask import Flask, render_template, request, redirect, session
import csv
import os

app = Flask(__name__)
app.secret_key = 'wealthvault_premium_secure'

ADMIN_USER = "admin"
ADMIN_PASS = "vault77"

def get_leads():
    leads = []
    if not os.path.exists('leads.csv'):
        with open('leads.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Status', 'Name', 'Title', 'Company'])
    with open('leads.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            leads.append(row)
    return leads

@app.route('/')
def welcome():
    # This shows the flowing welcome screen FIRST
    return render_template('landing.html')

@app.route('/dashboard')
def index():
    if not session.get('logged_in'):
        return redirect('/login')
    return render_template('index.html', leads=get_leads())

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == ADMIN_USER and request.form['password'] == ADMIN_PASS:
            session['logged_in'] = True
            return redirect('/dashboard')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run()
