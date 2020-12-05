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
    cus_address = db.Column(db.String(200))

    def __init__(self, cus_sex, cus_email, cus_name, cus_surname, cus_Birthdate, cus_telNo, cus_totalOrder, cus_address):
        self.cus_sex = cus_sex
        self.cus_email = cus_email
        self.cus_name = cus_name
        self.cus_surname = cus_surname
        self.cus_Birthdate = cus_Birthdate
        self.cus_telNo = cus_telNo
        self.cus_totalOrder = cus_totalOrder
        self.cus_address = cus_address

class EmployeeLogin(db.Model):
    employeeID = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    type = db.Column(db.String)

    def __init__(self, employeeID, username, password, type):
        self.employeeID = employeeID
        self.username = username
        self.password = password
        self.type = type

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

    def __init__(self, order_no, customer_id, carrier_id):
        self.order_no = order_no
        self.customer_id = customer_id
        self.carrier_id = carrier_id

class OrderDate(db.Model): #Normalization
    __tablename__ = 'OrderDate'
    order_no = db.Column(db.Integer,db.ForeignKey('Order.order_no'), primary_key=True)
    order_date = db.Column(db.DateTime)

    def __init__(self, order_no, order_date):
        self.order_no = order_no
        self.order_date = order_date


class Made_by(db.Model):
    __tablename__ = 'Made_by'
    madebyID = db.Column(db.Integer, db.ForeignKey('Employee.memberID'),primary_key=True)
    perfumeID=db.Column(db.Integer,db.ForeignKey('Perfume.ProductID'),primary_key=True)

    def __init__(self, madebyID, perfumeID):
        self.madebyID = madebyID
        self.perfumeID = perfumeID

class Content(db.Model):
    __tablename__ = 'Content'
    contentId = db.Column(db.Integer, primary_key=True)
    perfumeID=db.Column(db.Integer,db.ForeignKey('Perfume.ProductID'))

    def __init__(self, contentId, perfumeID):
        self.contentId = contentId
        self.perfumeID = perfumeID

class Takes(db.Model):
    __tablename__ = 'Takes'
    matId = db.Column(db.Integer,db.ForeignKey('Material.mat_id'),primary_key=True)
    memberId=db.Column(db.Integer,db.ForeignKey('Employee.memberID'),primary_key=True)
    quantity=db.Column(db.Integer)
    cost=db.Column(db.Integer)

    def __init__(self, matId, memberId, quantity, cost):
        self.matId = matId
        self.memberId = memberId
        self.quantity = quantity
        self.cost = cost

class TakesFirm(db.Model): #Normalization
    __tablename__ = 'takesFirm'
    matId = db.Column(db.Integer,db.ForeignKey('Material.mat_id',primary_key=True))
    memberID = db.Column(db.Integer,db.ForeignKey('Employee.memberID'),primary_key=True)
    firm_name = db.Column(db.String)

    def __init__(self, matId, memberID, firm_name):
        self.matId = matId
        self.memberID = memberID
        self.firm_name = firm_name

class Vehicle(db.Model):
    __tablename__ = 'Vehicle'
    c_id = db.Column(db.Integer,db.ForeignKey('Company.C_id'))
    vehicle_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    package=db.Column(db.Integer) #the number of products which are carried

    def __init__(self, c_id, vehicle_id, package):
        self.c_id = c_id
        self.vehicle_id = vehicle_id
        self.package = package

class VehicleFeatures(db.Model): #Normalization
    __tablename__ = 'VehicleFeatures'
    vehicle_id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    licence = db.Column(db.String(40))
    kilometer = db.Column(db.Integer)
    first_price = db.Column(db.Integer)
    last_price = db.Column(db.Integer)
    vehicle_type = db.Column(db.String)

    def __init__(self, vehicle_id, licence, kilometer, first_price, last_price, vehicle_type):
        self.vehicle_id = vehicle_id
        self.licence = licence
        self.kilometer = kilometer
        self. first_price = first_price
        self.last_price = last_price
        self.vehicle_type = vehicle_type

class Perfume(db.Model):
    __tablename__ = 'Perfume'
    Category = db.Column(db.String(20))
    ProductID=db.Column(db.Integer,primary_key=True,autoincrement=True)
    Content=db.Column(db.String(40))
    Price=db.Column(db.Integer)
    Duration = db.Column(db.Integer)
    NumberOfStock= db.Column(db.Integer)

    def __init__(self, Category, ProductID, Content, Price, Duration, NumberOfStock):
        self.Category = Category
        self.ProductID = ProductID
        self.Content = Content
        self.Price = Price
        self.Duration = Duration
        self.NumberOfStock = NumberOfStock


class MadePerfume(db.Model): #Normalization
    __tablename__ = 'MadePerfume',
    ProductId = db.Column(db.Integer,primary_key=True,autoincrement=True)
    made_by = db.Column(db.Integer,db.ForeignKey('Employee.memberID'))

    def __init__(self, ProductId, made_by):
        self.ProductId = ProductId
        self.made_by = made_by

