from flaskblog.models import User,Post # if we import above 'db' this will give error as deadlock situation appears
from flask import render_template,url_for,flash,redirect
import datetime
from flaskblog.forms import RegisterForm,LoginForm
from flaskblog import app

posts=[
    {
        "author": "Vikas Bhat",
        "title": "My first post",
        "content": "This is my first post",
        "date_posted": datetime.date.today()
    },
    {
        "author": "Bhat",
        "title": "My second post",
        "content": "This is my second post",
        "date_posted": datetime.date.today()
    }
]
@app.route("/")
@app.route("/home") # a home page or we can write as home
def home():
    return render_template('home.html', posts=posts)

# app.route("/")
# def home():
#     return "<h1>Home Page</h1>"

#we can add more web-page by adding just about decorator
@app.route("/about")
def about():
    return render_template('about.html',title='About')

@app.route("/register",methods=['GET','POST'])
def register():
    form=RegisterForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Registration',form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)