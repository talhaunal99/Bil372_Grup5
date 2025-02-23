from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, flash, url_for, redirect, render_template, make_response
from flask_migrate import Migrate
import datetime
from model import db, app
from model import Employee,Customer,CustomerLogin,Carrier,Chemist,Company,Content,Confirms,ConsistOf,Customer_Service,EmployeesOfCompany,Accountant,Includes,EmployeeLogin,AdminLogin,Admin,Analyst,Takes,Order,Sells,Department,Manages,Material,MemberLicenceType,OrderDate,Packages,Perfume,ProductFeature,Supplier,Vehicle,VehicleFeatures,Worker,ProductQuantity
from random import randrange

@app.route('/')
def opening():
    print('opening')
    return render_template('Welcome.html')

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
                cus_address = request.form.get('address')
                username = request.form.get('username')
                password = request.form.get('password')
                cus_totalOrder = 0

                cus = Customer(cus_sex,
                               cus_email,
                               cus_name,
                               cus_surname,
                               cus_Birthdate,
                               cus_telNo,
                               cus_totalOrder,
                               cus_address)

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
                response = make_response(render_template('Main-Page.html', customer = cus, customerlogin = cuslog))
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
                response = make_response(render_template('AdminHomePage.html', admin_emp = admin_emp, admin = admin, adminlog = adminlog))
                response.set_cookie("emp_id", str(admin_emp.memberID))
                response.set_cookie("admin_id", str(admin.memberID))
                response.set_cookie("adminlog_id", str(adminlog.adminId))
                return response
            else:
                flash('Incorrect Email or Password')
                return render_template('admin_login.html')
    else:
        print('error')
        
@app.route('/employee_login')
def employee_login():
    return render_template('employee_login.html')

@app.route('/employee_page', methods=['GET', 'POST']) # Type'a gore degisiklikler yapilmasi gerek.
def employee_page():
    if request.method == 'POST':
        if not request.form['username'] or not request.form['password'] or not request.form['type']:
            flash('Please enter all the fields', 'error')
        else:
            username = request.form.get('username')
            password = request.form.get('password')
            type = request.form.get('type')
            emplog = EmployeeLogin.query.filter_by(username=username, password=password, type=type).first()  # if this returns a user, then the email already exists in database

            if emplog:  # if a user is found, we want to redirect back to signup page so user can try again
                emp = Employee.query.filter_by(memberID=emplog.employeeID).first()
                if type == "carrier":
                    response = make_response(render_template('carrier_page.html', employee=emp, employeelogin=emplog))
                    response.set_cookie("emp_id", str(emp.memberID))
                    response.set_cookie("emplog_id", str(emplog.employeeID))
                    response.set_cookie("emplog_type", str(emplog.type))
                    return response
                elif type == "chemist":
                    response = make_response(render_template('chemist_page.html', employee=emp, employeelogin=emplog))
                    response.set_cookie("emp_id", str(emp.memberID))
                    response.set_cookie("emplog_id", str(emplog.employeeID))
                    response.set_cookie("emplog_type", str(emplog.type))
                    return response
                elif type == "supplier":
                    response = make_response(render_template('supplier_page.html', employee=emp, employeelogin=emplog))
                    response.set_cookie("emp_id", str(emp.memberID))
                    response.set_cookie("emplog_id", str(emplog.employeeID))
                    response.set_cookie("emplog_type", str(emplog.type))
                    return response
                else:
                    response = make_response(render_template('employee_page.html', employee=emp, employeelogin=emplog))
                    response.set_cookie("emp_id", str(emp.memberID))
                    response.set_cookie("emplog_id", str(emplog.employeeID))
                    response.set_cookie("emplog_type", str(emplog.type))
                    return response
            else:
                flash('Incorrect Email or Password')
                return render_template('employee_login.html')
    else:
        print('error')

@app.route('/carrierpage', methods=['GET', 'POST']) # Type'a gore degisiklikler yapilmasi gerek.
def carrier_page():
    if request.method == 'POST':
        if not request.form['username'] or not request.form['password']:
            flash('Please enter all the fields', 'error')
        else:
            username = request.form.get('username')
            password = request.form.get('password')

            emplog = EmployeeLogin.query.filter_by(username=username, password=password).first()  # if this returns a user, then the email already exists in database

            if emplog:  # if a user is found, we want to redirect back to signup page so user can try again
                emp = Employee.query.filter_by(emp_id=emplog.employeeID).first()
                response = make_response(render_template('carrierpage.html', employee = emp, employeelogin = emplog))
                response.set_cookie("emp_id", str(emp.emp_id))
                response.set_cookie("emplog_id", str(emplog.employeeID))
                return response

            else:
                flash('Incorrect Email or Password')
                return render_template('employee_login.html')
    else:
        print('error')

