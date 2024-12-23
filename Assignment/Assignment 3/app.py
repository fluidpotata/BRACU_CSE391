from flask import Flask, redirect,render_template,request, session, url_for
from helper import *
from datetime import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = "any random string"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if isAuthenticated(username, password):
            session['username'] = username
            if ifAdmin(username):
                return redirect(url_for('admin'))
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Invalid username or password")
    elif request.method == 'GET':
        try:
            if session['username']:
                if ifAdmin(session['username']):
                    return redirect(url_for('admin'))
                return redirect(url_for('dashboard'))
        except:
            return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        if 'username' in session:
            if ifAdmin(session['username']):
                return redirect(url_for('admin'))
            return redirect(url_for('dashboard'))
        else:
            return render_template('signup.html')
    elif request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        address = request.form['address']
        phone = request.form['phone']
        password = request.form['password']
        cpassword = request.form['confirm_password']
        if password != cpassword:
            return render_template('signup.html', error="Password doesn't match")   
        if ifUserExists(username):
            return render_template('signup.html', error="Username taken! Try another username.")
        clientRegister(name, address, phone, username, password)
        return redirect(url_for('login'))



@app.route('/admin')
def admin():
    tdata = getClientAppointments()
    data = []
    for i in tdata:
        data.append((getClientName(i[1]), getMechanicName(i[2]), i[3], i[4], i[5], i[0], getClientPhone(i[1])))
    mechanics = showAllMechanics(datetime.now().strftime('%Y-%m-%d'))
    return render_template('admin.html', data=data, mechanics=mechanics)


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        data = {}
        data['carEngineNumber'] = request.form['carEngineNumber']
        data['carLicenseNumber'] = request.form['carLicenseNumber']
        data['carAppointmentDate'] = request.form['carAppointmentDate']
        if ifAppointmentExists(data['carLicenseNumber'], data['carEngineNumber'], data['carAppointmentDate']):
            return render_template('dashboard.html', error="You have already taken an appointment")
        # return render_template('appointment.html', carLicenseNumber=carLicenseNumber, carEngineNumber=carEngineNumber, carAppointmentDate=carAppointmentDate)
        session['mechanic'] = data
        return redirect(url_for('appointment'))
    elif request.method == 'GET':
        if 'flash' not in session:
            flash = None
        else:
            flash = session['flash']
            session.pop('flash')
        try:
            if session['username']:
                if ifAdmin(session['username']):
                    return redirect(url_for('admin'))
                return render_template('dashboard.html', flash=flash)
        except:
            return redirect(url_for('login'))



@app.route('/appointment', methods=['GET', 'POST'])
def appointment():
    if request.method == 'POST':
        appdata = session['mechanic']   
        carLicenseNumber, carEngineNumber, carAppointmentDate = appdata['carLicenseNumber'], appdata['carEngineNumber'], appdata['carAppointmentDate']
        mechanic = request.form['mechanic']
        if ifAppointmentExists(carLicenseNumber, carEngineNumber, carAppointmentDate, mechanic):
            return render_template('appointment.html', error="You have already taken an appointment")
        if isMechanicAvailable(carAppointmentDate, mechanic):
            takeAppointment(session['username'], carLicenseNumber, carEngineNumber, carAppointmentDate, mechanic)
            session['flash'] = 'Appointment Success'
            return redirect(url_for('dashboard'))
        else:
            return render_template('appointment.html', error="Mechanic is not available")
    elif request.method == 'GET':
        try:
            if session['username']:
                if ifAdmin(session['username']):
                    return redirect(url_for('admin'))
                data = session.get('mechanic')
                date = data['carAppointmentDate']
                mech = showAllMechanics(date)
                return render_template('appointment.html', mechanics=mech)
        except:
            return redirect(url_for('login'))

@app.route('/update_appointment', methods=['POST'])
def update_appointment():
    if 'username' not in session or not ifAdmin(session['username']):
        return redirect(url_for('login'))
        
    appointmentID = request.form['appointmentID']
    newDate = request.form['newDate']
    newMechanic = request.form['newMechanic']
    
    if not isMechanicAvailable(newDate, newMechanic):
        return "Mechanic not available", 400
        
    updateAppointment(appointmentID, newDate, newMechanic)
    return redirect(url_for('admin'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')