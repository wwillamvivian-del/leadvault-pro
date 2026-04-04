from flask import Flask, render_template_string

app = Flask(__name__)

# Data for your buyer
stats = {"visits": 0, "clicks": 0}

@app.route('/')
def home():
    stats["visits"] += 1
    return """
    <body style="background:#0d1117; color:white; text-align:center; font-family:sans-serif;">
        <h1 style="color:#58a6ff;">LEADVAULT PRO</h1>
        <p>Verified Executive Contacts</p>
        <div style="background:#161b22; border:1px solid #30363d; padding:20px; border-radius:10px; margin:20px;">
            <h3>James Anderson</h3>
            <p>CEO, TechFlow Solutions</p>
            <p style="color:#58a6ff;">ja***@techflow.com</p>
        </div>
        <a href="/click" style="background:#238636; color:white; padding:15px; text-decoration:none; border-radius:5px; font-weight:bold;">UNLOCK 500+ LEADS ($49)</a>
        <br><br>
        <p style="color:#8b949e; font-size:10px;">User ID: Active</p>
    </body>
    """

@app.route('/click')
def click():
    stats["clicks"] += 1
    return "<h3>Redirecting to Payment...</h3><a href='/'>Go Back</a>"

@app.route('/admin')
def admin():
    return f"""
    <body style="font-family:sans-serif; padding:20px;">
        <h1 style="color:green;">Owner Dashboard</h1>
        <hr>
        <h3>Live Stats for Buyer:</h3>
        <p><b>Total Visitors:</b> {stats['visits']}</p>
        <p><b>Button Clicks:</b> {stats['clicks']}</p>
        <br>
        <a href="/">View Main Site</a>
    </body>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
