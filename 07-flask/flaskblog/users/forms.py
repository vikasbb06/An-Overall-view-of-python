from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,PasswordField,BooleanField
from wtforms.validators import DataRequired,Email,EqualTo,ValidationError,Length
from flask_wtf.file import FileAllowed,FileField
from flaskblog.models import User
from flask_login import current_user

class RegisterForm(FlaskForm):
    #here we have the form fields and imported classes
    username=StringField('Username',
                        validators=[DataRequired(),Length(min=2,max=20)])   #under the string-field arguments are name & validators (condition when filling)
    email = StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    DOB=StringField('Date Of Birth',validators=[DataRequired()])
    submit=SubmitField('Sign up')

    #we have to create a custom validation of username
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


class UpdateAccountForm(FlaskForm):
    #here we have the form fields and imported classes
    username=StringField('Username',
                        validators=[DataRequired(),Length(min=2,max=20)])   #under the string-field arguments are name & validators (condition when filling)
    email = StringField('Email',validators=[DataRequired(),Email()])
    picture=FileField('Update the profile picture',validators=[FileAllowed(['jpg','png'],'Images only!')])
    submit=SubmitField('Update')

    #we have to create a custom validation of username
    def validate_username(self,username):
        if username.data!=current_user.username:
            user=User.query.filter_by(username=username.data).first() # this will be check whether the username exist in db
            if user:
                raise ValidationError('Sorry, that username already exists')

    def validate_email(self,email):
        if email.data!=current_user.email:
            email=User.query.filter_by(email=email.data).first()
            if email:
                raise ValidationError('Sorry, that email  already exists')


class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Reset Password')