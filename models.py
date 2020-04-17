from flask_sqlalchemy import SQLAlchemy


# initialzing the sql alchemy object 

db=SQLAlchemy()

# creating a class which will inherit fro sql alchemy database
class User(db.Model):
    # Users Model
    #creating or ttaching to a table already present in database
    __tablename__="users"
    id =db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(25), unique=True, nullable=False)
    password= db.Column(db.String(), nullable=False)
    
    # use this only one time. For now, lets create table from post gres directly. 
    # db.create_all()

