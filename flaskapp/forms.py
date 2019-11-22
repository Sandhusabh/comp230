from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Optional

class AddressForm(FlaskForm):
    housenumber = StringField('House #', validators=[DataRequired(), Length(min=2, max=5, message="Enter a valid house number")])
    stname = StringField('Street Name', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    unit = StringField('Unit #')
    phonenumber = StringField('Phone No.', validators=[Length(min=0, max=10)])
    submit = SubmitField('Continue')
