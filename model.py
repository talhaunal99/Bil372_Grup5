from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:test@localhost/Perfume Database'
app.config['SQLALCHEMY_ECHO'] = False
db = SQLAlchemy(app)


class Customer(db.Model):
    __tablename__ = 'customer'
    cus_id = db.Column(db.Integer, primary_key=True)
    cus_sex=db.Column(db.Boolean)
    cus_email=db.Column(db.String(80), unique=True)
    cus_name = db.Column(db.String(80))
    cus_surname = db.Column(db.String(80))
    cus_Birthdate = db.Column(db.DateTime)
    cus_telNo=db.Column(db.String)
    cus_totalOrder=db.Column(db.Integer)

class Order(db.Model):
    __tablename__ = 'Order'
    order_no = db.Column(db.Integer, primary_key=True)
    order_date=db.Column(db.DateTime)
    customer_id=db.Column(db.Integer, db.ForeignKey('customer.cus_id'))
    carrier_id = db.Column(db.Integer,db.ForeignKey('Employee.memberID'))
#Employee için class oluşturulduğunda __tablename__ yazan yerdeki isim Employee olacak ve memberID columnuna sahip olacak


class Made_by(db.Model):
    __tablename__ = 'Made_by'
    madebyID = db.Column(db.Integer, primary_key=True)
    perfumeID=db.Column(db.Integer,db.ForeignKey('ProductId'))

class Content(db.Model):
    __tablename__ = 'Content'
    contentId = db.Column(db.Integer, primary_key=True)
    perfumeID=db.Column(db.Integer,db.ForeignKey('ProductId'))

class Takes(db.Model):
    __tablename__ = 'Takes'
    matId = db.Column(db.Integer,db.ForeignKey('mat_id'))
    memberId=db.Column(db.Integer,db.ForeignKey('memberID'))
    quantity=db.Column(db.Integer)
    firm_name=db.Column(db.String(40))
    cost=db.Column(db.Integer)

class Vehicle(db.Model):
    __tablename__ = 'Vehicle'
    c_id = db.Column(db.Integer,db.ForeignKey('Company.C_id'))
    vehicle_id=db.Column(db.Integer,primary_key=True)
    package=db.Column(db.Integer) #the number of products which are carried
    licence_plate=db.Column(db.String(40))
    kilometer=db.Column(db.Integer)
    first_price = db.Column(db.Integer)
    last_price= db.Column(db.Integer)
    vehicle_type=db.Column(db.String)

class Perfume(db.Model):
    __tablename__ = 'Perfume'
    Category = db.Column(db.String(20))
    ProductID=db.Column(db.Integer,primary_key=True)
    Content=db.Column(db.Array(db.String(40)))
    Price=db.Column(db.Integer)
    Duration = db.Column(db.Integer)
    NumberOfStock= db.Column(db.Integer)
    made_by=db.Column(db.Integer,db.ForeignKey('Employee.memberID'))

class Department(db.Model):
    __tablename__ = 'Department'
    dep_address = db.Column(db.String(20))
    dep_TelNo=db.Column(db.String(40))
    dep_name=db.Column(db.String(40))
    department_id=db.Column(db.Integer,primary_key=True)
    salary = db.Column(db.Integer)
    c_id= db.Column(db.Integer,db.ForeignKey('Company.C_id'))

class Confirms(db.Model):
    __tablename__ = 'Confirms'
    ProductID = db.Column(db.Integer, db.ForeignKey('Perfume.ProductID'))
    memberID = db.Column(db.Integer, db.ForeignKey('Employee.memberID'))
    verification_no = db.Column(db.Integer)

class Packages(db.Model):
    __tablename__ = 'Packages'
    packageID = db.Column(db.Integer, primary_key = True)
    ProductID = db.Column(db.Integer, db.ForeignKey('Perfume.ProductId'))
    memberID = db.Column(db.Integer, db.ForeignKey('Employee.memberID'))
    Expiration_Date = db.Column(db.DateTime)
    production_Date = db.Column(db.DateTime)

