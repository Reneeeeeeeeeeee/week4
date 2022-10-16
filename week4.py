from flask import Flask, url_for
from flask import render_template
from flask import request
from requests import post
from flask import redirect
from flask import session
app=Flask(__name__,static_folder="static",static_url_path="/", template_folder="templates")
app.secret_key="secret"
@app.route("/", methods=["GET"])
def week4():
    return render_template("week4.html")         
@app.route("/member")
def member():
    session["account"]="signin"
    return render_template("member.html")
@app.route("/signout")
def signout():
    session.pop("account",None)
    return render_template("week4.html")
@app.route("/error")
def error():
    message= request.args.get("message")
    if message == "Empty":
        return render_template("week4.html")
    else:
        return render_template("error.html")   
@app.route("/signin", methods=["POST"])
def signin():
    account= request.form["account"]
    password= request.form["password"]
    if (account=="test" and password=="test"):
        session["account"]= "signin"
        return redirect("/member")
    elif (not account) or (not password):
        return redirect(url_for('error',message="Empty"))
    else:
        return redirect(url_for('error', message="Incorrect")) 
@app.route('/calculate')
def calculate():
    number=request.args.get("number")
    number=int(number)
    #result=square*square
    return redirect(url_for('square',num=number))
@app.route("/square/<num>")
def square(num):
    num=int(num)
    result=num*num
    return render_template("ans.html", data=result)

app.run(port=3000)