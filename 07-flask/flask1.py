from flask import Flask
app= Flask(__name__)

@app.route("/") # a home page or we can write as home
def hello():
    return "<h1>Home Page</h1>"

# app.route("/home")
# def home():
#     return "<h1>Home Page</h1>"

#we can add more web-page by adding just about decorator
@app.route("/about")
def about():
    return "<h1>About Page</h1>"

if __name__ == "__main__": #there are 2 types for running a file 1.by creating a variable in terminal
    # 2.by instantiating as we done here
    app.run(debug=True)