@app.route('/chemist_page', methods=['GET', 'POST']) # Type'a gore degisiklikler yapilmasi gerek.
def chemist_page():
    if request.method == 'POST':
        if not request.form['username'] or not request.form['password']:
            flash('Please enter all the fields', 'error')
        else:
            username = request.form.get('username')
            password = request.form.get('password')

            emplog = EmployeeLogin.query.filter_by(username=username, password=password).first()  # if this returns a user, then the email already exists in database

            if emplog:  # if a user is found, we want to redirect back to signup page so user can try again
                emp = Employee.query.filter_by(emp_id=emplog.employeeID).first()
                response = make_response(render_template('chemist_page.html', employee = emp, employeelogin = emplog))
                response.set_cookie("emp_id", str(emp.emp_id))
                response.set_cookie("emplog_id", str(emplog.employeeID))
                return response

            else:
                flash('Incorrect Email or Password')
                return render_template('employee_login.html')
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
    print(cus.cus_name)
    print(cus_log.password)

    if request.method == 'POST':
        if False:
            response = make_response(render_template('Profile.html', customer = cus, customerlogin = cus_log))
            response.set_cookie("cus_id", str(cus_id))
            response.set_cookie("cuslog_id", str(cuslog_id))
            return response

        else:
            if request.form.get('gender') == "male":
                cus.cus_sex = False
                gender = "Male"
            else:
                cus.cus_sex = True
                gender = "Female"

            cus.cus_email = request.form.get('email')
            cus.cus_name = request.form.get('name')
            cus.cus_surname = request.form.get('surname')
            cus.cus_Birthdate = request.form.get('birthdate')
            cus.cus_telNo = request.form.get('telno')
            cus.cus_address = request.form.get('address')
            db.session.commit()

            cus_log.username = request.form.get('username')
            cus_log.password = request.form.get('password')
            db.session.commit()

            response = make_response(render_template('Profile.html', customer = cus, customerlogin = cus_log, content = gender))
            response.set_cookie("cus_id", str(cus_id))
            response.set_cookie("cuslog_id", str(cuslog_id))
            return response

@app.route('/update_employee_info_page')
def update_employee_info_page():
    emp_id = request.args.get('memberID')
    emplog_id = request.args.get('memberID')
    print(emp_id)
    print(emplog_id)
    emp = Employee.query.filter_by(memberID=emp_id).first()
    emp_log = EmployeeLogin.query.filter_by(employeeID = emplog_id).first()
    response = make_response(render_template('update_employee_info.html', employee = emp, employeelogin = emp_log, Employee=Employee.query.all()))
    response.set_cookie("emp_id", str(emp_id))
    response.set_cookie("emplog_id", str(emplog_id))

    return response

@app.route('/update_employee_info', methods=['GET', 'POST'])
def update_employee_info():
    emp_id = int(request.cookies.get('emp_id'))
    emplog_id = int(request.cookies.get('emplog_id'))
    emp = Employee.query.filter_by(memberID=emp_id).first()
    emp_log = EmployeeLogin.query.filter_by(employeeID=emplog_id).first()
    print(emp.name)
    print(emp_log.password)

    if request.method == 'POST':
        if False:
            response = make_response(render_template('Profile.html', customer = cus, customerlogin = cus_log))
            response.set_cookie("cus_id", str(cus_id))
            response.set_cookie("cuslog_id", str(cuslog_id))
            return response

        else:
            emp.email = request.form.get('email')
            emp.name = request.form.get('name')
            emp.surname = request.form.get('surname')
            emp.Birthdate = request.form.get('birthdate')
            emp.address = request.form.get('address')
            emp.telNo = request.form.get('telno')
            emp.salary = request.form.get('salary')
            db.session.commit()

            emp_log.username = request.form.get('username')
            emp_log.password = request.form.get('password')
            db.session.commit()

            response = make_response(render_template('list_employees.html', employee = emp, employeelogin = emp_log, Employee=Employee.query.all()))
            response.set_cookie("emp_id", str(emp_id))
            response.set_cookie("emplog_id", str(emplog_id))
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
            response = make_response(render_template('AdminHomePage.html', admin_emp=admin_emp, admin=admin, adminlog=adminlog))
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

            if type == "accountant":
                newemp = Accountant(id)
                db.session.add(newemp)
                db.session.commit()
            elif type == "analyst":
                newemp = Analyst(id)
                db.session.add(newemp)
                db.session.commit()
            elif type == "carrier":
                newemp = Carrier(1, id)
                db.session.add(newemp)
                db.session.commit()
            elif type == "chemist":
                newemp = Chemist(id)
                db.session.add(newemp)
                db.session.commit()
            elif type == "customer service":
                newemp = Accountant(id)
                db.session.add(newemp)
                db.session.commit()
            elif type == "supplier":
                newemp = Supplier(id)
                db.session.add(newemp)
                db.session.commit()
            else:
                newemp = Worker(id)
                db.session.add(newemp)
                db.session.commit()

            response = make_response(render_template('AdminHomePage.html', admin_emp=admin_emp, admin=admin, adminlog=adminlog))
            response.set_cookie("emp_id", str(admin_emp.memberID))
            response.set_cookie("admin_id", str(admin.memberID))
            response.set_cookie("adminlog_id", str(adminlog.adminId))
            return response

@app.route('/list_employees')
def list_employees():
    emp_id = int(request.cookies.get('emp_id'))
    admin_id = int(request.cookies.get('admin_id'))
    adminlog_id = int(request.cookies.get('adminlog_id'))
    admin = Admin.query.filter_by(memberID=admin_id).first()
    admin_emp = Employee.query.filter_by(memberID=emp_id).first()
    adminlog = AdminLogin.query.filter_by(adminId=adminlog_id).first()
    response = make_response(render_template('list_employees.html', Employee=Employee.query.all()))
    response.set_cookie("emp_id", str(admin_emp.memberID))
    response.set_cookie("admin_id", str(admin.memberID))
    response.set_cookie("adminlog_id", str(adminlog.adminId))
    return response

