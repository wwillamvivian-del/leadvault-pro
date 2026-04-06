from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import requests
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'wealthvault_premium'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vault.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(#2026 update: SQLAlchemy 3.0 compatible
        db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    balance = db.Column(db.Float, default=1382920.50)
    last_seen = db.Column(db.DateTime, default=datetime.utcnow) 
    transactions = db.relationship('Transaction', backref='owner', lazy=True)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    type = db.Column(db.String(20), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    # Fixed for SQLAlchemy 2.0+
    return db.session.get(User, int(user_id))

def get_crypto_prices():
    assets = {'BTC': 'btc-usd', 'GRT': 'grt-usd', 'AMP': 'amp-usd', 'COMP': 'comp-usd'}
    prices = {}
    for ticker, pair in assets.items():
        try:
            r = requests.get(f'https://api.coinbase.com/v2/prices/{pair}/spot', timeout=3)
            prices[ticker] = float(r.json()['data']['amount'])
        except:
            fallbacks = {'BTC': 68432.10, 'GRT': 0.48, 'AMP': 0.0072, 'COMP': 82.50}
            prices[ticker] = fallbacks.get(ticker)
    return prices

@app.route('/')
@login_required
def index():
    # --- AUTOMATIC GROWTH LOGIC ---
    now = datetime.utcnow()
    time_diff = (now - current_user.last_seen).total_seconds() / 60
    
    if time_diff > 0.05: # Triggers every 3 seconds for demo speed
        growth = time_diff * 1.50 # Earns $1.50 per minute automatically
        current_user.balance += growth
        current_user.last_seen = now
        db.session.commit()
    # ------------------------------
    
    history = Transaction.query.filter_by(user_id=current_user.id).order_by(Transaction.date.desc()).limit(5).all()
    return render_template('index.html', prices=get_crypto_prices(), history=history)

@app.route('/buy', methods=['POST'])
@login_required
def buy():
    current_user.balance += 1000
    new_tx = Transaction(amount=1000, type='Deposit', user_id=current_user.id)
    db.session.add(new_tx)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and user.password == request.form['password']:
            login_user(user)
            return redirect(url_for('index'))
    return render_template('login.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # Create a fresh admin user since we deleted the old db
        if not User.query.filter_by(username='admin').first():
            admin = User(username='admin', password='password123')
            db.session.add(admin)
            db.session.commit()
    app.run(debug=True, port=5000, host='0.0.0.0')
@app.route('/deposit', methods=['GET', 'POST'])
@login_required
def deposit():
    if request.method == 'POST':
        amount = float(request.form.get('amount', 0))
        current_user.balance += amount
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('deposit.html')

@app.route('/withdraw', methods=['GET', 'POST'])
@login_required
def withdraw():
    if request.method == 'POST':
        amount = float(request.form.get('amount', 0))
        if current_user.balance >= amount:
            current_user.balance -= amount
            db.session.commit()
        return redirect(url_for('index'))
    return render_template('withdraw.html')