class Department(db.Model):
    __tablename__ = 'Department'
    dep_address = db.Column(db.String(20))
    dep_TelNo=db.Column(db.String(40))
    dep_name=db.Column(db.String(40))
    department_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    salary = db.Column(db.Integer)
    c_id= db.Column(db.Integer,db.ForeignKey('Company.C_id'))

    def __init__(self, dep_address, dep_TelNo, dep_name, department_id, salary, c_id):
        self.dep_address = dep_address
        self.dep_TelNo = dep_TelNo
        self.dep_name = dep_name
        self.department_id = department_id
        self.salary = salary
        self.c_id = c_id

class Confirms(db.Model):
    __tablename__ = 'Confirms'
    ProductID = db.Column(db.Integer, db.ForeignKey('Perfume.ProductID'),primary_key=True)
    memberID = db.Column(db.Integer, db.ForeignKey('Employee.memberID'),primary_key=True)
    verification_no = db.Column(db.Integer)

    def __init__(self, ProductID, memberID, verification_no):
        self.ProductID = ProductID
        self.memberID = memberID
        self.verification_no = verification_no

class Packages(db.Model):
    __tablename__ = 'Packages'
    packageID = db.Column(db.Integer, primary_key = True,autoincrement=True)
    ProductID = db.Column(db.Integer, db.ForeignKey('Perfume.ProductID'))
    memberID = db.Column(db.Integer, db.ForeignKey('Employee.memberID'))

    def __init__(self, packageID, ProductID, memberID):
        self.packageID = packageID
        self.ProductID = ProductID
        self.memberID = memberID

class ProductFeature(db.Model): #Normalization
    __tablename__ = 'ProductFeature'
    packageID = db.Column(db.Integer,primary_key=True,autoincrement=True)
    ProductId = db.Column(db.Integer,db.ForeignKey('Perfume.ProductID'))
    Expiration_Date = db.Column(db.DateTime)
    production_Date = db.Column(db.DateTime)

    def __init__(self, packageID, ProductId, Expiration_Date, production_Date):
        self.packageID = packageID
        self.ProductId = ProductId
        self.Expiration_Date = Expiration_Date
        self.production_Date = production_Date

class ConsistOf(db.Model):
    __tablename__ = 'ConsistOf'
    product_id = db.Column(db.Integer, db.ForeignKey('Perfume.ProductID'),primary_key=True)
    mat_id = db.Column(db.Integer, db.ForeignKey('Material.mat_id'),primary_key=True)

    def __init__(self, product_id, mat_id):
        self.product_id = product_id
        self.mat_id = mat_id

class Includes(db.Model):
    __tablename__ = 'Includes'
    order_no = db.Column(db.Integer, db.ForeignKey('Order.order_no'),primary_key=True)
    ProductId = db.Column(db.Integer, db.ForeignKey('Perfume.ProductID'),primary_key=True)

    def __init__(self, order_no, ProductId):
        self.order_no = order_no
        self.ProductId = ProductId

class ProductQuantity(db.Model): #Normalization
    __tablename__ = 'ProductQuantity'
    order_no = db.Column(db.Integer,db.ForeignKey('Order.order_no'),primary_key=True)
    quantity = db.Column(db.Integer)

    def __init__(self, order_no, quantity):
        self.order_no = order_no
        self.quantity = quantity

class Company(db.Model):
    __tablename__ = 'Company'
    C_id = db.Column(db.Integer, primary_key = True,autoincrement=True)
    Name = db.Column(db.String(80))
    Budget = db.Column(db.Integer)
    Address = db.Column(db.String(200))
    TelNo = db.Column(db.String(11))

    def __init__(self, C_id, Name, Budget, Address, TelNo):
        self.C_id = C_id
        self.Name = Name
        self.Budget = Budget
        self.Address = Address
        self.TelNo = TelNo

class Manages(db.Model):
    __tablename__ = 'Manages'
    C_id = db.Column(db.Integer, db.ForeignKey('Company.C_id'),primary_key=True)
    memberID = db.Column(db.Integer, db.ForeignKey('Employee.memberID'),primary_key=True)

    def __init__(self, C_id, memberID):
        self.C_id = C_id
        self.memberID = memberID

class Produces(db.Model):
    __tablename__ = 'Produces'
    chemist_id = db.Column(db.Integer, db.ForeignKey('Employee.memberID'),primary_key=True)
    ProductID = db.Column(db.Integer, db.ForeignKey('Perfume.ProductID'),primary_key=True)

    def __init__(self, chemist_id, ProductID):
        self.chemist_id = chemist_id
        self.ProductID = ProductID

