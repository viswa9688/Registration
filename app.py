from flask import Flask
from flask import render_template, request

# This represents that the website belongs to this current file.
app=Flask(__name__)
#This represents the default page of the website.
# @app.route("/")
# def index():
#     return "Hello, world!!!@#$%^^^"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello", methods=["GET","POST"])
def hello():
    if request.method=='GET':
        return "Please submit the form instead"
    else:
        name=request.form.get("name")
        return render_template("hello.html",name=name)
@app.route("/privacy.html")
def privacy():
    return render_template("privacy.html")

@app.route("/sign_in.html")
def sign_in():
    return render_template('sign_in.html')
@app.route('/sign_in.html', methods=['GET', 'POST'])
def lionel(): 
    return render_template('sign_in.html')
