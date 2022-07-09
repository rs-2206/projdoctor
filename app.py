from MySQLdb import Date
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
from datetime import date,datetime
import MySQLdb.cursors
import os

app = Flask(__name__,static_folder="static")
app.secret_key = 'super secret key'

import mysql.connector

connection=mysql.connector.connect(host="localhost",user="root",password="Root@265",database="DMS")
cursor=connection.cursor(buffered=True)

app.config["FILE_UPLOADS"] = "C:/Users/sharv/OneDrive/Desktop/shar/CS208/"
app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024
app.config['DOWNLOAD_FOLDER'] = "C:/Users/sharv/OneDrive/Desktop/shar/CS208/"

@app.route("/")
def homepage():
    return render_template("finalhome.html")

@app.route("/role")
def role():
    return render_template("role.html")

@app.route("/signin")
def signin():
    return render_template("user.html")

@app.route("/logout")
def logout():
    return render_template("finalhome.html")

@app.route("/register1")
def home():
    return render_template("homepage.html")

@app.route("/contactus")
def contact():
    return render_template("contactus.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@app.route("/rhome")
def rhome():
    return render_template("rhomepage.html")

@app.route("/rcontactus")
def rcontact():
    return render_template("rcontactus.html")

@app.route("/raboutus")
def raboutus():
    return render_template("raboutus.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/covid")
def covid():
    return render_template("covid.html")

@app.route("/food")
def food():
    return render_template("food.html")

@app.route("/hygiene")
def hygiene():
    return render_template("hygiene.html")

@app.route("/medicalassistance")
def massistance():
    return render_template("medical.assistance.html")

@app.route("/technology")
def tech():
    return render_template("technology.html")

@app.route("/startups")
def startup():
    return render_template("startups.html")

@app.route("/login",methods=["POST","GET"])
def login():
    role = request.form["role"]
    session["role"] = role
    if role == "Patient":
        return render_template("user.html")
    else:
        return render_template("receplogin.html")
    
@app.route("/login2", methods=["POST","GET"])
def login2():
    email = request.form["email"]
    password = request.form["password"]
    session["email"] = email
    cursor.execute("SELECT * from patient where Email='{}' and Password='{}'".format(email,password))
    a = cursor.fetchall()
    if(len(a) > 0):
        return render_template("homepage.html")
    else:
        return render_template("user.html")

@app.route("/rlogin", methods=["POST","GET"])
def rlogin2():
    Email = request.form["email"]
    password = request.form["password"]
    session["Email"] = Email
    cursor.execute("SELECT * from Receptionist where Email='{}' and Password='{}'".format(Email,password))
    a = cursor.fetchall()
    if(len(a) > 0):
        return render_template("rhomepage.html")
    else:
        return render_template("receplogin.html")

@app.route("/register")
def register():
    role=session.get("role",None)
    id = session.get("email",None)
    print(id)
    if(role == "Patient"):
        return render_template("registration.html")
    else:
        return render_template("recepregis.html")

@app.route('/recepregis',methods=['GET','POST'])
def index():
    if request.method=='POST':
        userdetails=request.form
        hospitalname=userdetails['hospitalname']
        email=userdetails['email']
        password=userdetails['inputpassword']
        confirm=userdetails['confirmpassword']
        cursor.execute("SELECT Email FROM Receptionist WHERE Email='{}'".format(email))
        validate=cursor.fetchall()
        if password!=confirm:
            return render_template('password.html')
        if len(validate)==0:
         cursor.execute("""INSERT INTO Receptionist(Email,Password,HospitalName) VALUES('{}','{}','{}')""".format(email,password,hospitalname))
         connection.commit()
        else :
            return render_template('finalhome.html')
        return render_template('receplogin.html')
    return render_template('recepregis.html')

@app.route("/register2",methods=["POST","GET"])
def register2():
    fname=request.form["fname"]
    lname=request.form["lname"]
    email=request.form["email"]
    password=request.form["password"]
    cpassword=request.form['cpassword']
    mobileno=request.form["mobileno"]
    gender=request.form["gender"]
    bgroup=request.form["bgroup"]
    dob=request.form["dob"]
    address=request.form["address"]
    address1=request.form["address1"]
    city=request.form["city"]
    state=request.form["state"]
    pcode=request.form["pcode"]
    cursor.execute("SELECT Email FROM patient WHERE Email='{}'".format(email))
    validate=cursor.fetchall()
    if len(validate)<=0:
        if password == cpassword:
            cursor.execute("""INSERT INTO patient(Email, Firstname, Lastname, Password, cpassword, DOB, Gender, Bloodgroup, mobilenumber, Address, Address1, State, Pincode, City) values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')""".format(email,fname,lname,password,cpassword,dob,gender,bgroup,mobileno,address,address1,state,pcode,city))
            connection.commit()
            return render_template('user.html')
        else:
            return render_template('registration.html',validpassword="(Passwords didn't match)")  
    if len(validate)>0:
        return render_template('registration.html',validuserid="(User Id already present)")  

@app.route("/search")
def search():
    return render_template("departments.html")

@app.route("/appointments")
def appointments():
    mailid = session.get("email",None)
    t = date.today()
    cursor.execute("SELECT * FROM Appointments WHERE id = '{}'".format(mailid))
    appointments = cursor.fetchall()
    for i in appointments:
        k = i[4]
        if k > t:
            Status = "Not Completed"
        elif k <= t:
            Status = "Completed"
        cursor.execute("UPDATE Appointments SET Status = '{}' WHERE id='{}' and Hid='{}' and Did='{}' and Date='{}'".format(Status,mailid,i[1],i[2],i[4]))
        connection.commit()
    print(appointments)
    k = len(appointments)
    return render_template("appointments.html", c = appointments, k = k,a=mailid)

@app.route("/pastappointments")
def pastappointments():
    mailid = session.get("email",None)
    cursor.execute("SELECT * FROM Appointments WHERE id = '{}'".format(mailid))
    appointments = cursor.fetchall()
    print(appointments)
    k = len(appointments)
    return render_template("pastappointments.html", c = appointments, k = k,a=mailid)

@app.route("/rappointments")
def rappointments():
    hid = session.get("Email",str)
    print(hid)
    cursor.execute("SELECT * FROM Appointments JOIN insurance where Appointments.Hid='{}' and Appointments.id=insurance.Pid".format(hid))
    appointments = cursor.fetchall()
    print(appointments)
    k = len(appointments)
    return render_template("rappointments.html", c = appointments, k = k,a=hid)

@app.route("/rpastappointments")
def rpastappointments():
    mailid = session.get("Email",None)
    cursor.execute("SELECT * FROM Appointments JOIN insurance where Appointments.Hid='{}' and Appointments.id=insurance.Pid".format(mailid))
    appointments = cursor.fetchall()
    print(appointments)
    k = len(appointments)
    return render_template("rpastappointments.html", c = appointments, k = k,a=mailid)

@app.route("/doctors/<spec>",methods=['GET', 'POST'])
def doctors(spec):
    print(spec)
    session['specialisation'] = spec
    cursor.execute("SELECT * FROM Doctor WHERE Specialisation='{}'".format(spec))
    doctors=cursor.fetchall()
    k = len(doctors)
    print(doctors)
    return  render_template('doctors.html',c = doctors)

@app.route("/makingappointment/<did>",methods = ["POST","GET"])
def makingappointment(did):
    cursor.execute("SELECT * FROM Doctor WHERE Email='{}'".format(did))
    doctor=cursor.fetchall()
    print(doctor)
    hid = doctor[0][1]
    cursor.execute("SELECT * FROM slots WHERE Did='{}' and Hid='{}'".format(did,hid))
    slots = cursor.fetchall()
    print(slots)
    t = date.today()
    k = []
    for i in slots:
        if(i[2] >= t):
            k.append(i)
    print(k)
    p = len(k)
    return render_template("makingappointments.html",c = doctor,slots = k,p=p)

@app.route("/doctors/makingappointment/<did>",methods = ["POST","GET"])
def makeappointment(did):
    cursor.execute("SELECT * FROM Doctor WHERE Email='{}'".format(did))
    doctor=cursor.fetchall()
    print(doctor)
    hid = doctor[0][1]
    cursor.execute("SELECT * FROM slots WHERE Did='{}' and Hid='{}'".format(did,hid))
    slots = cursor.fetchall()
    print(slots)
    t = date.today()
    k = []
    for i in slots:
        if(i[2] >= t):
            k.append(i)
    print(k)
    p = len(k)
    return render_template("makingappointments.html",c = doctor,slots = k,p=p)

@app.route("/reason/<did>/<date>",methods=['GET','POST'])
def reason(did,date):
    return render_template("reason.html", i=did,date = date)

@app.route("/book/<did>/<d>",methods=['GET', 'POST'])
def book(did,d):
    reason = request.form['reason']
    session["reason"] = reason
    id1=session.get("email",None)
    print(id1)
    cursor.execute("SELECT * FROM Patient WHERE Email='{}'".format(id1))
    p = cursor.fetchall()
    print(p)
    cursor.execute("SELECT * FROM Doctor WHERE Email='{}'".format(did))
    q = cursor.fetchall()
    print(q)
    Hid = q[0][1]
    t = datetime.today()
    k = datetime.strptime(d, "%Y-%m-%d")
    cursor.execute("SELECT * FROM slots WHERE Did='{}' and Hid='{}' and Date='{}'".format(did,Hid,d))
    r = cursor.fetchall()
    print(r)
    print(k)
    print(t)
    if k > t:
        Status = "Not Completed"
    elif k < t:
        Status = "Completed"
    cursor.execute("""INSERT INTO Appointments(id, Did, Hid, Reason, Date, Status) values('{}','{}','{}','{}','{}','{}')""".format(id1,did,Hid,reason,d,Status))
    cursor.execute("UPDATE slots SET AvailableSlots = '{}' WHERE Did='{}' and Hid='{}' and Date='{}'".format(r[0][3]-1,did,Hid,d))
    connection.commit()
    return render_template("confirmation.html",p = p,q=q,r=r)

@app.route('/cancel/<did>/<reason>/<d>',methods=['GET','POST'])
def cancel(did,reason,d):
    pid = session.get("email",None)
    cursor.execute("SELECT * FROM Doctor WHERE Email='{}'".format(did))
    q = cursor.fetchall()
    print(q)
    Hid = q[0][1]
    cursor.execute("SELECT * FROM slots WHERE Did='{}' and Hid='{}'".format(did,Hid))
    r = cursor.fetchall()
    cursor.execute("UPDATE slots SET AvailableSlots = '{}' WHERE Did='{}' and Hid='{}' and Date='{}'".format(r[0][3]+1,did,Hid,d))
    connection.commit()
    cursor.execute("DELETE FROM Appointments WHERE Reason='{}' and Did='{}' and Hid='{}' and Date='{}'".format(reason,did,Hid,d))
    connection.commit()
    cursor.execute("SELECT * FROM Appointments WHERE id = '{}'".format(pid))
    appointments = cursor.fetchall()
    k = len(appointments)
    return render_template("cancellation.html",c=appointments,k = k,a=pid)

@app.route('/insurance',methods=['GET','POST'])
def insurance():    
     mail=session.get('email',str)
     cursor.execute("SELECT * FROM insurance WHERE Pid='{}'".format(mail))
     validate=cursor.fetchall()
     if len(validate)==0 :
       if request.method=='POST':
        user=request.form
        email=user['email']
        insuranceholder=user['insuranceholder']
        expirydate=user['expirydate']
        benefits=user['benefitscontact']
        insurancenumber=user['insurancenumber']
        cursor.execute("""INSERT INTO Insurance(Pid,InsuranceNumber,HolderName,insuranceExpiryDate,Benefitscontact) VALUES('{}','{}','{}','{}','{}')""".format(email,insurancenumber,insuranceholder, expirydate, benefits))
        connection.commit()
        return render_template('homepage.html')
       return render_template('insurance.html')
     cursor.execute("select*from Insurance where Pid='{}'".format(mail))
     validate=cursor.fetchall()
     return render_template('postinsurance.html',mail=validate[0][0],insurance=validate[0][1],HolderName=validate[0][2],date=validate[0][3],benefit=validate[0][4])

@app.route("/doctors/makingappointment/favourites/<did>",methods=['GET','POST'])
def favourites(did):
    pid = session.get("email",None)
    print(pid)
    cursor.execute("SELECT * FROM Doctor WHERE Email='{}'".format(did))
    a = cursor.fetchall()
    cursor.execute("SELECT * FROM FavouriteDoctors WHERE Did='{}' and id='{}'".format(did,pid))
    validate = cursor.fetchall()
    print(validate)
    if(len(validate) <= 0):
        cursor.execute("INSERT INTO FavouriteDoctors(id,Did) VALUES('{}','{}')".format(pid,did))
        connection.commit()
    return redirect("/register1")

@app.route("/favourites")
def show():
    c = []
    id = session.get("email",None)
    cursor.execute("SELECT * FROM FavouriteDoctors WHERE id='{}'".format(id))
    a = cursor.fetchall()
    print(a)
    for i in a:
        print(i)
        cursor.execute("SELECT * FROM Doctor WHERE Email='{}'".format(i[1]))
        k = cursor.fetchall()
        print(k)
        c.append(k)
    return render_template("favourites.html",c = c)

@app.route("/release")
def release():
    return render_template("releaseslots.html")

@app.route("/releaseslots",methods=['POST','GET'])
def releaseslots():
    msg = ""
    hid = request.form['hid']
    did = request.form['did']
    date = request.form['date']
    slots = request.form['slots']
    cursor.execute("INSERT INTO slots(Hid,Did,Date,AvailableSlots) VALUES('{}','{}','{}','{}')".format(hid,did,date,slots))
    connection.commit()
    return render_template("releaseslots.html",msg = "Released Successfully")

@app.route("/add")
def add():
    return render_template("adddoctors.html")

@app.route('/adddoctors',methods=['POST','GET'])
def adddoctors():
    if request.method=='POST':
        doctor=request.form
        mail=session.get('Email',str())
        email=doctor['email']
        name=doctor['name']
        specialisation=doctor['specialisation']
        regno=doctor['regno']
        experience=doctor['experience']
        laknown=doctor['laknown'] 
        cursor.execute("select * from Doctor where Email='{}'".format(email)) 
        validate=cursor.fetchall()
        if len(validate)>0:
            return render_template('doctoralreadyexist.html')
        else:
            cursor.execute("""INSERT INTO Doctor(Hid,Email,Name,Specialisation,RegistrationNo,Experience,TotalRating,Languageknown) VALUES('{}','{}','{}','{}','{}','{}','{}','{}')""".format(mail,email,name,specialisation, regno, experience,0,laknown))
            connection.commit()
        return render_template('rhomepage.html')
    return render_template('adddoctors.html')

@app.route("/edit")
def edit():
    email = session.get("email",str)
    cursor.execute("SELECT * FROM Patient WHERE Email='{}'".format(email))
    p = cursor.fetchall()
    return render_template("editprofile.html",p=p)

@app.route("/editprofile",methods=['POST','GET'])
def editprofile():
    email = session.get("email",str)
    fname=request.form["fname"]
    lname=request.form["lname"]
    mobileno=request.form["mobileno"]
    gender=request.form["gender"]
    bgroup=request.form["bgroup"]
    dob=request.form["dob"]
    address=request.form["address"]
    address1=request.form["address1"]
    city=request.form["city"]
    state=request.form["state"]
    pcode=request.form["pcode"]
    cursor.execute("""UPDATE patient SET Firstname='{}', Lastname='{}', DOB='{}', Gender='{}', Bloodgroup='{}', mobilenumber='{}', Address='{}', Address1='{}', State='{}', Pincode='{}', City='{}' WHERE Email='{}'""".format(fname,lname,dob,gender,bgroup,mobileno,address,address1,state,pcode,city,email))
    connection.commit()
    return render_template('homepage.html') 

uploaded_file=[]

@app.route("/present")
def present():
    return render_template("presentrecords.html")

@app.route('/past', methods=['GET', 'POST'])
def upload_file():
    print(uploaded_file)
    if request.method == "POST":
        if request.files:
            file = request.files.getlist("files")
            for i in file:
                i.save(os.path.join(app.config["FILE_UPLOADS"], i.filename))
                uploaded_file.append(i.filename)
            print(uploaded_file)
            return render_template("past.html", uploaded_file=uploaded_file)
            process_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), filename)
            return redirect(url_for('uploaded_file',filename=file.filename))
    return render_template("presentrecords.html")

@app.route('/uploads/<filename>')
def send_uploaded_file(filename):
    from flask import send_from_directory
    return send_from_directory(app.config['FILE_UPLOADS'], filename)

@app.route("/rpa/<id>/<did>/<date>")
def rpa(id,did,date):
    mailid = session.get("Email",str)
    cursor.execute("UPDATE Appointments SET Status = '{}' WHERE id='{}' and Hid='{}' and Did='{}' and Date='{}'".format("Not Showed",id,mailid,did,date))
    connection.commit()
    cursor.execute("SELECT * FROM Appointments JOIN insurance where Appointments.Hid='{}' and Appointments.id = '{}'and Appointments.Did = '{}' and Appointments.id=insurance.Pid".format(mailid,id,did))
    appointments = cursor.fetchall()
    print(appointments)
    k = len(appointments)
    return render_template("rpa.html", c = appointments, k = k,a=mailid)

if __name__ == "__main__":
    app.run(debug=True)
