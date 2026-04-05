from flask import Flask, render_template, request
import csv
import os

app = Flask(__name__)

@app.route('/')
def home():
    leads = []
    if os.path.exists('leads.csv'):
        with open('leads.csv', mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            leads = list(reader)
    
    query = request.args.get('search', '')
    if query:
        leads = [l for l in leads if query.lower() in str(l).lower()]
        
    return render_template('index.html', leads=leads, query=query)

if __name__ == '__main__':
    # CRITICAL FIX: Render needs the port to be set by the environment
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
