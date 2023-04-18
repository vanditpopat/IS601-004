from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
import re

employee = Blueprint('employee', __name__, url_prefix='/employee')


@employee.route("/search", methods=["GET"])
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve employee id as id, first_name, last_name, email, company_id, company_name using a LEFT JOIN
    #vp645 Date 8/15/2023
    query = """SELECT e.id, e.first_name, e.last_name, e.email, e.company_id, IF(name is not null, name,'N/A') as company_name
    FROM IS601_MP3_Employees as e
    LEFT JOIN IS601_MP3_Companies as c on c.id = e.company_id
    WHERE 1=1"""
    args = {} # <--- add values to replace %s/%(named)s placeholders
    allowed_columns = ["first_name", "last_name", "email", "company_name"]
    # TODO search-2 get fn, ln, email, company, column, order, limit from request args
    # TODO search-3 append like filter for first_name if provided
    # TODO search-4 append like filter for last_name if provided
    # TODO search-5 append like filter for email if provided
    # TODO search-6 append equality filter for company_id if provided
    # TODO search-7 append sorting if column and order are provided and within the allowed columns and order options (asc, desc)
    # TODO search-8 append limit (default 10) or limit greater than 1 and less than or equal to 100
    # TODO search-9 provide a proper error message if limit isn't a number or if it's out of bounds
    #vp645 Date 8/15/2023
    limit = 10 # TODO change this per the above requirements
    if request.args.get('fn'):
        fn = request.args.get('fn')
        query += " and first_name like %(fn)s"
        args['fn'] = "%"+fn+"%"
    if request.args.get('ln'):
        ln = request.args.get('ln')
        query += " and last_name like %(ln)s"
        args['ln'] = "%"+ln+"%"
    if request.args.get('email'):
        email = request.args.get('email')
        query += " and email like %(email)s"
        args['email'] = "%"+email+"%"
    if request.args.get('company'):
        company_id = int(request.args.get('company'))
        query += " and company_id = %(company_id)s"
        args['company_id'] = company_id
    templimit = int(request.args.get('limit', 10))
    if templimit and (templimit >= 10 and templimit <= 100):
        limit = templimit
    templimit = int(request.args.get('limit', 10))
    if templimit and (templimit >= 10 and templimit <= 100):
        limit = templimit
    else:
        flash("Limit should be between 10 and 100", "warning")
    if request.args.get('column') and request.args.get('column') != "":
        column = request.args.get('column')
        order = request.args.get('order')
        if column in allowed_columns and order in ['asc', 'desc']:
            query += f" order by {column} {order}"
    query += " LIMIT %(limit)s"
    args["limit"] = limit
    print("query",query)
    print("args", args)
    try:
        result = DB.selectAll(query, args)
        if result.status:
            rows = result.rows
    except Exception as e:
        # TODO search-10 make message user friendly
        print(str(e))
        flash("Something wen't wrong, please try again later", "warning")
    # hint: use allowed_columns in template to generate sort dropdown
    # hint2: convert allowed_columns into a list of tuples representing (value, label)
    # do this prior to passing to render_template, but not before otherwise it can break validation
    #vp645 Date 8/15/2023
    allowed_columns = list(zip(allowed_columns,allowed_columns))    
    return render_template("list_employees.html", rows=rows, allowed_columns=allowed_columns)

@employee.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        # TODO add-1 retrieve form data for first_name, last_name, company, email
        # TODO add-2 first_name is required (flash proper error message)
        # TODO add-3 last_name is required (flash proper error message)
        # TODO add-4 company (may be None)
        # TODO add-5 email is required (flash proper error message)
        # TODO add-5a verify email is in the correct format
        #vp645 Date 8/15/2023
        first_name = request.form.get('first_name', "")
        last_name = request.form.get('last_name', "")
        email = request.form.get('email', "")
        company = request.form.get('company', None)

        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        has_error = False
        
        if first_name == "":
                flash("First Name is Required", "warning")
                has_error = True
        if last_name == "":
            flash("Last Name is Required", "warning")
            has_error = True
        if email == "":
            flash("Email is Required", "warning")
            has_error = True
        else:
            if not re.fullmatch(regex, email):
                flash("Please provide a valide email address", "warning")
                has_error = True
            
        if not has_error:
            try:
                if company == "":
                    result = DB.insertOne("""
                    INSERT INTO IS601_MP3_Employees(first_name, last_name, email)
                        VALUES(%s, %s, %s)""", first_name, last_name, email) # <-- TODO add-6 add query and add arguments
                else:
                    result = DB.insertOne("""
                    INSERT INTO IS601_MP3_Employees(first_name, last_name, email, company_id)
                    VALUES(%s, %s, %s, %s)""", first_name, last_name, email, company)
                if result.status:
                    flash("Created Employee Record", "success")
            except Exception as e:
                # TODO add-7 make message user friendly
                print(str(e))
                flash("Something went wrong, please try again later", "danger")
        else:
            form = request.form
    return render_template("add_employee.html")

