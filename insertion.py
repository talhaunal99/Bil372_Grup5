import pandas as pd
from sqlalchemy.exc import IntegrityError

from model import db

from model import Employee,Customer,CustomerLogin,Carrier,Chemist,Company,Content,Confirms,ConsistOf,Customer_Service,EmployeesOfCompany,Accountant,Includes,EmployeeLogin,AdminLogin,Admin,Analyst,Takes,TakesFirm,Order,Sells,Department,Made_by,MadePerfume,Manages,Material,MemberLicenceType,OrderDate,Packages,Perfume,Produces,ProductFeature,Supplier,Vehicle,VehicleFeatures,Worker,ProductQuantity
import pandas as pd

engine = db.get_engine()  # db is the one from the question
csv_file_path = 'company.csv'

# Read CSV with Pandas
with open(csv_file_path, 'r', encoding='utf-8-sig') as file:
    df = pd.read_csv(file)

# Insert to DB
for i in range(len(df)):
    try:
        df.iloc[i:i+1].to_sql(name="Company",if_exists='append',con = engine,index=False)
    except IntegrityError:
        pass #or any other action
csv_file_path = 'department.csv'

# Read CSV with Pandas
with open(csv_file_path, 'r', encoding='utf-8-sig') as file:
    df = pd.read_csv(file)

# Insert to DB
for i in range(len(df)):
    try:
        df.iloc[i:i+1].to_sql(name="Department",if_exists='append',con = engine,index=False)
    except IntegrityError:
        pass #or any other action



csv_file_path = 'employees.csv'

# Read CSV with Pandas
with open(csv_file_path, 'r',encoding='utf-8-sig') as file:
    df = pd.read_csv(file, index_col=[0])

# Insert to DB
for i in range(len(df)):
    try:
        df.iloc[i:i+1].to_sql(name="Employee",if_exists='append',con = engine,index=False)
    except IntegrityError:
        pass #or any other action


csv_file_path = 'admin.csv'

# Read CSV with Pandas
with open(csv_file_path, 'r', encoding='utf-8-sig') as file:
    df = pd.read_csv(file)

# Insert to DB
for i in range(len(df)):
    try:
        df.iloc[i:i+1].to_sql(name="Admin",if_exists='append',con = engine,index=False)
    except IntegrityError:
        pass #or any other action

csv_file_path = 'accountant.csv'

# Read CSV with Pandas
with open(csv_file_path, 'r', encoding='utf-8-sig') as file:
    df = pd.read_csv(file)

# Insert to DB
for i in range(len(df)):
    try:
        df.iloc[i:i+1].to_sql(name="Accountant",if_exists='append',con = engine,index=False)
    except IntegrityError:
        pass #or any other action

csv_file_path = 'AdminLogin.csv'

# Read CSV with Pandas
with open(csv_file_path, 'r', encoding='utf-8-sig') as file:
    df = pd.read_csv(file)

# Insert to DB
for i in range(len(df)):
    try:
        df.iloc[i:i+1].to_sql(name="admin_login",if_exists='append',con = engine,index=False)
    except IntegrityError:
        pass #or any other action

csv_file_path = 'analyst.csv'

# Read CSV with Pandas
with open(csv_file_path, 'r', encoding='utf-8-sig') as file:
    df = pd.read_csv(file)

# Insert to DB
for i in range(len(df)):
    try:
        df.iloc[i:i+1].to_sql(name="Analyst",if_exists='append',con = engine,index=False)
    except IntegrityError:
        pass #or any other action



csv_file_path = 'chemist.csv'

# Read CSV with Pandas
with open(csv_file_path, 'r', encoding='utf-8-sig') as file:
    df = pd.read_csv(file)

# Insert to DB
for i in range(len(df)):
    try:
        df.iloc[i:i+1].to_sql(name="Chemist",if_exists='append',con = engine,index=False)
    except IntegrityError:
        pass #or any other action

csv_file_path = 'customer_service.csv'

# Read CSV with Pandas
with open(csv_file_path, 'r', encoding='utf-8-sig') as file:
    df = pd.read_csv(file)

# Insert to DB
for i in range(len(df)):
    try:
        df.iloc[i:i+1].to_sql(name="Customer_Service",if_exists='append',con = engine,index=False)
    except IntegrityError:
        pass #or any other action

csv_file_path = 'customerList.csv'

# Read CSV with Pandas
with open(csv_file_path, 'r', encoding='utf-8-sig') as file:
    df = pd.read_csv(file)

