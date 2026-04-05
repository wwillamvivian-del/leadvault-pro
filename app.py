from flask import Flask, render_template, request
import csv
import os

app = Flask(__name__)

def get_leads(query=None):
    leads = []
    if not os.path.exists('leads.csv'): return leads
    with open('leads.csv', mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not query or query.lower() in row['Name'].lower() or query.lower() in row['Company'].lower():
                leads.append(row)
    return leads

@app.route('/')
def home():
    search_query = request.args.get('search')
    results = get_leads(search_query)
    return render_template('index.html', leads=results, query=search_query)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000

cat <<EOF > app.py
from flask import Flask, render_template, request
import csv
import os

app = Flask(__name__)

def get_leads(query=None):
    leads = []
    if not os.path.exists('leads.csv'):
        return leads
    with open('leads.csv', mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not query or query.lower() in row['Name'].lower() or query.lower() in row['Company'].lower():
                leads.append(row)
    return leads

@app.route('/')
def home():
    search_query = request.args.get('search')
    results = get_leads(search_query)
    return render_template('index.html', leads=results, query=search_query)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