@app.route('/list_vehicles')
def list_vehicles():
    response = make_response(render_template('list_vehicles.html', VehicleFeatures=VehicleFeatures.query.all()))
    return response

@app.route('/list_orders')
def list_orders():
    response = make_response(render_template('list_orders.html', Order=Order.query.all(), OrderDate=OrderDate.query.all()))
    return response

@app.route('/list_orders_forCarriers')
def list_orders_forCarriers():
    emp_id = int(request.cookies.get('emp_id'))
    response = make_response(render_template('list_orders_forCarriers.html', emp_id=emp_id, Order=Order.query.all(), OrderDate=OrderDate.query.all()))
    return response

@app.route('/list_perfumes_readyForPackage')
def list_perfumes_readyForPackage():
    response = make_response(render_template('list_perfumes_readyForPackage.html', Perfume=Perfume.query.all()))
    return response

@app.route('/list_customers')
def list_customers():
    response = make_response(render_template('list_customers.html', Customer=Customer.query.all()))
    return response

@app.route('/about_us')
def about_us():
    return render_template('AboutUs.html')

@app.route('/profile')
def profile():
    cus_id = int(request.cookies.get('cus_id'))
    cuslog_id = int(request.cookies.get('cuslog_id'))
    cus = Customer.query.filter_by(cus_id=cus_id).first()
    cus_log = CustomerLogin.query.filter_by(customerID = cuslog_id).first()
    if cus.cus_sex == True:
        gender = "Female"
    else:
        gender = "Male"
    response = make_response(render_template('Profile.html', customer = cus, customerlogin = cus_log, content = gender))
    response.set_cookie("cus_id", str(cus_id))
    response.set_cookie("cuslog_id", str(cuslog_id))
    return response

@app.route('/main_page')
def main_page():
    cus_id = int(request.cookies.get('cus_id'))
    cuslog_id = int(request.cookies.get('cuslog_id'))
    cus = Customer.query.filter_by(cus_id=cus_id).first()
    cus_log = CustomerLogin.query.filter_by(customerID = cuslog_id).first()
    response = make_response(render_template('Main-Page.html', customer = cus, customerlogin = cus_log))
    response.set_cookie("cus_id", str(cus_id))
    response.set_cookie("cuslog_id", str(cuslog_id))
    return response

@app.route('/admin_home_page')
def admin_home_page():
    emp_id = int(request.cookies.get('emp_id'))
    admin_id = int(request.cookies.get('admin_id'))
    adminlog_id = int(request.cookies.get('adminlog_id'))
    admin = Admin.query.filter_by(memberID=admin_id).first()
    admin_emp = Employee.query.filter_by(memberID=emp_id).first()
    adminlog = AdminLogin.query.filter_by(adminId=adminlog_id).first()
    response = make_response(render_template('AdminHomePage.html', admin_emp=admin_emp, admin=admin, adminlog=adminlog))
    response.set_cookie("emp_id", str(admin_emp.memberID))
    response.set_cookie("admin_id", str(admin.memberID))
    response.set_cookie("adminlog_id", str(adminlog.adminId))
    return response

@app.route('/make_perfume')
def make_perfume():
    emp_id = int(request.cookies.get("emp_id"))
    emplog_id = int(request.cookies.get("emplog_id"))
    emp = Employee.query.filter_by(memberID = emp_id).first()
    emplog = EmployeeLogin.query.filter_by(employeeID = emplog_id).first()
    print(emplog_id)
    print(emplog.type)
    response = make_response(render_template('MakePerfume.html', employee=emp, employeelogin=emplog, error = 0))
    response.set_cookie("emp_id", str(emp_id))
    response.set_cookie("emplog_id", str(emplog_id))
    response.set_cookie("emplog_type", str(emplog.type))
    return response

@app.route('/items')
def items():
    emp_id = int(request.cookies.get("emp_id"))
    emplog_id = int(request.cookies.get("emplog_id"))
    emp = Employee.query.filter_by(memberID = emp_id).first()
    emplog = EmployeeLogin.query.filter_by(employeeID = emplog_id).first()
    print(emplog_id)
    print(emplog.type)
    response = make_response(render_template('Items.html', employee=emp, employeelogin=emplog, error = 0))
    response.set_cookie("emp_id", str(emp_id))
    response.set_cookie("emplog_id", str(emplog_id))
    response.set_cookie("emplog_type", str(emplog.type))
    return response

@app.route('/shop')
def shop():
    cus_id = int(request.cookies.get('cus_id'))
    cuslog_id = int(request.cookies.get('cuslog_id'))
    cus = Customer.query.filter_by(cus_id=cus_id).first()
    cus_log = CustomerLogin.query.filter_by(customerID = cuslog_id).first()
    response = make_response(render_template('Page-3.html', customer = cus, customerlogin = cus_log, error=0))
    response.set_cookie("cus_id", str(cus_id))
    response.set_cookie("cuslog_id", str(cuslog_id))
    return response

