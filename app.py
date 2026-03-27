from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
from datetime import datetime, timedelta

app = Flask(__name__)


app.secret_key = 'blood_bank_secure_key_2026'


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password' 
app.config['MYSQL_DB'] = 'blood_bank'

mysql = MySQL(app)

def is_logged_in():
    return 'username' in session


@app.route('/')
def index():
    """Renders the login page."""
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    """Handles user login and sets session roles."""
    username = request.form['username']
    role = request.form['role']
    session['username'] = username
    session['role'] = role
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    """Directs users to the correct dashboard based on their role."""
    if not is_logged_in():
        return redirect(url_for('index'))
    
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM donors")
    data = cur.fetchall()
    cur.close()

    if session['role'] == 'staff':
        return render_template('staff_dash.html', donors=data)
    else:
        return render_template('hospital_dash.html', donors=data)

@app.route('/add_donor', methods=['POST'])
def add_donor():
    """Allows staff to add a donor and calculates eligibility."""
    if session.get('role') != 'staff':
        return "Unauthorized Access", 403
    
    name = request.form['name']
    blood_group = request.form['blood_group']
    last_date_str = request.form['last_date']
    last_date = datetime.strptime(last_date_str, '%Y-%m-%d')
    next_eligible = last_date + timedelta(days=90)
    
    cur = mysql.connection.cursor()
    cur.execute("""
        INSERT INTO donors (name, blood_group, last_donation_date, next_eligible_date) 
        VALUES (%s, %s, %s, %s)
    """, (name, blood_group, last_date, next_eligible))
    
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('dashboard'))

@app.route('/delete_donor/<int:id>')
def delete_donor(id):
    """Allows staff to delete a donor record."""
    if session.get('role') != 'staff':
        return "Unauthorized Access", 403
    
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM donors WHERE id = %s", (id,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    """Clears the session and logs the user out."""
    session.clear()
    return redirect(url_for('index'))


@app.errorhandler(404)
def page_not_found(e):
    return "This page does not exist. Check your routes!", 404

if __name__ == '__main__':
    app.run(debug=True)