from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, flash, url_for, redirect, render_template, make_response
from flask_migrate import Migrate
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:1234@localhost/Perfume Database'
app.config['SQLALCHEMY_ECHO'] = False
db = SQLAlchemy(app)

class Customer(db.Model):
    __tablename__ = 'customer'
    cus_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cus_sex=db.Column(db.Boolean)
    cus_email=db.Column(db.String(80), unique=True)
    cus_name = db.Column(db.String(80))
    cus_surname = db.Column(db.String(80))
    cus_Birthdate = db.Column(db.DateTime)
    cus_telNo=db.Column(db.String)
    cus_totalOrder=db.Column(db.Integer)

    def __init__(self, cus_sex, cus_email, cus_name, cus_surname, cus_Birthdate, cus_telNo, cus_totalOrder):
        self.cus_sex = cus_sex
        self.cus_email = cus_email
        self.cus_name = cus_name
        self.cus_surname = cus_surname
        self.cus_Birthdate = cus_Birthdate
        self.cus_telNo = cus_telNo
        self.cus_totalOrder = cus_totalOrder

class EmployeeLogin(db.Model):
    employeeID = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __init__(self, customerID, username, password):
        self.customerID = customerID
        self.username = username
        self.password = password

class CustomerLogin(db.Model):
    customerID=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String,unique=True)
    password=db.Column(db.String)

    def __init__(self, customerID, username, password):
        self.customerID = customerID
        self.username = username
        self.password = password

class AdminLogin(db.Model):
    adminId=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String,unique=True)
    password=db.Column(db.String)

    def __init__(self, adminId, username, password):
        self.adminId = adminId
        self.username = username
        self.password = password

class Order(db.Model):
    __tablename__ = 'Order'
    order_no = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id=db.Column(db.Integer, db.ForeignKey('customer.cus_id'))
    carrier_id = db.Column(db.Integer,db.ForeignKey('Employee.memberID'))

orderDate = db.Table('orderDate',
                           db.Column('order_no',db.Integer,db.ForeignKey('Order.order_no')),
                           db.Column('order_date',db.DateTime))


class Made_by(db.Model):
    __tablename__ = 'Made_by'
    madebyID = db.Column(db.Integer, db.ForeignKey('Employee.memberID'),primary_key=True)
    perfumeID=db.Column(db.Integer,db.ForeignKey('Perfume.ProductID'),primary_key=True)

class Content(db.Model):
    __tablename__ = 'Content'
    contentId = db.Column(db.Integer, primary_key=True)
    perfumeID=db.Column(db.Integer,db.ForeignKey('Perfume.ProductID'))

class Takes(db.Model):
    __tablename__ = 'Takes'
    matId = db.Column(db.Integer,db.ForeignKey('Material.mat_id'),primary_key=True)
    memberId=db.Column(db.Integer,db.ForeignKey('Employee.memberID'),primary_key=True)
    quantity=db.Column(db.Integer)
    cost=db.Column(db.Integer)

takesFirm=db.Table('takesFirm',
                   db.Column('matId',db.Integer,db.ForeignKey('Material.mat_id',primary_key=True)),
                    db.Column('memberId',db.Integer,db.ForeignKey('Employee.memberID'),primary_key=True),
                    db.Column('firm_name',db.Integer))

class Vehicle(db.Model):
    __tablename__ = 'Vehicle'
    c_id = db.Column(db.Integer,db.ForeignKey('Company.C_id'))
    vehicle_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    package=db.Column(db.Integer) #the number of products which are carried

vehicleFeatures=db.Table('vehicleFeatures',
                         db.Column('vehicle_id',db.Integer,primary_key=True,autoincrement=True),
                         db.Column('licence',db.String(40)),
                         db.Column('kilometer',db.Integer),
                         db.Column('first_price',db.Integer),
                         db.Column('last_price',db.Integer),
                         db.Column('vehicle_type',db.String))

