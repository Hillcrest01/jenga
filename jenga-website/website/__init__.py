from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = 'database.db'

def create_database():
    db.create_all()
    print('database created successfully')

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'EYDVHBWE UIVHBVYUDJ'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    #we initialize the database here
    db.init_app(app)

    from .views import views

    app.register_blueprint(views , url_prefix='/')



    with app.app_context():
        create_database()
    return app