# Insert to DB
for i in range(len(df)):
    try:
        df.iloc[i:i+1].to_sql(name="customer",if_exists='append',con = engine,index=False)
    except IntegrityError:
        pass #or any other action

csv_file_path = 'carrier.csv'

# Read CSV with Pandas
with open(csv_file_path, 'r',encoding='utf-8-sig') as file:
    df = pd.read_csv(file)

# Insert to DB
for i in range(len(df)):
    try:
        df.iloc[i:i+1].to_sql(name="MemberLicenceType",if_exists='append',con = engine,index=False)
    except IntegrityError:
        pass #or any other action

csv_file_path='customerOrder.csv'
# Read CSV with Pandas
with open(csv_file_path, 'r',encoding='utf-8-sig') as file:
    df = pd.read_csv(file)

# Insert to DB
for i in range(len(df)):
    try:
        df.iloc[i:i+1].to_sql(name="Order",if_exists='append',con = engine,index=False)
    except IntegrityError:
        pass #or any other action

csv_file_path = 'customerLogin.csv'

# Read CSV with Pandas
with open(csv_file_path, 'r',encoding='utf-8-sig') as file:
    df = pd.read_csv(file)

# Insert to DB
for i in range(len(df)):
    try:
        df.iloc[i:i+1].to_sql(name="customer_login",if_exists='append',con = engine,index=False)
    except IntegrityError:
        pass #or any other action


csv_file_path = 'employeesOfCompanies.csv'

# Read CSV with Pandas
with open(csv_file_path, 'r', encoding='utf-8-sig') as file:
    df = pd.read_csv(file)

# Insert to DB
for i in range(len(df)):
    try:
        df.iloc[i:i+1].to_sql(name="employeesOfCompanies",if_exists='append',con = engine,index=False)
    except IntegrityError:
        pass #or any other action

csv_file_path = 'material.csv'

# Read CSV with Pandas
with open(csv_file_path, 'r', encoding='utf-8-sig') as file:
    df = pd.read_csv(file)

# Insert to DB
for i in range(len(df)):
    try:
        df.iloc[i:i+1].to_sql(name="Material",if_exists='append',con = engine,index=False)
    except IntegrityError:
        pass #or any other action

csv_file_path = 'orderDate.csv'

# Read CSV with Pandas
with open(csv_file_path, 'r', encoding='utf-8-sig') as file:
    df = pd.read_csv(file)

# Insert to DB
for i in range(len(df)):
    try:
        df.iloc[i:i+1].to_sql(name="orderDate",if_exists='append',con = engine,index=False)
    except IntegrityError:
        pass #or any other action

csv_file_path = 'Perfume.csv'

# Read CSV with Pandas
with open(csv_file_path, 'r', encoding='utf-8-sig') as file:
    df = pd.read_csv(file)

# Insert to DB
for i in range(len(df)):
    try:
        df.iloc[i:i+1].to_sql(name="Perfume",if_exists='append',con = engine,index=False)
    except IntegrityError:
        pass #or any other action

csv_file_path = 'supplier.csv'

# Read CSV with Pandas
with open(csv_file_path, 'r', encoding='utf-8-sig') as file:
    df = pd.read_csv(file)

# Insert to DB
for i in range(len(df)):
    try:
        df.iloc[i:i+1].to_sql(name="Supplier",if_exists='append',con = engine,index=False)
    except IntegrityError:
        pass #or any other action
csv_file_path = 'vehicleFeatures.csv'

# Read CSV with Pandas
with open(csv_file_path, 'r', encoding='utf-8-sig') as file:
    df = pd.read_csv(file)

# Insert to DB
for i in range(len(df)):
    try:
        df.iloc[i:i+1].to_sql(name="VehicleFeatures",if_exists='append',con = engine,index=False)
    except IntegrityError:
        pass #or any other action

csv_file_path = 'worker.csv'

# Read CSV with Pandas
with open(csv_file_path, 'r', encoding='utf-8-sig') as file:
    df = pd.read_csv(file)

# Insert to DB
for i in range(len(df)):
    try:
        df.iloc[i:i+1].to_sql(name="Worker",if_exists='append',con = engine,index=False)
    except IntegrityError:
        pass #or any other action

csv_file_path = 'carrierVehicle.csv'

# Read CSV with Pandas
with open(csv_file_path, 'r', encoding='utf-8-sig') as file:
    df = pd.read_csv(file)

# Insert to DB
for i in range(len(df)):
    try:
        df.iloc[i:i+1].to_sql(name="Carrier",if_exists='append',con = engine,index=False)
    except IntegrityError:
        pass

