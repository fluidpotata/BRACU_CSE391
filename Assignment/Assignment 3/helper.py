import sqlite3


def dbConnect():
    return sqlite3.connect('main.db')


def ifAdmin(username):
    connection = dbConnect()
    cursor = connection.cursor()
    cursor.execute(f"SELECT role FROM Users WHERE username='{username}'")
    result = cursor.fetchall()
    connection.close()
    return result[0][0] == 'Admin'


def isAuthenticated(username, password):
    connection = dbConnect()
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM Users WHERE username='{username}' AND password='{password}'")
    result = cursor.fetchall()
    connection.close()
    if len(result)>0:
        return True
    return False


def clientRegister(name, address, phone, username, password):
    # A client visiting to the web application should be able to entry their Name, Address, Phone
    connection = dbConnect()
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO Users(name, address, phone, username, password) VALUES('{name}', '{address}', '{phone}', '{username}', '{password}')")
    connection.commit()
    connection.close()
    return 


def takeAppointment(username, carLicenseNumber, carEngineNumber, carAppointmentDate, mechanic):
    # A client should be able to entry their Car License number, Car Engine Number, appointment date and can select their desire mechanic
    connection = dbConnect()
    cursor = connection.cursor()
    cursor.execute(f"SELECT id from Users where username='{username}'")
    userid = cursor.fetchall()[0][0]
    cursor.execute(f"INSERT INTO Appointments(carLicenseNumber, carEngineNumber, carAppointmentDate, mechanicID, userID) VALUES('{carLicenseNumber}', '{carEngineNumber}', '{carAppointmentDate}', '{mechanic}', '{userid}')")
    connection.commit()
    connection.close()
    return

def isMechanicAvailable(carAppointmentDate, mechanic):
    # each mechanic is allowed to get assign on maximum 4 active cars(clients) everyday
    # if the mechanic is occupied with maximum no. of appointment the system should notify client otherwise it will approve the appointment.
    connection = dbConnect()
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM Appointments WHERE carAppointmentDate='{carAppointmentDate}' AND mechanicID='{mechanic}'")
    result = cursor.fetchall()
    connection.close()
    if len(result)<4:
        return True
    return False

def showAllMechanics(date):
    # The list of the mechanic should show how many free places are available for each mechanic
    connection = dbConnect()
    cursor = connection.cursor()
    cursor.execute(f"""
        SELECT m.*, COUNT(a.id) as appointments_today
        FROM mechanic m
        LEFT JOIN Appointments a ON m.id = a.mechanicID AND DATE(a.carAppointmentDate) = DATE('{date}')
        GROUP BY m.id
    """)
    result = cursor.fetchall()
    connection.close()
    return result

def ifAppointmentExists(carLicenseNumber, carEngineNumber, carAppointmentDate, mechanic=None):
    # After a client makes data submission, it should check whether the client has already taken any appointment from any mechanic on certain date or not
    # If not, then the client is allowed to take an appointment
    # otherwise s/he will be notifying that he has already taken an appointment on that specific date.
    connection = dbConnect()
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM Appointments WHERE (carLicenseNumber='{carLicenseNumber}' OR carEngineNumber='{carEngineNumber}') AND carAppointmentDate='{carAppointmentDate}'")
    result = cursor.fetchall()
    connection.close()
    if len(result)>0:
        return True
    return False

def getClientAppointments():
    connection = dbConnect()
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM Appointments")
    result = cursor.fetchall()
    connection.close()
    return result


def ifUserExists(username):
    connection = dbConnect()
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM Users WHERE username='{username}'")
    result = cursor.fetchall()
    connection.close()
    if len(result)>0:
        return True
    return False


def getClientName(userid):
    connection = dbConnect()
    cursor = connection.cursor()
    cursor.execute(f"SELECT name FROM Users WHERE id='{userid}'")
    result = cursor.fetchall()
    connection.close()
    return result[0][0]


def getMechanicName(mechaID):
    connection = dbConnect()
    cursor = connection.cursor()
    cursor.execute(f"SELECT first_name, last_name FROM mechanic WHERE id='{mechaID}'")
    result = cursor.fetchall()
    connection.close()
    return result[0][0]+" "+result[0][1]

def updateAppointment(oldLicense, oldEngine, newDate, newMechanic):
    connection = dbConnect()
    cursor = connection.cursor()
    cursor.execute(f"""
        UPDATE Appointments 
        SET carAppointmentDate = '{newDate}', mechanicID = '{newMechanic}'
        WHERE carLicenseNumber = '{oldLicense}' AND carEngineNumber = '{oldEngine}'
    """)
    connection.commit()
    connection.close()
    return True