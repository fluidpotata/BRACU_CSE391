from flask import Flask, redirect,render_template,request, session, url_for
from helper import *

app = Flask(__name__)
app.config["SECRET_KEY"] = "any random string"


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if isAuthenticated(username, password):
            session['username'] = username
            response = redirect(url_for('dashboard'))
            response.set_cookie('user_id', username)
            return response
    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', data=getClientAppointments(session['username']))


@app.route('/appointment')
def appointment():
    return render_template('appointment.html')


if __name__ == '__main__':
    app.run(debug=True)