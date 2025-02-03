from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp, ValidationError
import re

EXISTING_USERNAMES = ['john_doe', 'jane_smith']

