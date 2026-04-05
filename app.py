from flask import Flask, render_template

app = Flask(__name__)

# Data for your buyer (Tracking stats)
stats = {"visits": 0, "clicks": 0}

@app.route('/')
def home():
    stats["visits"] += 1
    # This tells the app to use your 'index.html' file for the design
    return render_template('index.html')

@app.route('/click')
def click
