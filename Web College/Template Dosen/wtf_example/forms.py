from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')
    
    def validate_name(self, name):
        if not name.data.isalpha():
            raise ValidationError('Name must contain only alphabetic characters (letters)')
    
# Design Interface

