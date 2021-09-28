# file in charge of holding authentications
# File in charge of holding routes 
from  flask import Blueprint,render_template,request,flash,redirect,url_for
from .models import User
from . import db
from werkzeug.security import check_password_hash,generate_password_hash
from flask_login import login_required,login_user,logout_user,current_user

auth = Blueprint('auth',__name__)


@auth.route('/sign_up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name=request.form.get('firstName')
        password1=request.form.get('password1')
        password2=request.form.get('password2')

        # To prevent a user to sign up with the same email,
        user=User.query.filter_by(email=email).first()
        if user:
            flash("email already exists", category='error')
        # add validations/flash messages 

        elif len("email")<2:
            flash("email must be greater than two characters",category='Success')
        elif len('first_name')<3:
            flash("firstname too short",category='error')
        elif len('password')<4:
            flash('password too short',category='error')
        elif password1 != password2:
            flash("passwords dont match", category="error")
        else:
            new_user=User(email=email,password=generate_password_hash(password1, method='sha256'),first_name=first_name)
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            #add user to database
            flash('account created',category='success')
            #to redirect the user to the homepage of the website, 
            return redirect(url_for('views.home'))


    return render_template("sign_up.html" ,text="Hello new user :)",user=current_user)


@auth.route('/login')
def login():
    return render_template('login.html')
@auth.route('/logout')
def logout():
    return render_template("home.html")

