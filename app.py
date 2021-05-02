from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///users.db'
#Initializ the database
db=SQLAlchemy(app)

#create db model
class Users(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name_=db.Column(db.String(200), nullable=False)
    email_=db.Column(db.String, nullable=False, unique=True)
    age_=db.Column(db.Integer, nullable=False)
    date_created=db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, name_, email_, age_):
        self.name_=name_
        self.email_=email_
        self.age_=age_



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    if request.method=='POST':
        user= request.form["user_name"]
        email= request.form["email_name"]
        age= request.form["age"]
        print(user,email,age)
        data=Users(user,email,age)
        db.session.add(data)
        db.session.commit()
        return render_template("success.html")


if __name__ =='__main__':
    app.debug=True
    app.run()