class Material(db.Model):
    __tablename__ = 'Material'
    mat_id = db.Column(db.Integer, primary_key = True,autoincrement=True)
    mat_name = db.Column(db.String(80))
    mat_region = db.Column(db.String(80))
    mat_stock = db.Column(db.Integer)
    mat_price = db.Column(db.Integer)

    def __init__(self, mat_id, mat_name, mat_region, mat_stock, mat_price):
        self.mat_id = mat_id
        self.mat_name = mat_name
        self.mat_region = mat_region
        self.mat_stock = mat_stock
        self.mat_price = mat_price

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
    department_id=db.Column(db.Integer,db.ForeignKey('Department.department_id'), primary_key = True)

    def __init__(self, name, surname, address, telNo, Birthdate, startDate, salary, email, department_id):
        self.name = name
        self.surname = surname
        self.address = address
        self.telNo = telNo
        self.Birthdate = Birthdate
        self.startDate = startDate
        self.salary = salary
        self.email = email
        self.department_id = department_id

class EmployeesOfCompany(db.Model): #Normalization
    __tablename__ = 'EmployessOfCompany'
    memberID = db.Column(db.Integer,db.ForeignKey('Employee.memberID'),primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('Company.C_id'),primary_key=True)

    def __init__(self, memberID, company_id):
        self.memberID = memberID
        self.company_id = company_id

class Carrier(db.Model):
    __tablename__ = 'Carrier'
    vehicle_id = db.Column(db.Integer, db.ForeignKey('Vehicle.vehicle_id'),primary_key=True)
    memberID= db.Column(db.Integer,db.ForeignKey('Employee.memberID'),primary_key=True)

    def __init__(self, vehhicle_id, memberID):
        self.vehicle_id = vehhicle_id
        self.memberID = memberID

class MemberLicenceType(db.Model): #Normalization
    __tablename__ = 'MemberLicenceType'
    memberID = db.Column(db.Integer,db.ForeignKey('Employee.memberID'),primary_key=True)
    drivingLicenceType = db.Column(db.String(20))

    def __init__(self, memberID, drivingLicenceType):
        self.memberID = memberID
        self.drivingLicenceType = drivingLicenceType

class Sells(db.Model):
    __tablename__ = 'Sells'
    ProductID = db.Column(db.Integer, db.ForeignKey('Perfume.ProductID'),primary_key=True)
    C_id= db.Column(db.Integer,db.ForeignKey('Company.C_id'),primary_key=True)

    def __init__(self, ProductID, C_id):
        self.ProductID = ProductID
        self.C_id = C_id

class Admin(db.Model):
    __tablename__ = 'Admin'
    memberID = db.Column(db.Integer, db.ForeignKey('Employee.memberID'),primary_key=True)
    C_id = db.Column(db.Integer, db.ForeignKey('Company.C_id'))

    def __init__(self, memberID, C_id):
        self.memberID = memberID
        self.C_id = C_id

class Analyst(db.Model):
    __tablename__ = 'Analyst'
    memberID = db.Column(db.Integer, db.ForeignKey('Employee.memberID'),primary_key=True)
    method=db.Column(db.String(40))

    def __init__(self, memberID, method):
        self.memberID = memberID
        self.method = method

class Customer_Service(db.Model):
    __tablename__ = 'Customer_Service'
    memberID = db.Column(db.Integer, db.ForeignKey('Employee.memberID'),primary_key=True)

    def __init__(self, memberID):
        self.memberID = memberID

class Supplier(db.Model):
    __tablename__ = 'Supplier'
    memberID = db.Column(db.Integer, db.ForeignKey('Employee.memberID'),primary_key=True)

    def __init__(self, memberID):
        self.memberID = memberID

class Accountant(db.Model):
    __tablename__ = 'Accountant'
    memberID = db.Column(db.Integer, db.ForeignKey('Employee.memberID'),primary_key=True)

    def __init__(self, memberID):
        self.memberID = memberID

class Worker(db.Model):
    __tablename__ = 'Worker'
    memberID = db.Column(db.Integer, db.ForeignKey('Employee.memberID'),primary_key=True)

    def __init__(self, memberID):
        self.memberID = memberID

class Chemist(db.Model):
    __tablename__ = 'Chemist'
    memberID = db.Column(db.Integer, db.ForeignKey('Employee.memberID'),primary_key=True)

    def __init__(self, memberID):
        self.memberID = memberID

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
            department_id = request.form.get('departmentid')
            username = request.form.get('username')
            password = request.form.get('password')
            type = request.form.get('job')


            emp = Employee(name,
                           surname,
                           address,
                           telNo,
                           Birthdate,
                           startDate,
                           salary,
                           email,
                           department_id)

            db.session.add(emp)
            db.session.commit()

            id = Employee.query.filter_by(email=email).first().memberID
            c_id = admin.C_id
            emplog = EmployeeLogin(id, username, password, type)

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
