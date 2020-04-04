from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, RadioField, SelectField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
    fname = StringField('Firstname', validators=[DataRequired()])
    lname = StringField('Lastname', validators=[DataRequired()])
    dob = DateField('Date of Birth', validators=[DataRequired()], format='%d-%m-%Y')
    gender = RadioField("Gender", choices = [('Male','Male'),('Female','Female')], validators=[DataRequired()])
    stud_work = SelectField("Current Status", choices=[('Student','Student'),('Working Professional','Working Professional')], validators=[DataRequired()])
    mobile = StringField('Mobile Number', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(),Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm', message='Passwords Do Not Match!')])
    pass_confirm = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register!')

    def check_email(self, field):
        # Check if not None for that user email!
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')

    def check_username(self, field):
        # Check if not None for that username!
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Sorry, that username is taken!')