@app.route('/get_material')
def get_material():
    mat_id=request.args.get('mat_id')
    material=Material.query.filter_by(mat_id=mat_id).first()
    company = Company.query.filter_by(C_id=1).first()
    emp_id = int(request.cookies.get("emp_id"))
    emplog_id = int(request.cookies.get("emplog_id"))
    emp = Employee.query.filter_by(memberID = emp_id).first()
    emplog = EmployeeLogin.query.filter_by(employeeID = emplog_id).first()

    if company.Budget > material.mat_price:
        company.Budget = company.Budget - material.mat_price
        db.session.commit()
        material.mat_stock = material.mat_stock + 1
        db.session.commit()
        response = make_response(render_template('Items.html', employee=emp, employeelogin=emplog, error=2))
        response.set_cookie("emp_id", str(emp_id))
        response.set_cookie("emplog_id", str(emplog_id))
        response.set_cookie("emplog_type", str(emplog.type))
        return response
    else:
        response = make_response(render_template('Items.html', employee=emp, employeelogin=emplog, error=1))
        response.set_cookie("emp_id", str(emp_id))
        response.set_cookie("emplog_id", str(emplog_id))
        response.set_cookie("emplog_type", str(emplog.type))
        return response

@app.route('/deliver')
def deliver():
    order_no = request.args.get('order_no')
    order=Order.query.filter_by(order_no = order_no).first()
    print(order_no)
    emp_id = request.args.get('emp_id')
    print(emp_id)
    carrier = Carrier.query.filter_by(memberID=emp_id).first()
    print(carrier.memberID)
    vehicle = VehicleFeatures.query.filter_by(vehicle_id=carrier.vehicle_id).first()

    vehicle.kilometer = vehicle.kilometer+5
    db.session.commit()
    vehicle.last_price=vehicle.last_price-5*50
    print(vehicle.vehicle_id)
    db.session.commit()
    order_date=OrderDate.query.filter_by(order_no = order_no).first()
    db.session.delete(order)
    db.session.delete(order_date)
    db.session.commit()
    response = make_response(render_template('list_orders_forCarriers.html', emp_id=emp_id, Order=Order.query.all(),OrderDate=OrderDate.query.all()))
    return response

