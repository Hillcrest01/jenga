from flask import Blueprint , render_template , request
from .models import User
from . import db

views = Blueprint('views' , __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/services')
def services():
    return render_template('services.html')

@views.route('/about')
def about():
    return render_template('about.html')

@views.route('/contact' , methods = ['POST' , 'GET'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        new_user = User(name = name , email = email , message = message)
        if new_user:
            db.session.add(new_user)
            db.session.commit()
            print('comments added successfully')

        else:
            print('user not added')

    return render_template('contact.html')