from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/click')
def click():
    return "<h3>Redirecting to Secure Payment Vault...</h3>"

if __name__ == '__main__':
    # Use port 10000 for Render
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
