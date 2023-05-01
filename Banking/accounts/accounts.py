import math
import datetime
from flask import Blueprint, flash, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from sql.db import DB
from accounts.forms import CreateAccountForm, DepositWithdrawForm
from werkzeug.datastructures import MultiDict
accounts = Blueprint('accounts', __name__, url_prefix='/accounts',template_folder='templates')

def refresh_account(account_id):
    b = DB.selectAll("SELECT SUM(balance_change) as balance FROM IS601_Transactions WHERE account_src=%s", account_id)
    balance = None
    if b.status and b.rows:
        balance = float(b.rows[0]['balance'])
    if balance != None:
        result = DB.insertOne("UPDATE IS601_Accounts set balance = %s WHERE id = %s",
                balance, account_id)
        return balance
    return None

def expected_balance(account_id, diff):
    b = DB.selectOne("SELECT * FROM IS601_Accounts WHERE id=%s LIMIT 1", account_id)
    
    expected_balance = 0.00
    if b.status and b.row:
        expected_balance = float(b.row['balance']) + diff
    return expected_balance



@accounts.route("/create", methods=["GET","POST"])
@login_required
def create():
    user_id = current_user.get_id()
    form = CreateAccountForm()  
    if form.validate_on_submit():
        try:

            result = DB.insertOne("INSERT INTO IS601_Accounts (account_type, creation_date, balance, user_id) VALUES (%s, %s, %s, %s)",
                form.acc_type.data, form.creation_date.data, 0, user_id)

            # Option 2: Generate the number based on the id column;
            # requires inserting a null first to get the last insert id, then
            # update the record immediately after

            user_account = DB.selectOne("SELECT id FROM IS601_Accounts WHERE user_id=%s AND account_type=%s", user_id, form.acc_type.data)
            if user_account.status and user_account.row:
                user_account_id = user_account.row['id']
                acc_number = str(user_account_id).zfill(12)
                result = DB.insertOne("UPDATE IS601_Accounts set account_number = %s WHERE id = %s",
                acc_number, user_account_id)

            src_expected_total = expected_balance(-1, form.funds.data*-1)
            trans1 = DB.insertOne("INSERT INTO IS601_Transactions (account_src, account_dest, balance_change, expected_total, transaction_type, memo) VALUES (%s, %s, %s, %s, %s, %s)",
            -1, user_account_id, form.funds.data*-1, src_expected_total, "Deposit", "")

            dst_expected_total = expected_balance(acc_number, form.funds.data)
            trans2 = DB.insertOne("INSERT INTO IS601_Transactions (account_src, account_dest, balance_change, expected_total, transaction_type, memo) VALUES (%s, %s, %s, %s, %s, %s)",
            user_account_id, -1, form.funds.data, dst_expected_total, "Deposit", "")

            refresh_account(-1)
            refresh_account(user_account_id)

            if result.status:
                flash(f"Created {form.acc_type.data} account", "success")

            return redirect(url_for("accounts.list"))
        except Exception as e:
            flash(f"Error creating account - {e}", "danger")
    return render_template("account_form.html", form=form, type="Create")



@accounts.route("/list", methods=["GET"])
@login_required
def list():
    user_id = current_user.get_id()
    rows = [] 
    try:
        result = DB.selectAll("SELECT account_number, account_type, modified, balance FROM IS601_Accounts WHERE user_id=%s LIMIT 5", user_id)
        if result.status and result.rows:
            rows = result.rows
    except Exception as e:
        print(e)
        flash("Error getting accounts", "danger")
    return render_template("accounts_list.html", rows=rows)



