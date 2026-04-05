from flask import Flask, render_template, request, redirect
import csv
import os

app = Flask(__name__)

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
    query = request.args.get('search', '').lower()
    all_leads = get_leads()
    if query:
        filtered_leads = [l for l in all_leads if query in l['Name'].lower() or query in l['Company'].lower()]
        return render_template('index.html', leads=filtered_leads, query=query)
    return render_template('index.html', leads=all_leads)

@app.route('/admin_portal_77', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        name, title, company = request.form.get('name'), request.form.get('title'), request.form.get('company')
        status = request.form.get('status', 'Verified')
        with open('leads.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([status, name, title, company])
        return redirect('/admin_portal_77')
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body { background: #000; color: #28A745; font-family: sans-serif; padding: 20px; text-align: center; }
            input, select, button { width: 100%; padding: 15px; margin: 10px 0; border-radius: 8px; border: 1px solid #28A745; background: #111; color: white; box-sizing: border-box; }
            button { background: #28A745; color: black; font-weight: bold; cursor: pointer; }
        </style>
    </head>
    <body>
        <h2>ADMIN PORTAL</h2>
        <form method="POST">
            <input type="text" name="name" placeholder="Full Name" required>
            <input type="text" name="title" placeholder="Job Title" required>
            <input type="text" name="company" placeholder="Organization" required>
            <select name="status"><option value="Verified">Verified</option><option value="Pending">Pending</option></select>
            <button type="submit">ADD TO DATABASE</button>
        </form>
        <br><a href="/" style="color: #666; text-decoration: none;">← Back to Site</a>
    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(debug=True)
