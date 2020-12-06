import pandas as pd
from model import db

from model import Employee,Customer,CustomerLogin,Carrier,Chemist,Company,Content,Confirms,ConsistOf,Customer_Service,EmployeesOfCompany,Accountant,Includes,EmployeeLogin,AdminLogin,Admin,Analyst,Takes,TakesFirm,Order,Sells,Department,Made_by,MadePerfume,Manages,Material,MemberLicenceType,OrderDate,Packages,Perfume,Produces,ProductFeature,Supplier,Vehicle,VehicleFeatures,Worker,ProductQuantity
import pandas as pd

engine = db.get_engine()  # db is the one from the question
csv_file_path = 'admin.csv'

# Read CSV with Pandas
with open(csv_file_path, 'r', encoding='utf-8-sig') as file:
    df = pd.read_csv(file)

# Insert to DB
df.to_sql('Admin',
          con=engine,
          index=False,
          index_label='memberID',
          if_exists='append')

csv_file_path = 'accountant.csv'

# Read CSV with Pandas
with open(csv_file_path, 'r', encoding='utf-8-sig') as file:
    df = pd.read_csv(file)

# Insert to DB
df.to_sql('Accountant',
          con=engine,
          index=False,
          index_label='memberID',
          if_exists='append')

csv_file_path = 'AdminLogin.csv'

# Read CSV with Pandas
with open(csv_file_path, 'r', encoding='utf-8-sig') as file:
    df = pd.read_csv(file)

# Insert to DB
df.to_sql('admin_login',
          con=engine,
          index=False,
          index_label='memberID',
          if_exists='append')

csv_file_path = 'analyst.csv'

# Read CSV with Pandas
with open(csv_file_path, 'r', encoding='utf-8-sig') as file:
    df = pd.read_csv(file)

# Insert to DB
df.to_sql('Analyst',
          con=engine,
          index=False,
          index_label='memberID',
          if_exists='append')



csv_file_path = 'chemist.csv'

# Read CSV with Pandas
with open(csv_file_path, 'r', encoding='utf-8-sig') as file:
    df = pd.read_csv(file)

# Insert to DB
df.to_sql('Chemist',
          con=engine,
          index=False,
          index_label='memberID',
          if_exists='append')

csv_file_path = 'customer_service.csv'

# Read CSV with Pandas
with open(csv_file_path, 'r', encoding='utf-8-sig') as file:
    df = pd.read_csv(file)

# Insert to DB
df.to_sql('Customer_Service',
          con=engine,
          index=False,
          index_label='memberID',
          if_exists='append')

csv_file_path = 'customerList.csv'

# Read CSV with Pandas
with open(csv_file_path, 'r', encoding='utf-8-sig') as file:
    df = pd.read_csv(file)

# Insert to DB
df.to_sql('customer',
          con=engine,
          index=False,
          index_label='cus_id',
          if_exists='append')

csv_file_path = 'carrier.csv'

# Read CSV with Pandas
with open(csv_file_path, 'r',encoding='utf-8-sig') as file:
    df = pd.read_csv(file)

# Insert to DB
df.to_sql('Carrier',
          con=engine,
          index=False,
          index_label='memberID',
          if_exists='append')

# Read CSV with Pandas
with open(csv_file_path, 'r',encoding='utf-8-sig') as file:
    df = pd.read_csv(file)

# Insert to DB
df.to_sql('Order',
          con=engine,
          index=False,
          index_label='order_no',
          if_exists='append')

csv_file_path = 'customerLogin.csv'

# Read CSV with Pandas
with open(csv_file_path, 'r',encoding='utf-8-sig') as file:
    df = pd.read_csv(file)

# Insert to DB
df.to_sql('customer_login',
          con=engine,
          index=False,
          index_label='customerID',
          if_exists='append')

csv_file_path = 'department.csv'

# Read CSV with Pandas
with open(csv_file_path, 'r', encoding='utf-8-sig') as file:
    df = pd.read_csv(file)

# Insert to DB
df.to_sql('Department',
          con=engine,
          index=False,
          index_label='department_id',
          if_exists='append')

csv_file_path = 'employess.csv'

# Read CSV with Pandas
with open(csv_file_path, 'r',encoding='utf-8-sig') as file:
    df = pd.read_csv(file)

# Insert to DB
df.to_sql('Employee',
          con=engine,
          index=False,
          index_label='employeeID',
          if_exists='append')

csv_file_path = 'employeesOfCompanies.csv'

# Read CSV with Pandas
with open(csv_file_path, 'r', encoding='utf-8-sig') as file:
    df = pd.read_csv(file)

# Insert to DB
df.to_sql('employeesOfCompanies',
          con=engine,
          index=False,
          index_label='memberID',
          if_exists='append')

csv_file_path = 'material.csv'

# Read CSV with Pandas
with open(csv_file_path, 'r', encoding='utf-8-sig') as file:
    df = pd.read_csv(file)

# Insert to DB
df.to_sql('Material',
          con=engine,
          index=False,
          index_label='mat_id',
          if_exists='append')

csv_file_path = 'orderDate.csv'

# Read CSV with Pandas
with open(csv_file_path, 'r', encoding='utf-8-sig') as file:
    df = pd.read_csv(file)

# Insert to DB
df.to_sql('orderDate',
          con=engine,
          index=False,
          index_label='order_no',
          if_exists='append')

csv_file_path = 'Perfume.csv'

# Read CSV with Pandas
with open(csv_file_path, 'r', encoding='utf-8-sig') as file:
    df = pd.read_csv(file)

# Insert to DB
df.to_sql('Perfume',
          con=engine,
          index=False,
          index_label='ProductID',
          if_exists='append')

csv_file_path = 'supplier.csv'

# Read CSV with Pandas
with open(csv_file_path, 'r', encoding='utf-8-sig') as file:
    df = pd.read_csv(file)

# Insert to DB
df.to_sql('Supplier',
          con=engine,
          index=False,
          index_label='memberID',
          if_exists='append')
csv_file_path = 'vehicleFeatures.csv'

# Read CSV with Pandas
with open(csv_file_path, 'r', encoding='utf-8-sig') as file:
    df = pd.read_csv(file)

# Insert to DB
df.to_sql('VehicleFeatures',
          con=engine,
          index=False,
          index_label='vehicle_id',
          if_exists='append')

csv_file_path = 'worker.csv'

# Read CSV with Pandas
with open(csv_file_path, 'r', encoding='utf-8-sig') as file:
    df = pd.read_csv(file)

# Insert to DB
df.to_sql('Worker',
          con=engine,
          index=False,
          index_label='memberID',
          if_exists='append')