@employee.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    #vp645 Date 8/15/2023
    try:
        id = request.args['id']
    except:
        id = ""
    if id == "": # TODO update this for TODO edit-1
        flash("No Company Id Availble.", "warning")
        return redirect(url_for('company.search'))
    else:
        if request.method == "POST":
            
            # TODO edit-1 retrieve form data for first_name, last_name, company, email
            # TODO edit-2 first_name is required (flash proper error message)
            # TODO edit-3 last_name is required (flash proper error message)
            # TODO edit-4 company (may be None)
            # TODO edit-5 email is required (flash proper error message)
            # TODO edit-5a verify email is in the correct format
            has_error = False # use this to control whether or not an insert occurs
            #vp645 Date 8/15/2023

            first_name = request.form.get('first_name', "")
            last_name = request.form.get('last_name', "")
            email = request.form.get('email', "")
            company = request.form.get('company', None)

            if first_name == "":
                flash("First Name is Required", "warning")
                has_error = True
            if last_name == "":
                flash("Last Name is Required", "warning")
                has_error = True
            if email == "":
                flash("Email is Required", "warning")
                has_error = True
                
            if not has_error:
                try:
                    # TODO edit-6 fill in proper update query
                    #vp645 Date 8/15/2023
                    if company == "":
                        result = DB.update("""
                                    UPDATE IS601_MP3_Employees SET first_name = %s, last_name = %s, email = %s
                                    where id = %s
                                    """, first_name, last_name, email, id)
                    else:
                        result = DB.update("""
                                    UPDATE IS601_MP3_Employees SET first_name = %s, last_name = %s, email = %s, company_id = %s
                                    where id = %s
                                    """, first_name, last_name, email, company, id)
                    if result.status:
                        flash("Updated record", "success")
                except Exception as e:
                    # TODO edit-7 make this user-friendly
                    flash("Something wen't wrong, please try again later", "danger")
        row = {}
        try:
            # TODO edit-8 fetch the updated data 
            #vp645 Date 8/15/2023
            result = DB.selectOne("""SELECT e.first_name, e.last_name, e.email, e.company_id as company FROM IS601_MP3_Employees as e WHERE e.id = %s""",id)
            if result.status and result.row:
                row = result.row
            else:
                flash("No Employee Data Available.", "warning")
                return redirect(url_for('employee.search'))
        except Exception as e:
            # TODO edit-9 make this user-friendly
            print(str(e))
            flash("Something wen't wrong, please try again later", "danger")
    # TODO edit-10 pass the employee data to the render template
    return render_template("edit_employee.html", employee=row)
@employee.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 delete employee by id
    # TODO delete-2 redirect to employee search
    # TODO delete-3 pass all argument except id to this route
    # TODO delete-4 ensure a flash message shows for successful delete
    # TODO delete-5 if id is missing, flash necessary message and redirect to search
    #vp645 Date 8/15/2023
    try:
        id = request.args['id']
    except:
        id = ""
    if id != "":
        try:
            result = DB.delete("""DELETE FROM IS601_MP3_Employees where id=%s """, id)
            if result.status:
                flash("Employee Data Deleted", "success")
        except Exception as e:
            # TODO edit-12 make this user-friendly
            flash("Something wen't wrong, please try again later", "danger")
    else:
        flash("No Id Found", "warning")
    return redirect(url_for('employee.search'))