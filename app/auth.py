# file in charge of holding authentications
# File in charge of holding routes 
from  flask import Blueprint,render_template

auth = Blueprint('auth',__name__)


@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html" ,text="Hello new user :)") 
