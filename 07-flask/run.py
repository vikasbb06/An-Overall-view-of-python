from flaskblog import app

if __name__ == "__main__": #there are 2 types for running a file 1.by creating a variable in terminal
    # 2.by instantiating as we done here
    app.run(debug=True,port=5001)
