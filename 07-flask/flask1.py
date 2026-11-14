from email.policy import default

from flask import Flask,render_template,url_for,flash,redirect
import datetime
from flask_sqlalchemy import SQLAlchemy
from forms import RegisterForm,LoginForm

app= Flask(__name__)
app.config['SECRET_KEY']='c2ebb04d945a3e53de0c457177f88eb0' # this is basically for avoiding the cross-site request,protect against modifying cookies
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)
#creating the database instance

class User(db.Model):
    #  now we can add columns to the table
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(20),unique=True,nullable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)
    image_file=db.Column(db.String(20),nullable=False,default='default.jpg')
    password=db.Column(db.String(60),nullable=False)
    posts=db.relationship('Post',backref='author',lazy=True) #as one author have mny blogs but vice-vers is not true
                                                                #backref similar to adding column in another classes
    def __repr__(self): # the dunder function is used for the reprsentation
        return f'User {self.username},{self.email},{self.image_file}'

class Post(db.Model): # for holding our post
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=lambda: datetime.datetime.now(datetime.timezone.utc))
    content=db.Column(db.Text,nullable=False)
    #once relationship is created b/w classes then we have to use foreign key
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self): return f'Post {self.title},{self.date_posted}'

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

if __name__ == "__main__": #there are 2 types for running a file 1.by creating a variable in terminal
    # 2.by instantiating as we done here
    app.run(debug=True,port=5001)