@app.route('/add_perfume')
def add_perfume():
    id=request.args.get('id')
    emp_id = int(request.cookies.get("emp_id"))
    ProductID = int(id)
    emplog_id = int(request.cookies.get("emplog_id"))
    emp = Employee.query.filter_by(memberID = emp_id).first()
    emplog = EmployeeLogin.query.filter_by(employeeID = emplog_id).first()

    if ProductID == 1:
        mat_id = 6
        mat = Material.query.filter_by(mat_id = mat_id).first()
        if mat.mat_stock>0:
            perfume = Perfume.query.filter_by(ProductID = ProductID).first()
            print(perfume.Category)
            perfume.NumberOfStock = perfume.NumberOfStock+1
            db.session.commit()
            mat.mat_stock = mat.mat_stock-1
            db.session.commit()
            response = make_response(render_template('MakePerfume.html', employee=emp, employeelogin=emplog, error=2))
            response.set_cookie("emp_id", str(emp_id))
            response.set_cookie("emplog_id", str(emplog_id))
            response.set_cookie("emplog_type", str(emplog.type))
            return response
        else:
            response = make_response(render_template('MakePerfume.html', employee=emp, employeelogin=emplog, error=1))
            response.set_cookie("emp_id", str(emp_id))
            response.set_cookie("emplog_id", str(emplog_id))
            response.set_cookie("emplog_type", str(emplog.type))
            return response
    elif ProductID == 2:
        mat_id = 2
        mat_id2 = 5
        mat = Material.query.filter_by(mat_id = mat_id).first()
        mat2 = Material.query.filter_by(mat_id = mat_id2).first()
        if mat.mat_stock>0 and mat2.mat_stock>0:
            perfume = Perfume.query.filter_by(ProductID = ProductID).first()
            perfume.NumberOfStock = perfume.NumberOfStock+1
            db.session.commit()
            mat.mat_stock = mat.mat_stock-1
            db.session.commit()
            mat2.mat_stock = mat2.mat_stock-1
            db.session.commit()
            response = make_response(render_template('MakePerfume.html', employee=emp, employeelogin=emplog, error=2))
            response.set_cookie("emp_id", str(emp_id))
            response.set_cookie("emplog_id", str(emplog_id))
            response.set_cookie("emplog_type", str(emplog.type))
            return response
        else:
            response = make_response(render_template('MakePerfume.html', employee=emp, employeelogin=emplog, error=1))
            response.set_cookie("emp_id", str(emp_id))
            response.set_cookie("emplog_id", str(emplog_id))
            response.set_cookie("emplog_type", str(emplog.type))
            return response
    elif ProductID == 3:
        mat_id = 5
        mat_id2 = 9
        mat = Material.query.filter_by(mat_id = mat_id).first()
        mat2 = Material.query.filter_by(mat_id = mat_id2).first()
        if mat.mat_stock>0 and mat2.mat_stock>0:
            perfume = Perfume.query.filter_by(ProductID = ProductID).first()
            perfume.NumberOfStock = perfume.NumberOfStock+1
            db.session.commit()
            mat.mat_stock = mat.mat_stock-1
            db.session.commit()
            mat2.mat_stock = mat2.mat_stock-1
            db.session.commit()
            response = make_response(render_template('MakePerfume.html', employee=emp, employeelogin=emplog, error=2))
            response.set_cookie("emp_id", str(emp_id))
            response.set_cookie("emplog_id", str(emplog_id))
            response.set_cookie("emplog_type", str(emplog.type))
            return response
        else:
            response = make_response(render_template('MakePerfume.html', employee=emp, employeelogin=emplog, error=1))
            response.set_cookie("emp_id", str(emp_id))
            response.set_cookie("emplog_id", str(emplog_id))
            response.set_cookie("emplog_type", str(emplog.type))
            return response
    elif ProductID == 4:
        mat_id = 2
        mat_id2 = 11
        mat = Material.query.filter_by(mat_id = mat_id).first()
        mat2 = Material.query.filter_by(mat_id = mat_id2).first()
        if mat.mat_stock>0 and mat2.mat_stock>0:
            perfume = Perfume.query.filter_by(ProductID = ProductID).first()
            perfume.NumberOfStock = perfume.NumberOfStock+1
            db.session.commit()
            mat.mat_stock = mat.mat_stock-1
            db.session.commit()
            mat2.mat_stock = mat2.mat_stock-1
            db.session.commit()
            response = make_response(render_template('MakePerfume.html', employee=emp, employeelogin=emplog, error=2))
            response.set_cookie("emp_id", str(emp_id))
            response.set_cookie("emplog_id", str(emplog_id))
            response.set_cookie("emplog_type", str(emplog.type))
            return response
        else:
            response = make_response(render_template('MakePerfume.html', employee=emp, employeelogin=emplog, error=1))
            response.set_cookie("emp_id", str(emp_id))
            response.set_cookie("emplog_id", str(emplog_id))
            response.set_cookie("emplog_type", str(emplog.type))
            return response
    elif ProductID == 5:
        mat_id = 2
        mat_id2 = 6
        mat = Material.query.filter_by(mat_id = mat_id).first()
        mat2 = Material.query.filter_by(mat_id = mat_id2).first()
        if mat.mat_stock>0 and mat2.mat_stock>0:
            perfume = Perfume.query.filter_by(ProductID = ProductID).first()
            perfume.NumberOfStock = perfume.NumberOfStock+1
            db.session.commit()
            mat.mat_stock = mat.mat_stock-1
            db.session.commit()
            mat2.mat_stock = mat2.mat_stock-1
            db.session.commit()
            response = make_response(render_template('MakePerfume.html', employee=emp, employeelogin=emplog, error=2))
            response.set_cookie("emp_id", str(emp_id))
            response.set_cookie("emplog_id", str(emplog_id))
            response.set_cookie("emplog_type", str(emplog.type))
            return response
        else:
            response = make_response(render_template('MakePerfume.html', employee=emp, employeelogin=emplog, error=1))
            response.set_cookie("emp_id", str(emp_id))
            response.set_cookie("emplog_id", str(emplog_id))
            response.set_cookie("emplog_type", str(emplog.type))
            return response
    elif ProductID == 6:
        mat_id = 12
        mat_id2 = 13
        mat = Material.query.filter_by(mat_id = mat_id).first()
        mat2 = Material.query.filter_by(mat_id = mat_id2).first()
        if mat.mat_stock>0 and mat2.mat_stock>0:
            perfume = Perfume.query.filter_by(ProductID = ProductID).first()
            perfume.NumberOfStock = perfume.NumberOfStock+1
            db.session.commit()
            mat.mat_stock = mat.mat_stock-1
            db.session.commit()
            mat2.mat_stock = mat2.mat_stock-1
            db.session.commit()
            response = make_response(render_template('MakePerfume.html', employee=emp, employeelogin=emplog, error=2))
            response.set_cookie("emp_id", str(emp_id))
            response.set_cookie("emplog_id", str(emplog_id))
            response.set_cookie("emplog_type", str(emplog.type))
            return response
        else:
            response = make_response(render_template('MakePerfume.html', employee=emp, employeelogin=emplog, error=1))
            response.set_cookie("emp_id", str(emp_id))
            response.set_cookie("emplog_id", str(emplog_id))
            response.set_cookie("emplog_type", str(emplog.type))
            return response
    elif ProductID == 7:
        mat_id = 12
        mat_id2 = 15
        mat = Material.query.filter_by(mat_id = mat_id).first()
        mat2 = Material.query.filter_by(mat_id = mat_id2).first()
        if mat.mat_stock>0 and mat2.mat_stock>0:
            perfume = Perfume.query.filter_by(ProductID = ProductID).first()
            perfume.NumberOfStock = perfume.NumberOfStock+1
            db.session.commit()
            mat.mat_stock = mat.mat_stock-1
            db.session.commit()
            mat2.mat_stock = mat2.mat_stock-1
            db.session.commit()
            response = make_response(render_template('MakePerfume.html', employee=emp, employeelogin=emplog, error=2))
            response.set_cookie("emp_id", str(emp_id))
            response.set_cookie("emplog_id", str(emplog_id))
            response.set_cookie("emplog_type", str(emplog.type))
            return response
        else:
            response = make_response(render_template('MakePerfume.html', employee=emp, employeelogin=emplog, error=1))
            response.set_cookie("emp_id", str(emp_id))
            response.set_cookie("emplog_id", str(emplog_id))
            response.set_cookie("emplog_type", str(emplog.type))
            return response
    elif ProductID == 8:
        mat_id = 7
        mat = Material.query.filter_by(mat_id = mat_id).first()
        if mat.mat_stock>0:
            perfume = Perfume.query.filter_by(ProductID = ProductID).first()
            perfume.NumberOfStock = perfume.NumberOfStock+1
            db.session.commit()
            mat.mat_stock = mat.mat_stock-1
            db.session.commit()
            response = make_response(render_template('MakePerfume.html', employee=emp, employeelogin=emplog, error=2))
            response.set_cookie("emp_id", str(emp_id))
            response.set_cookie("emplog_id", str(emplog_id))
            response.set_cookie("emplog_type", str(emplog.type))
            return response
        else:
            response = make_response(render_template('MakePerfume.html', employee=emp, employeelogin=emplog, error=1))
            response.set_cookie("emp_id", str(emp_id))
            response.set_cookie("emplog_id", str(emplog_id))
            response.set_cookie("emplog_type", str(emplog.type))
            return response
    elif ProductID == 9:
        mat_id = 2
        mat_id2 = 3
        mat = Material.query.filter_by(mat_id = mat_id).first()
        mat2 = Material.query.filter_by(mat_id = mat_id2).first()
        if mat.mat_stock>0 and mat2.mat_stock>0:
            perfume = Perfume.query.filter_by(ProductID = ProductID).first()
            perfume.NumberOfStock = perfume.NumberOfStock+1
            db.session.commit()
            mat.mat_stock = mat.mat_stock-1
            db.session.commit()
            mat2.mat_stock = mat2.mat_stock-1
            db.session.commit()
            response = make_response(render_template('MakePerfume.html', employee=emp, employeelogin=emplog, error=2))
            response.set_cookie("emp_id", str(emp_id))
            response.set_cookie("emplog_id", str(emplog_id))
            response.set_cookie("emplog_type", str(emplog.type))
            return response
        else:
            response = make_response(render_template('MakePerfume.html', employee=emp, employeelogin=emplog, error=1))
            response.set_cookie("emp_id", str(emp_id))
            response.set_cookie("emplog_id", str(emplog_id))
            response.set_cookie("emplog_type", str(emplog.type))
            return response
    elif ProductID == 10:
        mat_id = 2
        mat_id2 = 6
        mat = Material.query.filter_by(mat_id = mat_id).first()
        mat2 = Material.query.filter_by(mat_id = mat_id2).first()
        if mat.mat_stock>0 and mat2.mat_stock>0:
            perfume = Perfume.query.filter_by(ProductID = ProductID).first()
            perfume.NumberOfStock = perfume.NumberOfStock+1
            db.session.commit()
            mat.mat_stock = mat.mat_stock-1
            db.session.commit()
            mat2.mat_stock = mat2.mat_stock-1
            db.session.commit()
            response = make_response(render_template('MakePerfume.html', employee=emp, employeelogin=emplog, error=2))
            response.set_cookie("emp_id", str(emp_id))
            response.set_cookie("emplog_id", str(emplog_id))
            response.set_cookie("emplog_type", str(emplog.type))
            return response
        else:
            response = make_response(render_template('MakePerfume.html', employee=emp, employeelogin=emplog, error=1))
            response.set_cookie("emp_id", str(emp_id))
            response.set_cookie("emplog_id", str(emplog_id))
            response.set_cookie("emplog_type", str(emplog.type))
            return response
    elif ProductID == 11:
        mat_id = 13
        mat = Material.query.filter_by(mat_id = mat_id).first()
        if mat.mat_stock>0:
            perfume = Perfume.query.filter_by(ProductID = ProductID).first()
            perfume.NumberOfStock = perfume.NumberOfStock+1
            db.session.commit()
            mat.mat_stock = mat.mat_stock-1
            db.session.commit()
            response = make_response(render_template('MakePerfume.html', employee=emp, employeelogin=emplog, error=2))
            response.set_cookie("emp_id", str(emp_id))
            response.set_cookie("emplog_id", str(emplog_id))
            response.set_cookie("emplog_type", str(emplog.type))
            return response
        else:
            response = make_response(render_template('MakePerfume.html', employee=emp, employeelogin=emplog, error=1))
            response.set_cookie("emp_id", str(emp_id))
            response.set_cookie("emplog_id", str(emplog_id))
            response.set_cookie("emplog_type", str(emplog.type))
            return response
    elif ProductID == 12:
        mat_id = 8
        mat = Material.query.filter_by(mat_id = mat_id).first()
        if mat.mat_stock>0:
            perfume = Perfume.query.filter_by(ProductID = ProductID).first()
            perfume.NumberOfStock = perfume.NumberOfStock+1
            db.session.commit()
            mat.mat_stock = mat.mat_stock-1
            db.session.commit()
            response = make_response(render_template('MakePerfume.html', employee=emp, employeelogin=emplog, error=2))
            response.set_cookie("emp_id", str(emp_id))
            response.set_cookie("emplog_id", str(emplog_id))
            response.set_cookie("emplog_type", str(emplog.type))
            return response
        else:
            response = make_response(render_template('MakePerfume.html', employee=emp, employeelogin=emplog, error=1))
            response.set_cookie("emp_id", str(emp_id))
            response.set_cookie("emplog_id", str(emplog_id))
            response.set_cookie("emplog_type", str(emplog.type))
            return response
    elif ProductID == 13:
        mat_id = 1
        mat_id2 = 4
        mat = Material.query.filter_by(mat_id = mat_id).first()
        mat2 = Material.query.filter_by(mat_id = mat_id2).first()
        if mat.mat_stock>0 and mat2.mat_stock>0:
            perfume = Perfume.query.filter_by(ProductID = ProductID).first()
            perfume.NumberOfStock = perfume.NumberOfStock+1
            db.session.commit()
            mat.mat_stock = mat.mat_stock-1
            db.session.commit()
            mat2.mat_stock = mat2.mat_stock-1
            db.session.commit()
            response = make_response(render_template('MakePerfume.html', employee=emp, employeelogin=emplog, error=2))
            response.set_cookie("emp_id", str(emp_id))
            response.set_cookie("emplog_id", str(emplog_id))
            response.set_cookie("emplog_type", str(emplog.type))
            return response
        else:
            response = make_response(render_template('MakePerfume.html', employee=emp, employeelogin=emplog, error=1))
            response.set_cookie("emp_id", str(emp_id))
            response.set_cookie("emplog_id", str(emplog_id))
            response.set_cookie("emplog_type", str(emplog.type))
            return response
    elif ProductID == 14:
        mat_id = 7
        mat = Material.query.filter_by(mat_id = mat_id).first()
        if mat.mat_stock>0:
            perfume = Perfume.query.filter_by(ProductID = ProductID).first()
            perfume.NumberOfStock = perfume.NumberOfStock+1
            db.session.commit()
            mat.mat_stock = mat.mat_stock-1
            db.session.commit()
            response = make_response(render_template('MakePerfume.html', employee=emp, employeelogin=emplog, error=2))
            response.set_cookie("emp_id", str(emp_id))
            response.set_cookie("emplog_id", str(emplog_id))
            response.set_cookie("emplog_type", str(emplog.type))
            return response
        else:
            response = make_response(render_template('MakePerfume.html', employee=emp, employeelogin=emplog, error=1))
            response.set_cookie("emp_id", str(emp_id))
            response.set_cookie("emplog_id", str(emplog_id))
            response.set_cookie("emplog_type", str(emplog.type))
            return response
    elif ProductID == 15:
        mat_id = 9
        mat = Material.query.filter_by(mat_id = mat_id).first()
        if mat.mat_stock>0:
            perfume = Perfume.query.filter_by(ProductID = ProductID).first()
            perfume.NumberOfStock = perfume.NumberOfStock+1
            db.session.commit()
            mat.mat_stock = mat.mat_stock-1
            db.session.commit()
            response = make_response(render_template('MakePerfume.html', employee=emp, employeelogin=emplog, error=2))
            response.set_cookie("emp_id", str(emp_id))
            response.set_cookie("emplog_id", str(emplog_id))
            response.set_cookie("emplog_type", str(emplog.type))
            return response
        else:
            response = make_response(render_template('MakePerfume.html', employee=emp, employeelogin=emplog, error=1))
            response.set_cookie("emp_id", str(emp_id))
            response.set_cookie("emplog_id", str(emplog_id))
            response.set_cookie("emplog_type", str(emplog.type))
            return response
    elif ProductID == 16:
        mat_id = 11
        mat_id2 = 12
        mat = Material.query.filter_by(mat_id = mat_id).first()
        mat2 = Material.query.filter_by(mat_id = mat_id2).first()
        if mat.mat_stock>0 and mat2.mat_stock>0:
            perfume = Perfume.query.filter_by(ProductID = ProductID).first()
            perfume.NumberOfStock = perfume.NumberOfStock+1
            db.session.commit()
            mat.mat_stock = mat.mat_stock-1
            db.session.commit()
            mat2.mat_stock = mat2.mat_stock-1
            db.session.commit()
            response = make_response(render_template('MakePerfume.html', employee=emp, employeelogin=emplog, error=2))
            response.set_cookie("emp_id", str(emp_id))
            response.set_cookie("emplog_id", str(emplog_id))
            response.set_cookie("emplog_type", str(emplog.type))
            return response
        else:
            response = make_response(render_template('MakePerfume.html', employee=emp, employeelogin=emplog, error=1))
            response.set_cookie("emp_id", str(emp_id))
            response.set_cookie("emplog_id", str(emplog_id))
            response.set_cookie("emplog_type", str(emplog.type))
            return response
    elif ProductID == 17:
        mat_id = 13
        mat_id2 = 14
        mat = Material.query.filter_by(mat_id = mat_id).first()
        mat2 = Material.query.filter_by(mat_id = mat_id2).first()
        if mat.mat_stock>0 and mat2.mat_stock>0:
            perfume = Perfume.query.filter_by(ProductID = ProductID).first()
            perfume.NumberOfStock = perfume.NumberOfStock+1
            db.session.commit()
            mat.mat_stock = mat.mat_stock-1
            db.session.commit()
            mat2.mat_stock = mat2.mat_stock-1
            db.session.commit()
            response = make_response(render_template('MakePerfume.html', employee=emp, employeelogin=emplog, error=2))
            response.set_cookie("emp_id", str(emp_id))
            response.set_cookie("emplog_id", str(emplog_id))
            response.set_cookie("emplog_type", str(emplog.type))
            return response
        else:
            response = make_response(render_template('MakePerfume.html', employee=emp, employeelogin=emplog, error=1))
            response.set_cookie("emp_id", str(emp_id))
            response.set_cookie("emplog_id", str(emplog_id))
            response.set_cookie("emplog_type", str(emplog.type))
            return response
    elif ProductID == 18:
        mat_id = 5
        mat_id2 = 13
        mat = Material.query.filter_by(mat_id = mat_id).first()
        mat2 = Material.query.filter_by(mat_id = mat_id2).first()
        if mat.mat_stock>0 and mat2.mat_stock>0:
            perfume = Perfume.query.filter_by(ProductID = ProductID).first()
            perfume.NumberOfStock = perfume.NumberOfStock+1
            db.session.commit()
            mat.mat_stock = mat.mat_stock-1
            db.session.commit()
            mat2.mat_stock = mat2.mat_stock-1
            db.session.commit()
            response = make_response(render_template('MakePerfume.html', employee=emp, employeelogin=emplog, error=2))
            response.set_cookie("emp_id", str(emp_id))
            response.set_cookie("emplog_id", str(emplog_id))
            response.set_cookie("emplog_type", str(emplog.type))
            return response
        else:
            response = make_response(render_template('MakePerfume.html', employee=emp, employeelogin=emplog, error=1))
            response.set_cookie("emp_id", str(emp_id))
            response.set_cookie("emplog_id", str(emplog_id))
            response.set_cookie("emplog_type", str(emplog.type))
            return response
    elif ProductID == 19:
        mat_id = 5
        mat_id2 = 6
        mat = Material.query.filter_by(mat_id = mat_id).first()
        mat2 = Material.query.filter_by(mat_id = mat_id2).first()
        if mat.mat_stock>0 and mat2.mat_stock>0:
            perfume = Perfume.query.filter_by(ProductID = ProductID).first()
            perfume.NumberOfStock = perfume.NumberOfStock+1
            db.session.commit()
            mat.mat_stock = mat.mat_stock-1
            db.session.commit()
            mat2.mat_stock = mat2.mat_stock-1
            db.session.commit()
            response = make_response(render_template('MakePerfume.html', employee=emp, employeelogin=emplog, error=2))
            response.set_cookie("emp_id", str(emp_id))
            response.set_cookie("emplog_id", str(emplog_id))
            response.set_cookie("emplog_type", str(emplog.type))
            return response
        else:
            response = make_response(render_template('MakePerfume.html', employee=emp, employeelogin=emplog, error=1))
            response.set_cookie("emp_id", str(emp_id))
            response.set_cookie("emplog_id", str(emplog_id))
            response.set_cookie("emplog_type", str(emplog.type))
            return response
    else:
        mat_id = 2
        mat_id2 = 14
        mat = Material.query.filter_by(mat_id=mat_id).first()
        mat2 = Material.query.filter_by(mat_id=mat_id2).first()
        if mat.mat_stock > 0 and mat2.mat_stock > 0:
            perfume = Perfume.query.filter_by(ProductID=ProductID).first()
            perfume.NumberOfStock = perfume.NumberOfStock + 1
            db.session.commit()
            mat.mat_stock = mat.mat_stock - 1
            db.session.commit()
            mat2.mat_stock = mat2.mat_stock - 1
            db.session.commit()
            response = make_response(render_template('MakePerfume.html', employee=emp, employeelogin=emplog, error=2))
            response.set_cookie("emp_id", str(emp_id))
            response.set_cookie("emplog_id", str(emplog_id))
            response.set_cookie("emplog_type", str(emplog.type))
            return response
        else:
            response = make_response(render_template('MakePerfume.html', employee=emp, employeelogin=emplog, error=1))
            response.set_cookie("emp_id", str(emp_id))
            response.set_cookie("emplog_id", str(emplog_id))
            response.set_cookie("emplog_type", str(emplog.type))
            return response

