from flask import Flask, render_template
import os

app = Flask(__name__)

stats = {"visits": 0, "clicks": 0}

@app.route('/')
def home():
    stats["visits"] += 1
    return render_template('index.html')

@app.route('/click')
def click():
    stats["clicks"] += 1
    return "<h3>Redirecting to Secure Payment Vault...</h3>"

if __name__ == '__main__':
    # We use port 10000 specifically for Render
    app.run(host='0.0.0.0', port=10000)
