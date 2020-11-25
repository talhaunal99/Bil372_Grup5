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




# db.create_all() tum tablelar bittikten sonra bunu calistiracagiz (normalizasyon dahil)




if __name__ == '__main__':
    app.run()