class Perfume(db.Model):
    __tablename__ = 'Perfume'
    Category = db.Column(db.String(20))
    ProductID=db.Column(db.Integer,primary_key=True,autoincrement=True)
    Content=db.Column(db.String(40))
    Price=db.Column(db.Integer)
    Duration = db.Column(db.Integer)
    NumberOfStock= db.Column(db.Integer)


madePerfume=db.Table('madePerfume',
                     db.Column('ProductId',db.Integer,primary_key=True,autoincrement=True),
                     db.Column('made_by',db.Integer,db.ForeignKey('Employee.memberID')))

class Department(db.Model):
    __tablename__ = 'Department'
    dep_address = db.Column(db.String(20))
    dep_TelNo=db.Column(db.String(40))
    dep_name=db.Column(db.String(40))
    department_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    salary = db.Column(db.Integer)
    c_id= db.Column(db.Integer,db.ForeignKey('Company.C_id'))

class Confirms(db.Model):
    __tablename__ = 'Confirms'
    ProductID = db.Column(db.Integer, db.ForeignKey('Perfume.ProductID'),primary_key=True)
    memberID = db.Column(db.Integer, db.ForeignKey('Employee.memberID'),primary_key=True)
    verification_no = db.Column(db.Integer)

class Packages(db.Model):
    __tablename__ = 'Packages'
    packageID = db.Column(db.Integer, primary_key = True,autoincrement=True)
    ProductID = db.Column(db.Integer, db.ForeignKey('Perfume.ProductID'))
    memberID = db.Column(db.Integer, db.ForeignKey('Employee.memberID'))

productFeature=db.Table('productFeature',
                        db.Column('packageID',db.Integer,primary_key=True,autoincrement=True),
                        db.Column('ProductId',db.Integer,db.ForeignKey('Perfume.ProductID')),
                        db.Column('Expiration_Date',db.DateTime),
                        db.Column('production_Date',db.DateTime))

class ConsistOf(db.Model):
    __tablename__ = 'ConsistOf'
    product_id = db.Column(db.Integer, db.ForeignKey('Perfume.ProductID'),primary_key=True)
    mat_id = db.Column(db.Integer, db.ForeignKey('Material.mat_id'),primary_key=True)

class Includes(db.Model):
    __tablename__ = 'Includes'
    order_no = db.Column(db.Integer, db.ForeignKey('Order.order_no'),primary_key=True)
    ProductId = db.Column(db.Integer, db.ForeignKey('Perfume.ProductID'),primary_key=True)

productQuantity=db.Table('productQuantity',
                         db.Column('order_no',db.Integer,db.ForeignKey('Order.order_no'),primary_key=True),
                         db.Column('quantity',db.Integer))

class Company(db.Model):
    __tablename__ = 'Company'
    C_id = db.Column(db.Integer, primary_key = True,autoincrement=True)
    Name = db.Column(db.String(80))
    Budget = db.Column(db.Integer)
    Address = db.Column(db.String(200))
    TelNo = db.Column(db.String(11))

class Manages(db.Model):
    __tablename__ = 'Manages'
    C_id = db.Column(db.Integer, db.ForeignKey('Company.C_id'),primary_key=True)
    memberID = db.Column(db.Integer, db.ForeignKey('Employee.memberID'),primary_key=True)

class Produces(db.Model):
    __tablename__ = 'Produces'
    chemist_id = db.Column(db.Integer, db.ForeignKey('Employee.memberID'),primary_key=True)
    ProductID = db.Column(db.Integer, db.ForeignKey('Perfume.ProductID'),primary_key=True)

class Material(db.Model):
    __tablename__ = 'Material'
    mat_id = db.Column(db.Integer, primary_key = True,autoincrement=True)
    mat_name = db.Column(db.String(80))
    mat_region = db.Column(db.String(80))
    mat_stock = db.Column(db.Integer)
    mat_price = db.Column(db.Integer)

