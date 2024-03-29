import datetime
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SelectField, SubmitField, DateField, FloatField, StringField
from wtforms.validators import DataRequired, NumberRange, InputRequired

#v645 Date 05/02/2023
class CreateAccountForm(FlaskForm):
    acc_type_choices = [('Checking', 'Checking Account'), ('Savings', 'Savings Account'), ('Fixed Deposit', 'Fixed Deposit Account'), ('Money Market', 'Money Market Account'), ('Certificates of Deposit', 'Certificates of Deposit Account')]
    acc_type = SelectField("Account Type", choices=acc_type_choices, validators=[DataRequired()])
    creation_date = DateField("Date", validators=[InputRequired()])
    funds = FloatField("Initial Deposit funds", validators=[InputRequired(),NumberRange(min=5)])
    submit = SubmitField("Create")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.creation_date.data:
            self.creation_date.data = datetime.date.today()

#v645 Date 05/02/2023
class DepositWithdrawForm(FlaskForm):
    account = SelectField("Account", choices=[], validators=[DataRequired()])
    funds = FloatField("Funds", validators=[InputRequired(),NumberRange(min=1)])
    memo = TextAreaField ("Memo", validators=[])
    submit = SubmitField("Submit")

    def __init__(self, accounts=None):
        super().__init__()  # calls the base initialisation and then...
        if accounts: 
            self.account.choices = [(c['id'], f"{c['account_type']} Account - {c['account_number']}") for c in accounts]

#v645 Date 05/02/2023
class TransferForm(FlaskForm):
    account_src = SelectField("Account Source", choices=[], validators=[DataRequired()])
    account_dest = SelectField("Account Destination", choices=[], validators=[DataRequired()])
    funds = FloatField("Funds", validators=[InputRequired(),NumberRange(min=1)])
    memo = TextAreaField ("Memo", validators=[])
    submit = SubmitField("Submit")

    def __init__(self, accounts=None):
        super().__init__()  # calls the base initialisation and then...
        if accounts: 
            self.account_src.choices = [(c['id'], f"{c['account_type']} Account - {c['account_number']} - ${c['balance']}") for c in accounts]
            self.account_dest.choices = [(c['id'], f"{c['account_type']} Account - {c['account_number']} - ${c['balance']}") for c in accounts]
#v645 Date 05/02/2023
class ExtTransferForm(FlaskForm):
    account_src = SelectField("Account Source", choices=[], validators=[DataRequired()])
    last_name = StringField("Last Name")
    account_dest = StringField("Last 4 digits of destination user's account number")
    funds = FloatField("Funds", validators=[InputRequired(),NumberRange(min=1)])
    memo = TextAreaField ("Memo", validators=[])
    submit = SubmitField("Submit")

    def __init__(self, accounts=None):
        super().__init__()  # calls the base initialisation and then...
        if accounts: 
            self.account_src.choices = [(c['id'], f"{c['account_type']} Account - {c['account_number']} - ${c['balance']}") for c in accounts]