@accounts.route("/transactions", methods=["GET"])
@login_required
def transactions():
    user_id = current_user.get_id()
    acc_number = request.args.get("acc_number")
    page = request.args.get('page', 1, type=int)
    items_per_page = 10
    start_date = request.args.get('start_date', '' )
    end_date = request.args.get('end_date', '' )
    transaction_type = request.args.get('transaction_type', '' )

    account = {}
    try:
        result = DB.selectOne("SELECT id, account_number, account_type, creation_date, modified, balance FROM IS601_Accounts WHERE account_number=%s AND user_id=%s LIMIT 1", acc_number, user_id)
        if result.status and result.row:
            account = result.row
    except Exception as e:
        print(e)
        flash("Error getting account", "danger")

    rows = [] 
    try:
        query = f"SELECT (SELECT account_number FROM IS601_Accounts WHERE id=transactions.account_src) as account_src, (SELECT account_number FROM IS601_Accounts WHERE id=transactions.account_dest) as  account_dest, transaction_type, balance_change, expected_total, created FROM IS601_Transactions transactions WHERE account_src={account['id']}"

        if start_date != '':
            query += f" AND created >= '{start_date}'"

        if end_date != '':
            query += f" AND created <= '{end_date}'"

        if transaction_type != '':
            query += f" AND transaction_type LIKE '{transaction_type}'"

        query += f" ORDER BY id DESC LIMIT 100"

        print(query)
        result = DB.selectAll(query)
        if result.status and result.rows:
            rows = result.rows
    except Exception as e:
        print(e)
        flash("Error getting account transactions", "danger")

    start_pos = 0 if page == 1 else items_per_page * (page - 1) 
    pages = math.ceil(len(rows)/10)
    rows = rows[start_pos: start_pos + items_per_page]
    return render_template("transactions_list.html", rows=rows, pages=pages, current_page=page, account=account)



@accounts.route("/deposit", methods=["GET","POST"])
@login_required
def deposit():
    user_id = current_user.get_id()
    rows = [] 
    try:
        result = DB.selectAll("SELECT id, account_number, account_type, modified, balance FROM IS601_Accounts WHERE user_id=%s LIMIT 100", user_id)
        if result.status and result.rows:
            rows = result.rows
    except Exception as e:
        print(e)

    form = DepositWithdrawForm(accounts=rows)
    if form.validate_on_submit():
        try:
            acc_id = form.account.data
            src_expected_total = expected_balance(-1, form.funds.data*-1)
            trans1 = DB.insertOne("INSERT INTO IS601_Transactions (account_src, account_dest, balance_change, expected_total, transaction_type, memo) VALUES (%s, %s, %s, %s, %s, %s)",
            -1, acc_id, form.funds.data*-1, src_expected_total, "Deposit", form.memo.data)

            dst_expected_total = expected_balance(acc_id, form.funds.data)
            trans2 = DB.insertOne("INSERT INTO IS601_Transactions (account_src, account_dest, balance_change, expected_total, transaction_type, memo) VALUES (%s, %s, %s, %s, %s, %s)",
            acc_id, -1, form.funds.data, dst_expected_total, "Deposit", form.memo.data)

            refresh_account(-1)
            refresh_account(acc_id)
            form = DepositWithdrawForm(accounts=rows)
            flash(f"Successfully deposited ${form.funds.data}", "success")
        except Exception as e:
            flash(f"Error depositing into account - {e}", "danger")
    return render_template("deposit_withdraw_form.html", form=form, type="Deposit")



@accounts.route("/withdraw", methods=["GET","POST"])
@login_required
def withdraw():
    user_id = current_user.get_id()
    rows = [] 
    try:
        result = DB.selectAll("SELECT id, account_number, account_type, modified, balance FROM IS601_Accounts WHERE user_id=%s LIMIT 100", user_id)
        if result.status and result.rows:
            rows = result.rows
    except Exception as e:
        print(e)

    form = DepositWithdrawForm(accounts=rows)
    if form.validate_on_submit():
        try:
            acc_id = form.account.data
            src_expected_total = expected_balance(acc_id, form.funds.data*-1)
            if src_expected_total < 0:
                flash("Amount being withdrawn exceeds balance!", "danger")
                return render_template("deposit_withdraw_form.html", form=form, type="Withdraw")

            trans1 = DB.insertOne("INSERT INTO IS601_Transactions (account_src, account_dest, balance_change, expected_total, transaction_type, memo) VALUES (%s, %s, %s, %s, %s, %s)",
            acc_id, -1, form.funds.data*-1, src_expected_total, "Withdraw", form.memo.data)

            dst_expected_total = expected_balance(-1, form.funds.data)
            trans2 = DB.insertOne("INSERT INTO IS601_Transactions (account_src, account_dest, balance_change, expected_total, transaction_type, memo) VALUES (%s, %s, %s, %s, %s, %s)",
            -1, acc_id, form.funds.data, dst_expected_total, "Withdraw", form.memo.data)

            # Calculate what the expected total would be for each account of the transaction pair
            refresh_account(-1)
            refresh_account(acc_id)

            form = DepositWithdrawForm(accounts=rows)
            flash(f"Successfully withdrew ${form.funds.data}", "success")
        except Exception as e:
            flash(f"Error withdrawing from account - {e}", "danger")
    return render_template("deposit_withdraw_form.html", form=form, type="Withdraw")