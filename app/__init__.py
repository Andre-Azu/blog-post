from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db=SQLAlchemy()
DB_NAME="database.db"

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{DB_NAME}'
    #initialize database
    db.init_app(app)
        
    from .views import views
    from .auth import auth

    # To register the paths
    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')

    
    return app