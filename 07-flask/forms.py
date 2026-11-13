from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo
#here we  create the classes for each forms

class RegisterForm(FlaskForm):
    #here we have the form fields and imported classes
    username=StringField('Username',
                        validators=[DataRequired(),Length(min=2,max=20)])   #under the string-field arguments are name & validators (condition when filling)
    email = StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    DOB=StringField('Date Of Birth',validators=[DataRequired()])
    submit=SubmitField('Sign up')

class LoginForm(FlaskForm):
    #we can either use email or username for logging in
    email = StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    remember_me=BooleanField('Remember Me') #this will keep user logged in for some time when browser is closed
    submit=SubmitField('Login')