class ConsistOf(db.Model):
    __tablename__ = 'ConsistOf'
    product_id = db.Column(db.Integer, db.ForeignKey('Perfume.ProductID'))
    mat_id = db.Column(db.Integer, db.ForeignKey('Material.mat_id'))

class Includes(db.Model):
    __tablename__ = 'Includes'
    order_no = db.Column(db.Integer, db.ForeignKey('Order.order_no'))
    ProductId = db.Column(db.Integer, db.ForeignKey('Product.ProductID'))
    quantitiy = db.Column(db.Integer)

class Company(db.Model):
    __tablename__ = 'Company'
    C_id = db.Column(db.Integer, primary_key = True)
    Name = db.Column(db.String(80))
    Budget = db.Column(db.Integer)
    Address = db.Column(db.String(200))
    TelNo = db.Column(db.String(11))

class Manages(db.Model):
    __tablename__ = 'Manages'
    C_id = db.Column(db.Integer, db.ForeignKey('Company.C_id'))

class Produces(db.Model):
    __tablename__ = 'Produces'
    chemist_id = db.Column(db.Integer, db.ForeignKey('Employee.memberID'))
    ProductID = db.Column(db.Integer, db.ForeignKey('Perfume.ProductID'))

class Material(db.Model):
    __tablename__ = 'Material'
    mat_id = db.Column(db.Integer, primary_key = True)
    mat_name = db.Column(db.String(80))
    mat_region = db.Column(db.String(80))
    mat_stock = db.Column(db.Integer)
    mat_price = db.Column(db.Integer)

class Employee(db.Model):
    __tablename__ = 'Employee'
    memberID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    surname = db.Column(db.String(30))
    address = db.Column(db.String(200))
    telNo = db.Column(db.String(11))
    Birthdate = db.Column(db.DateTime)
    startDate = db.Column(db.DateTime)
    salary = db.Column(db.Integer)
    email = db.Column(db.String(80))
    Department = db.Column(db.String(80))
    Company_id = db.Column(db.Integer, db.ForeignKey('Company.C_id'))

class Carrier(db.Model):
    __tablename__ = 'Carrier'
    drivingLicenceType= db.Column(db.String(20))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('Vehicle.vehicle_id'))
    memberID= db.Column(db.Integer,db.ForeignKey('Employee.memberID'))

class Sells(db.Model):
    __tablename__ = 'Sells'
    ProductID = db.Column(db.Integer, db.ForeignKey('Perfume.ProductId'))
    C_id= db.Column(db.Integer,db.ForeignKey('Company.C_id'))

class Admin(db.Model):
    __tablename__ = 'Admin'
    memberID = db.Column(db.Integer, db.ForeignKey('Employee.memberID'))
    C_id = db.Column(db.Integer, db.ForeignKey('Company.C_id'))

class Analyst(db.Model):
    __tablename__ = 'Analyst'
    memberID = db.Column(db.Integer, db.ForeignKey('Employee.memberID'))
    method=db.Column(db.String(40))

class Customer_Service(db.Model):
    __tablename__ = 'Customer_Service'
    memberID = db.Column(db.Integer, db.ForeignKey('Employee.memberID'))

class Supplier(db.Model):
    __tablename__ = 'Supplier'
    memberID = db.Column(db.Integer, db.ForeignKey('Employee.memberID'))

class Accountant(db.Model):
    __tablename__ = 'Accountant'
     memberID = db.Column(db.Integer, db.ForeignKey('Employee.memberID'))

class Worker(db.Model):
    __tablename__ = 'Worker'
     memberID = db.Column(db.Integer, db.ForeignKey('Employee.memberID'))

# db.create_all() tum tablelar bittikten sonra bunu calistiracagiz (normalizasyon dahil)

if __name__ == '__main__':
    app.run()
