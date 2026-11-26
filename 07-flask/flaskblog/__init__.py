#we are creating teh packages to avoid problems and load easily
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
import os

app= Flask(__name__)
app.config['SECRET_KEY']='c2ebb04d945a3e53de0c457177f88eb0' # this is basically for avoiding the cross-site request,protect against modifying cookies
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app) #creating the database instance
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER']='smtp.googlemail.com'
app.config['MAIL_PORT']=587
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USERNAME']=os.environ.get('MAIL_USE')
app.config['MAIL_PASSWORD']=os.environ.get('MAIL_PASS')
mail = Mail(app)

from flaskblog import routes