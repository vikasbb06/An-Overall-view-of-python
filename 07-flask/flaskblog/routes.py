from flaskblog.models import User,Post # if we import above 'db' this will give error as deadlock situation appears
from flask import render_template,url_for,flash,redirect,request
import datetime,secrets,os
from PIL import Image
from flaskblog.forms import RegisterForm,LoginForm,UpdateAccountForm
from flaskblog import app,bcrypt,db
from flask_login import login_user, current_user, logout_user,login_required

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
#       return "<h1>Home Page</h1>"

#we can add more web-page by adding just about decorator
@app.route("/about")
def about():
    return render_template('about.html',title='About')

@app.route("/register",methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form=RegisterForm()
    if form.validate_on_submit():
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(username=form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created! and You are now able to log in ', 'success')
        return redirect(url_for('login'))
    return render_template('register.html',title='Registration',form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):#this check the password in db and entered
            login_user(user,remember=form.remember_me.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

def save_picture(form_picture):
    random_hex=secrets.token_hex(8)
    f_name,f_ext=os.path.splitext(form_picture.filename)
    picture_fn=random_hex+f_ext
    picture_path=os.path.join(app.root_path,'static/profile_pics',picture_fn)
    #we want to re-size the image , so we use PIl function
    output_size=(125,125)
    i=Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

@app.route("/account",methods=['GET','POST'])
@login_required
def account():
    form=UpdateAccountForm() #instance of the class
    #in below static is the folder name in which image is present,filename is the folder or file inside the directory
    if form.validate_on_submit():
        if form.picture.data:
            picture_fn=save_picture(form.picture.data)
        current_user.username=form.username.data()
        current_user.email=form.email.data()
        db.session.commit()  # the updation of the DB
        flash(f'Account for {current_user.username} has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method=='GET':
        form.username.data=current_user.username
        form.email.data=current_user.email
    image_file=url_for('static',filename='profile_pics/'+current_user.image_file)
    return render_template("account.html",title="Account",image_file=image_file,form=form)