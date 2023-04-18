from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
import pycountry

company = Blueprint('company', __name__, url_prefix='/company')

@company.route("/search", methods=["GET"])
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve id, name, address, city, country, state, zip, website, employee count as employees for the company
    # don't do SELECT *
    #vp645 Date 8/14/2023
    
    query = '''select c.id, c.name, c.address, c.city, c.country, c.state, c.zip, c.website, count(e.id) as employees
            from IS601_MP3_Companies as c
            left join IS601_MP3_Employees as e on e.company_id = c.id
            where 1=1
            '''
    args = {} # <--- add values to replace %s/%(named)s placeholders
    allowed_columns = ["name", "city", "country", "state"]
    # TODO search-2 get name, country, state, column, order, limit request args
    # TODO search-3 append a LIKE filter for name if provided
    # TODO search-4 append an equality filter for country if provided
    # TODO search-5 append an equality filter for state if provided
    # TODO search-6 append sorting if column and order are provided and within the allows columsn and allowed order asc,desc
    # TODO search-7 append limit (default 10) or limit greater than 1 and less than or equal to 100
    # TODO search-8 provide a proper error message if limit isn't a number or if it's out of bounds
    #vp645 Date 8/14/2023

    limit = 10 # TODO change this per the above requirements
    if request.args.get('name'):
        name = request.args.get('name')
        query += " and name like %(name)s"
        args['name'] = "%"+name+"%"
    if request.args.get('country'):
        country = request.args.get('country')
        query += " and country = %(country)s"
        args['country'] = country
    if request.args.get('state'):
        state = request.args.get('state')
        query += " and state = %(state)s"
        args['state'] = state
    templimit = int(request.args.get('limit', 10))
    if templimit and (templimit >= 10 and templimit <= 100):
        limit = templimit
    else:
        flash("Limit should be between 10 and 100", "warning")
    query += " group by c.id"
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
        #print(f"result {result.rows}")
        if result.status:
            rows = result.rows
            #print(f"rows {rows}")
    except Exception as e:
        # TODO search-9 make message user friendly
        #vp645 Date 8/14/2023
        print(str(e))
        flash("Something went wrong, please try again later", "danger")
    # hint: use allowed_columns in template to generate sort dropdown
    # hint2: convert allowed_columns into a list of tuples representing (value, label)
    # do this prior to passing to render_template, but not before otherwise it can break validation
    allowed_columns = list(zip(allowed_columns,allowed_columns))
    return render_template("list_companies.html", rows=rows, allowed_columns=allowed_columns)

@company.route("/add", methods=["GET","POST"])
def add():
    form = {}
    if request.method == "POST":
        # TODO add-1 retrieve form data for name, address, city, state, country, zip, website
        #vp645 Date 8/14/2023
        '''

            # TODO add-2 name is required (flash proper error message)
            # TODO add-3 address is required (flash proper error message)
            # TODO add-8 zipcode is required (flash proper error message)

            # TODO add-4 city is required (flash proper error message)
            # TODO add-5 state is required (flash proper error message)
            # TODO add-5a state should be a valid state mentioned in pycountry for the selected state
            # hint see geography.py and pycountry documentation
            # TODO add-6 country is required (flash proper error message)
            # TODO add-6a country should be a valid country mentioned in pycountry
            # hint see geography.py and pycountry documentation
            # TODO add-7 website is not required
            # note: call zip variable zipcode as zip is a built in function it could lead to issues
        '''
        
        companyname = request.form.get('name', "")
        companyaddress = request.form.get('address', "")
        country = request.form.get('country', "")
        state = request.form.get('state', "")
        city = request.form.get('city', "")
        companyzipcode = request.form.get('zip', "")
        companywebsite = request.form.get('website', "")
        
        has_error = False # use this to control whether or not an insert occurs

        if companyname == "":
            flash("Company Name Required", "warning")
            has_error = True
        if companyaddress == "":
            flash("Company Address Required", "warning")
            has_error = True
        if country == "" or pycountry.countries.get(alpha_2=country) == None:
            flash("Invalid Country Name", "warning")
            has_error = True
        if state == "":
            flash("Invalid State Name", "warning")
            has_error = True
        if city == "":
            flash("City Name Required", "warning")
            has_error = True
        if companyzipcode == "":
            flash("Company Zipcode Required", "warning")
            has_error = True
        
        if not has_error:
            try:
                result = DB.insertOne("""
                INSERT INTO IS601_MP3_Companies(name,address,city,country,state,zip,website)
                VALUES(%s,%s,%s,%s,%s,%s,%s)
                """, companyname, companyaddress, city, country, state, companyzipcode, companywebsite) # <-- TODO add-8 add query and add arguments
                if result.status:
                    flash("Added Company", "success")
            except Exception as e:
                # TODO add-9 make message user friendly
                #vp645 Date 8/14/2023
                print(str(e))
                flash("Something wen't wrong, please try again later", "danger")
        form = request.form
    return render_template("add_company.html", form=form)

