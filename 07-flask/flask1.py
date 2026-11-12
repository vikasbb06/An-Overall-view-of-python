from flask import Flask,render_template,url_for
import datetime
app= Flask(__name__)

posts=[
    {
        "author": "Vikas Bhat",
        "title": "My first post",
        "content": "This is my first post",
        "date_posted": datetime.date.today()
    },
    {
        "author": "Mytri Bhat",
        "title": "My second post",
        "content": "This is my second post",
        "date_posted": datetime.date.today()
    }
]

@app.route("/") # a home page or we can write as home
def hello():
    return render_template('home.html', posts=posts)

# app.route("/home")
# def home():
#     return "<h1>Home Page</h1>"

#we can add more web-page by adding just about decorator
@app.route("/about")
def about():
    return render_template('about.html',title='About')

if __name__ == "__main__": #there are 2 types for running a file 1.by creating a variable in terminal
    # 2.by instantiating as we done here
    app.run(debug=True)
