# File in charge of holding the models.
from . import db
from sqlalchemy.sql import func #enables SQL to handle the date column.
from flask_login import UserMixin #gives users ability to log in


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    
    id=db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(150),unique=True)
    # Unique true ensures no two users can have the same emails
    password=db.Column(db.String(150))
    first_name=db.Column(db.String(150))
    
class Comment(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    data=db.Column(db.String(10000))
    date=db.Column(db.DateTime(timezone=True),default=func.now())
    # Relationship between the user and comment
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))