@company.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    try:
        id = request.args['id']
    except:
        id = ""
    if id == "": # TODO update this for TODO edit-1
        #vp645 Date 8/14/2023
        flash("No Company Id Availble.", "warning")
        return redirect(url_for('company.search'))
    else:
        if request.method == "POST":
            data = {"id": id} # use this as needed, can convert to tuple if necessary
            # TODO edit-1 retrieve form data for name, address, city, state, country, zip, website
            # TODO edit-2 name is required (flash proper error message)
            # TODO edit-3 address is required (flash proper error message)
            # TODO edit-4 city is required (flash proper error message)
            # TODO edit-5 state is required (flash proper error message)
            # TODO edit-5a state should be a valid state mentioned in pycountry for the selected state
            # hint see geography.py and pycountry documentation
            # TODO edit-6 country is required (flash proper error message)
            # TODO edit-6a country should be a valid country mentioned in pycountry
            # hint see geography.py and pycountry documentation
            # TODO edit-7 website is not required
            # TODO edit-8 zipcode is required (flash proper error message)

            #vp645 Date 8/12/2023
            
            companyname = request.form.get('name', "")
            companyaddress = request.form.get('address', "")
            country = request.form.get('country', "")
            state = request.form.get('state', "")
            city = request.form.get('city', "")
            companyzipcode = request.form.get('zip', "")
            companywebsite = request.form.get('website', "")

            data['name'] = companyname
            data['address'] = companyaddress
            data['country'] = country
            data['state'] = state
            data['city'] = city
            data['zip'] = companyzipcode
            data['website'] = companywebsite

            # note: call zip variable zipcode as zip is a built in function it could lead to issues
            # populate data dict with mappings
            has_error = False # use this to control whether or not an insert occurs
            #vp645 Date 8/12/2023

            if companyname == "":
                flash("Company Name Required", "warning")
                has_error = True
            if companyaddress == "":
                flash("Company Address Required", "warning")
                has_error = True
            if country != "" and pycountry.countries.get(alpha_2=country) == None:
                flash("Invalid Country Name", "warning")
                has_error = True
            if state == "":
                flash("Invalid State Name", "warning")
                has_error = True
            if city == "":
                flash("City Name Required", "warning")
                has_error = True
            if companyzipcode == "":
                flash("Company Zipcode Required", "warning")
                has_error = True

            if not has_error:
                try:
                    # TODO edit-9 fill in proper update query
                    # name, address, city, state, country, zip, website
                    #vp645 Date 8/14/2023
                    result = DB.update("""
                    UPDATE IS601_MP3_Companies
                    SET name=%s, address=%s, country=%s, state=%s, city=%s, zip=%s, website=%s where id=%s""", companyname, companyaddress, country, state, city, companyzipcode, companywebsite, id)
                    if result.status:
                        flash("Updated record", "success")
                except Exception as e:
                    # TODO edit-10 make this user-friendly
                    flash(e, "danger")
        row = {}
        try:
            # TODO edit-11 fetch the updated data
            result = DB.selectOne("SELECT name, address, city, country, state, zip, website FROM IS601_MP3_Companies WHERE id=%s", id)
            if result.status and result.row:
                row = result.row
            else:
                flash("No Company Data Available.", "warning")
                return redirect(url_for('company.search'))
                
        except Exception as e:
            # TODO edit-12 make this user-friendly
            print(str(e))
            flash("Something wen't wrong, please try again later", "danger")
    # TODO edit-13 pass the company data to the render template
    #vp645 Date 8/12/2023
    return render_template("edit_company.html", company=row)

@company.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 delete company by id (unallocate any employees see delete-5)
    # TODO delete-2 redirect to company search
    # TODO delete-3 pass all argument except id to this route
    # TODO delete-4 ensure a flash message shows for successful delete
    # TODO delete-5 for all employees assigned to this company set their company_id to None/null
    # TODO delete-6 if id is missing, flash necessary message and redirect to search
    #vp645 Date 8/12/2023
    try:
        id = request.args['id']
    except:
        id = ""
    if id != "":
        try:
            result = DB.update("""UPDATE IS601_MP3_Employees SET company_id=null where company_id=%s""", id)
            if result.status:
                result = DB.delete(""" DELETE FROM IS601_MP3_Companies where id=%s """, id)
                if result.status:
                    flash("Company Data Deleted", "success")
        except Exception as e:
            # TODO edit-12 make this user-friendly
            flash("Something wen't wrong, please try again later", "danger")
    else:
        flash("No Id Found", "warning")
    return redirect(url_for('company.search'))
    