class Employee(db.Model):
    __tablename__ = 'Employee'
    memberID = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(30))
    surname = db.Column(db.String(30))
    address = db.Column(db.String(200))
    telNo = db.Column(db.String(11))
    Birthdate = db.Column(db.DateTime)
    startDate = db.Column(db.DateTime)
    salary = db.Column(db.Integer)
    email = db.Column(db.String(80))
    Department = db.Column(db.String(80))

    def __init__(self, name, surname, address, telNo, Birthdate, startDate, salary, email, Department):
        self.name = name
        self.surname = surname
        self.address = address
        self.telNo = telNo
        self.Birthdate = Birthdate
        self.startDate = startDate
        self.salary = salary
        self.email = email
        self.Department = Department

employeesOfCompany=db.Table('employessOfCompany',
                            db.Column('memberId',db.Integer,db.ForeignKey('Employee.memberID'),primary_key=True),
                            db.Column('Company_id',db.Integer, db.ForeignKey('Company.C_id'),primary_key=True))

class Carrier(db.Model):
    __tablename__ = 'Carrier'
    vehicle_id = db.Column(db.Integer, db.ForeignKey('Vehicle.vehicle_id'),primary_key=True)
    memberID= db.Column(db.Integer,db.ForeignKey('Employee.memberID'),primary_key=True)

memberLicenceType=db.Table('memberLicenceType',
                      db.Column('memberID',db.Integer,db.ForeignKey('Employee.memberID'),primary_key=True),
                      db.Column('drivingLicenceType',db.String(20)))

class Sells(db.Model):
    __tablename__ = 'Sells'
    ProductID = db.Column(db.Integer, db.ForeignKey('Perfume.ProductID'),primary_key=True)
    C_id= db.Column(db.Integer,db.ForeignKey('Company.C_id'),primary_key=True)

class Admin(db.Model):
    __tablename__ = 'Admin'
    memberID = db.Column(db.Integer, db.ForeignKey('Employee.memberID'),primary_key=True)
    C_id = db.Column(db.Integer, db.ForeignKey('Company.C_id'))

class Analyst(db.Model):
    __tablename__ = 'Analyst'
    memberID = db.Column(db.Integer, db.ForeignKey('Employee.memberID'),primary_key=True)
    method=db.Column(db.String(40))

class Customer_Service(db.Model):
    __tablename__ = 'Customer_Service'
    memberID = db.Column(db.Integer, db.ForeignKey('Employee.memberID'),primary_key=True)

class Supplier(db.Model):
    __tablename__ = 'Supplier'
    memberID = db.Column(db.Integer, db.ForeignKey('Employee.memberID'),primary_key=True)

class Accountant(db.Model):
    __tablename__ = 'Accountant'
    memberID = db.Column(db.Integer, db.ForeignKey('Employee.memberID'),primary_key=True)

class Worker(db.Model):
    __tablename__ = 'Worker'
    memberID = db.Column(db.Integer, db.ForeignKey('Employee.memberID'),primary_key=True)

class Chemist(db.Model):
    __tablename__ = 'Chemist'
    memberID = db.Column(db.Integer, db.ForeignKey('Employee.memberID'),primary_key=True)

#---------------------------------FUNCTIONS---------------------------------

@app.route('/')
def opening():
    print('opening')
    return render_template('home.html')

