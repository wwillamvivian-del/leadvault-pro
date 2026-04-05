from flask import Flask, render_template, request, redirect, session
import csv
import os

app = Flask(__name__)
app.secret_key = 'wealthvault_secure_key'

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
def index():
    return render_template('index.html', leads=get_leads())

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == ADMIN_USER and request.form['password'] == ADMIN_PASS:
            session['logged_in'] = True
            return redirect('/admin_portal_77')
    return render_template('login.html')

@app.route('/admin_portal_77', methods=['GET', 'POST'])
def admin():
    if not session.get('logged_in'):
        return redirect('/login')
    if request.method == 'POST':
        with open('leads.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([request.form.get('status'), request.form.get('name'), request.form.get('title'), request.form.get('company')])
        return redirect('/admin_portal_77')
    return render_template('admin.html')

if __name__ == "__main__":
    app.run()