@app.route('/buy_perfume')
def buy_perfume():
    cus_id = int(request.cookies.get('cus_id'))
    cuslog_id = int(request.cookies.get('cuslog_id'))
    cus = Customer.query.filter_by(cus_id=cus_id).first()
    cus_log = CustomerLogin.query.filter_by(customerID = cuslog_id).first()
    id=request.args.get('id')
    ProductID = int(id)
    print("id",id)
    print("pro",ProductID)
    perfume = Perfume.query.filter_by(ProductID = ProductID).first()
    count = db.session.query(Employee).count()
    random = randrange(count)+1
    carrier = Carrier.query.filter_by(memberID = random).first()
    while not carrier:
        random = randrange(count) + 1
        carrier = Carrier.query.filter_by(memberID=random).first()

    if perfume.NumberOfStock > 0:
        perfume.NumberOfStock = perfume.NumberOfStock-1
        db.session.commit()
        cus.cus_totalOrder = cus.cus_totalOrder +1
        order = Order(cus_id, carrier.memberID)
        db.session.add(order)
        db.session.commit()
        order_no = order.order_no
        orderDate = OrderDate(order_no, datetime.datetime.now())
        db.session.add(orderDate)
        db.session.commit()
        company = Company.query.filter_by(C_id = 1).first()
        company.Budget = company.Budget+perfume.Price
        db.session.commit()
        response = make_response(render_template('Page-3.html', customer=cus, customerlogin=cus_log, error=2))
        response.set_cookie("cus_id", str(cus_id))
        response.set_cookie("cuslog_id", str(cuslog_id))
        return response
    else:
        response = make_response(render_template('Page-3.html', customer=cus, customerlogin=cus_log, error=1))
        response.set_cookie("cus_id", str(cus_id))
        response.set_cookie("cuslog_id", str(cuslog_id))
        return response


if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)

