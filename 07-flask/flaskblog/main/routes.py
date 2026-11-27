from flask import Blueprint,render_template,request
from flaskblog.models import Post


main = Blueprint('main',__name__)

@main.route("/")
@main.route("/home") # a home page or we can write as home
def home():
    page=request.args.get('page',1,type=int)
    posts=Post.query.order_by(Post.date_posted.desc()).paginate(page=page,per_page=5)
    return render_template('home.html', posts=posts)

# app.route("/")
# def home():
#       return "<h1>Home Page</h1>"

#we can add more web-page by adding just about decorator
@main.route("/about")
def about():
    return render_template('about.html',title='About')