@app.route('/register_page', methods=['GET', 'POST'])
def register_page():
    return render_template('register.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if False:
            return render_template('register.html')

        else:
            email = request.form.get('email')
            username = request.form.get('username')

            email_exist = Customer.query.filter_by(cus_email=email).first()  # if this returns a user, then the email already exists in database
            username_exist = CustomerLogin.query.filter_by(username=username).first()  # if this returns a user, then the username already exists in database

            if email_exist or username_exist:  # if a user is found, we want to redirect back to signup page so user can try again
                if email_exist:
                    flash('This email belongs to another account')
                    return render_template('customer_login.html')
                else:
                    flash('This username belongs to another account')
                    return render_template('customer_login.html')

            else:
                if request.form.get('gender') == "male":
                    cus_sex = False
                else:
                    cus_sex = True
                cus_email = request.form.get('email')
                cus_name = request.form.get('name')
                cus_surname = request.form.get('surname')
                cus_Birthdate = request.form.get('birthdate')
                cus_telNo = request.form.get('telno')
                username = request.form.get('username')
                password = request.form.get('password')
                cus_totalOrder = 0

                cus = Customer(cus_sex,
                               cus_email,
                               cus_name,
                               cus_surname,
                               cus_Birthdate,
                               cus_telNo,
                               cus_totalOrder)

                db.session.add(cus)
                db.session.commit()

                id = Customer.query.filter_by(cus_email=email).first().cus_id
                cuslog = CustomerLogin(id, username, password)

                db.session.add(cuslog)
                db.session.commit()

                return render_template('customer_login.html')

@app.route('/customer_login')
def customer_login():
    return render_template('customer_login.html')

@app.route('/customer_page', methods=['GET', 'POST'])
def customer_page():
    if request.method == 'POST':
        if not request.form['username'] or not request.form['password']:
            flash('Please enter all the fields', 'error')
        else:
            username = request.form.get('username')
            password = request.form.get('password')

            cuslog = CustomerLogin.query.filter_by(username=username, password=password).first()  # if this returns a user, then the email already exists in database

            if cuslog:  # if a user is found, we want to redirect back to signup page so user can try again
                cus = Customer.query.filter_by(cus_id=cuslog.customerID).first()
                response = make_response(render_template('customer_page.html', customer = cus, customerlogin = cuslog))
                response.set_cookie("cus_id", str(cus.cus_id))
                response.set_cookie("cuslog_id", str(cuslog.customerID))
                return response

            else:
                flash('Incorrect Email or Password')
                return render_template('customer_login.html')
    else:
        print('error')

@app.route('/admin_login')
def admin_login():
    return render_template('admin_login.html')

@app.route('/admin_page', methods=['GET', 'POST'])
def admin_page():
    if request.method == 'POST':
        if not request.form['username'] or not request.form['password']:
            flash('Please enter all the fields', 'error')
        else:
            username = request.form.get('username')
            password = request.form.get('password')

            adminlog = AdminLogin.query.filter_by(username=username, password=password).first()  # if this returns a user, then the email already exists in database

            if adminlog:  # if a user is found, we want to redirect back to signup page so user can try again
                admin = Admin.query.filter_by(memberID=adminlog.adminId).first()
                admin_emp = Employee.query.filter_by(memberID=admin.memberID).first()
                response = make_response(render_template('admin_page.html', admin_emp = admin_emp, admin = admin, adminlog = adminlog))
                response.set_cookie("emp_id", str(admin_emp.memberID))
                response.set_cookie("admin_id", str(admin.memberID))
                response.set_cookie("adminlog_id", str(adminlog.adminId))
                return response
            else:
                flash('Incorrect Email or Password')
                return render_template('admin_login.html')
    else:
        print('error')

@app.route('/update_customer_info_page')
def update_customer_info_page():
    cus_id = int(request.cookies.get('cus_id'))
    cuslog_id = int(request.cookies.get('cuslog_id'))
    cus = Customer.query.filter_by(cus_id=cus_id).first()
    cus_log = CustomerLogin.query.filter_by(customerID = cuslog_id).first()
    response = make_response(render_template('update_customer_info.html', customer = cus, customerlogin = cus_log))
    response.set_cookie("cus_id", str(cus_id))
    response.set_cookie("cuslog_id", str(cuslog_id))

    return response

@app.route('/update_customer_info', methods=['GET', 'POST'])
def update_customer_info():
    cus_id = int(request.cookies.get('cus_id'))
    cuslog_id = int(request.cookies.get('cuslog_id'))
    cus = Customer.query.filter_by(cus_id=cus_id).first()
    cus_log = CustomerLogin.query.filter_by(customerID=cuslog_id).first()

    if request.method == 'POST':
        if False:
            response = make_response(render_template('customer_page.html', customer = cus, customerlogin = cus_log))
            response.set_cookie("cus_id", str(cus_id))
            response.set_cookie("cuslog_id", str(cuslog_id))
            return response

        else:
            if request.form.get('gender') == "male":
                cus.cus_sex = False
            else:
                 cus.cus_sex = True
            cus.cus_email = request.form.get('email')
            cus.cus_name = request.form.get('name')
            cus.cus_surname = request.form.get('surname')
            cus.cus_Birthdate = request.form.get('birthdate')
            cus.cus_telNo = request.form.get('telno')
            cus_log.username = request.form.get('username')
            cus.log_password = request.form.get('password')

            response = make_response(render_template('customer_page.html', customer = cus, customerlogin = cus_log))
            response.set_cookie("cus_id", str(cus_id))
            response.set_cookie("cuslog_id", str(cuslog_id))
            return response

@app.route('/add_new_employee_page')
def add_new_employee_page():
    emp_id = int(request.cookies.get('emp_id'))
    admin_id = int(request.cookies.get('admin_id'))
    adminlog_id = int(request.cookies.get('adminlog_id'))
    admin = Admin.query.filter_by(memberID=admin_id).first()
    admin_emp = Employee.query.filter_by(memberID=emp_id).first()
    adminlog = AdminLogin.query.filter_by(adminId=adminlog_id).first()

    response = make_response(render_template('add_new_employee.html', admin_emp = admin_emp, admin = admin, adminlog = adminlog))
    response.set_cookie("emp_id", str(admin_emp.memberID))
    response.set_cookie("admin_id", str(admin.memberID))
    response.set_cookie("adminlog_id", str(adminlog.adminId))
    return response

@app.route('/add_new_employee', methods=['GET', 'POST'])
def add_new_employee():
    emp_id = int(request.cookies.get('emp_id'))
    admin_id = int(request.cookies.get('admin_id'))
    adminlog_id = int(request.cookies.get('adminlog_id'))
    admin = Admin.query.filter_by(memberID=admin_id).first()
    admin_emp = Employee.query.filter_by(memberID=emp_id).first()
    adminlog = AdminLogin.query.filter_by(adminId=adminlog_id).first()

    if request.method == 'POST':
        if False:
            response = make_response(render_template('admin_page.html', admin_emp=admin_emp, admin=admin, adminlog=adminlog))
            response.set_cookie("emp_id", str(admin_emp.memberID))
            response.set_cookie("admin_id", str(admin.memberID))
            response.set_cookie("adminlog_id", str(adminlog.adminId))
            return response

        else:
            name = request.form.get('name')
            surname = request.form.get('surname')
            address = request.form.get('address')
            telNo = request.form.get('telno')
            Birthdate = request.form.get('birthdate')
            startDate = request.form.get('startdate')
            salary = request.form.get('salary')
            email = request.form.get('email')
            Department = request.form.get('departmentid')
            username = request.form.get('username')
            password = request.form.get('password')

            emp = Employee(name,
                           surname,
                           address,
                           telNo,
                           Birthdate,
                           startDate,
                           salary,
                           email,
                           Department)

            db.session.add(emp)
            db.session.commit()

            id = Employee.query.filter_by(email=email).first().memberID
            c_id = admin.C_id
            emplog = EmployeeLogin(id, username, password)

            db.session.add(emplog)
            db.session.commit()

            response = make_response(render_template('admin_page.html', admin_emp=admin_emp, admin=admin, adminlog=adminlog))
            response.set_cookie("emp_id", str(admin_emp.memberID))
            response.set_cookie("admin_id", str(admin.memberID))
            response.set_cookie("adminlog_id", str(adminlog.adminId))
            return response


if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    db.create_all()
    app.run(debug=True)
