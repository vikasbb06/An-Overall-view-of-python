from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
#fetch the details from database
from flaskblog.models import User

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

    #we have to create a custom validaation of username
    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first() # this will be check whether the username exist in db
        if user:
            raise ValidationError('Sorry, that username already exists')

    def validate_email(self,email):
        email=User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('Sorry, that email  already exists')

class LoginForm(FlaskForm):
    #we can either use email or username for logging in
    email = StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired(),EqualTo('password')])
    remember_me=BooleanField('Remember Me') #this will keep user logged in for some time when browser is closed
    submit=SubmitField('Login')