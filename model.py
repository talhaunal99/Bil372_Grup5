from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:test@localhost/PerfumeDatabase'
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

class EmployeeLogin(db.Model):
    customerID = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)

class CustomerLogin(db.Model):
    customerID=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String,unique=True)
    password=db.Column(db.String)

class AdminLogin(db.Model):
    adminId=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String,unique=True)
    password=db.Column(db.String)

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
    Explanation=db.Column(db.String)


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

db.create_all()

if __name__ == '__main__':
    app.run()
