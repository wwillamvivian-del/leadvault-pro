# 1. Update the Python app
cat <<EOF > app.py
from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
EOF

# 2. Update the HTML Aurora design
mkdir -p templates
cat <<EOF > templates/index.html
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LeadVault Pro</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body { background: #05070a; color: white; font-family: sans-serif; display: flex; align-items: center; justify-content: center; min-height: 100vh; margin: 0; }
        .card { width: 90%; max-width: 350px; background: rgba(15, 20, 30, 0.9); padding: 30px; border-radius: 30px; border: 1px solid rgba(255,255,255,0.1); backdrop-filter: blur(10px); text-align: center; }
        h1 { background: linear-gradient(to right, #fff, #00d2ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin: 0; font-size: 26px; }
        .btn { display: block; background: linear-gradient(135deg, #3a7bd5, #00d2ff); color: white; padding: 16px; border-radius: 14px; text-decoration: none; font-weight: bold; margin-top: 25px; box-shadow: 0 10px 20px rgba(0,210,255,0.3); }
        .chart-box { width: 200px; margin: 20px auto; }
    </style>
</head>
<body>
    <div class="card">
        <h1>LEADVAULT PRO</h1>
        <p style="color:#667; font-size:12px; letter-spacing:2px;">PREMIUM INTELLIGENCE</p>
        <div class="chart-box"><canvas id="auroraChart"></canvas></div>
        <div style="text-align:left; background:rgba(255,255,255,0.05); padding:15px; border-radius:15px; border-left:4px solid #00ff88;">
            <p style="margin:0; font-size:10px; color:#00ff88;">LEAD IDENTIFIED</p>
            <p style="margin:5px 0; font-weight:bold; font-size:18px;">James Anderson</p>
            <p style="margin:0; font-size:13px; color:#888;">CEO, TechFlow Solutions</p>
        </div>
        <a href="#" class="btn">UNLOCK ALL LEADS ($49)</a>
    </div>
    <script>
        const ctx = document.getElementById('auroraChart').getContext('2d');
        new Chart(ctx, { type: 'doughnut', data: { datasets: [{ data: [65, 35], backgroundColor: ['#00d2ff', 'rgba(255,255,255,0.05)'], borderWidth: 0, borderRadius: 10 }] }, options: { cutout: '85%' } });
    </script>
</body>
</html>
EOF
