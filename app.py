import os
from flask import Flask,render_template

from wtform_fields import *

from models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

#standard flask instruction set by python community to call Flask 

app=Flask(__name__)


app.secret_key='replace later'

# configuring the database

app.config['SQLALCHEMY_DATABASE_URI']='postgres://wcutqjafaveqdv:f3e6dd068c0a38eb30ae38aa93590c111ee507ef505cff0dade7cdf48626a160@ec2-52-71-55-81.compute-1.amazonaws.com:5432/dbrahmv6vb3vv4'

# Initialzie a connection to our database
db=SQLAlchemy(app)
# engine=create_engine(os.getenv("SQLALCHEMY_DATABASE_URI"))
# db1=scoped_session(sessionmaker(bind=engine))

@app.route("/", methods=['GET', 'POST'])
def index():

    reg_form = RegistrationForm()

    # Update database if validation success
    if reg_form.validate_on_submit():
        username=reg_form.username.data
        password=reg_form.password.data

        #check if user name exists
       
        #To check whether the password exists or not, not necessary here
        # user_object.password=User.query.filter_by(password=password).first()

        
        # now, we add this to our database if the data passed by user has passed all validations and is not a duplicate
        # lets create a user object with user name and password as two columns which will get added into our sql table.
        user=User(username=username,password=password)
        db.session.add(user)
        db.session.commit()
        return " Inserted into DB "

    return render_template("index.html", form=reg_form)
# @app.route("/admin")
# def admin():
#     users=db1.execute("Select username from User")
#     for i in users:
#         print(users)


if __name__ == "__main__":
    app.run(debug=True)
