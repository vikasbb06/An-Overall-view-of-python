#we are creating teh packages to avoid problems and load easily
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app= Flask(__name__)
app.config['SECRET_KEY']='c2ebb04d945a3e53de0c457177f88eb0' # this is basically for avoiding the cross-site request,protect against modifying cookies
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app) #creating the database instance
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes