import sqlite3


def dbConnect():
    return sqlite3.connect('main.db')


def ifAdmin():
    # database connection
    return # result


def isAuthenticated(username, password):
    connection = dbConnect()
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM Users WHERE username={username} AND password={password}")
    result = cursor.fetchall()
    connection.close()
    if len(result)>0:
        return True
    return False


def clientRegister():
    # A client visiting to the web application should be able to entry their Name, Address, Phone
    return 


def takeAppointment():
    # A client should be able to entry their Car License number, Car Engine Number, appointment date and can select their desire mechanic
    return 

def isMechanicAvailable():
    # each mechanic is allowed to get assign on maximum 4 active cars(clients) everyday
    # if the mechanic is occupied with maximum no. of appointment the system should notify client otherwise it will approve the appointment.

    return # result

def showAllMechanics():
    # The list of the mechanic should show how many free places are available for each mechanic
    return # result

def ifAppointmentExists():
    # After a client makes data submission, it should check whether the client has already taken any appointment from any mechanic on certain date or not
    # If not, then the client is allowed to take an appointment
    # otherwise s/he will be notifying that he has already taken an appointment on that specific date.
    return

def getClientAppointments(username):
    connection = dbConnect()
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM Appointments WHERE username={username}")
    result = cursor.fetchall()
    connection.close()
    return result


