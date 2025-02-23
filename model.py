from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, flash, url_for, redirect, render_template, make_response
from flask_migrate import Migrate
import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:password@localhost/Perfume Database'
app.config['SQLALCHEMY_ECHO'] = False
db = SQLAlchemy(app)

class Customer(db.Model):
    __tablename__ = 'customer'
    cus_id = db.Column(db.Integer, primary_key=True, autoincrement=True,unique=True)
    cus_sex=db.Column(db.Boolean)
    cus_email=db.Column(db.String, unique=True)
    cus_name = db.Column(db.String(80))
    cus_surname = db.Column(db.String(80))
    cus_Birthdate = db.Column(db.Date)
    cus_telNo=db.Column(db.String)
    cus_totalOrder=db.Column(db.Integer)
    cus_address = db.Column(db.String)

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
    order_no = db.Column(db.Integer,autoincrement=True,primary_key=True,unique=True)
    customer_id=db.Column(db.Integer, db.ForeignKey('customer.cus_id'),primary_key=True)
    carrier_id = db.Column(db.Integer,db.ForeignKey('Employee.memberID'),primary_key=True)

    def __init__(self, customer_id, carrier_id):
        self.customer_id=customer_id
        self.carrier_id=carrier_id

class OrderDate(db.Model): #Normalization
    __tablename__ = 'OrderDate'
    order_no = db.Column(db.Integer,db.ForeignKey('Order.order_no'), primary_key=True)
    order_date = db.Column(db.Date)

    def __init__(self, order_no, order_date):
        self.order_no = order_no
        self.order_date = order_date

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
    Category = db.Column(db.String)
    ProductID=db.Column(db.Integer,primary_key=True,autoincrement=True)
    Content=db.Column(db.String)
    Price=db.Column(db.Float)
    Duration = db.Column(db.Integer)
    NumberOfStock= db.Column(db.Integer)

    def __init__(self, Category, ProductID, Content, Price, Duration, NumberOfStock):
        self.Category = Category
        self.ProductID = ProductID
        self.Content = Content
        self.Price = Price
        self.Duration = Duration
        self.NumberOfStock = NumberOfStock

class Department(db.Model):
    __tablename__ = 'Department'
    dep_address = db.Column(db.String)
    dep_TelNo=db.Column(db.String)
    dep_name=db.Column(db.String)
    department_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    c_id= db.Column(db.Integer,db.ForeignKey('Company.C_id'))

    def __init__(self, dep_address, dep_TelNo, dep_name, department_id, c_id):
        self.dep_address = dep_address
        self.dep_TelNo = dep_TelNo
        self.dep_name = dep_name
        self.department_id = department_id
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
    Expiration_Date = db.Column(db.Date)
    production_Date = db.Column(db.Date)

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
    Name = db.Column(db.String)
    Budget = db.Column(db.Integer)
    Address = db.Column(db.String)
    TelNo = db.Column(db.String)

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
    memberID = db.Column(db.Integer, primary_key=True,autoincrement=True,unique=True)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    address = db.Column(db.String)
    telNo = db.Column(db.String)
    Birthdate = db.Column(db.Date)
    startDate = db.Column(db.Date)
    salary = db.Column(db.Integer)
    email = db.Column(db.String)
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

    def __init__(self, vehicle_id, memberID):
        self.vehicle_id = vehicle_id
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
    method=db.Column(db.String)

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
db.create_all()
