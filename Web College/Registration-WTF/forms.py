from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, EmailField, validators
from wtforms.validators import DataRequired, Email, EqualTo, Regexp, ValidationError

EXISTING_USERNAMES = ['john_doe', 'jane_smith']

class RegistrationForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired(), Regexp(r'^[A-Za-z\s]+$', message="Full name must contain alphabetic characters only.")])
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone_number = StringField('Phone Number', validators=[DataRequired(), Regexp(r'^(\+62|62|0)8[1-9][0-9]{6,11}$', message="Invalid Indonesian phone number.")])
    date_of_birth = DateField('Date of Birth', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Register')

    def validate_username(self, username): 
        if username.data in EXISTING_USERNAMES:
            raise ValidationError('Username already exists.')













#Another things for commit 
