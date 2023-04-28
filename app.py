from flask import Flask;
from flask import render_template;
app= Flask(__name__)
from flask import request
from flask import Flask,redirect,url_for,render_template,request
app= Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

# @app.route("/")
# def home():
#     return render_template('index.html')
# @app.route("/signup")
# def signup():
#     return render_template('signup.html')
# @app.route('/login',methods = ['POST'])  
# def login():  
#       uname=request.form['uname']  
#       passwrd=request.form['pass']  
#       print(uname,passwrd) 
#       return render_template('loggedin.html',result={'email':uname,'password':passwrd})
# if __name__=='__main__' :
#      app.run()

if __name__=='__main__':
    app.run(debug=True)
