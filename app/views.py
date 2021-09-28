## where users will be navigating to
# this import below says that is file is a blueprint of the application that means it has a bunch of roots and urls' inside it
# it allows us to define views in multiple files.
from flask import Blueprint,render_template,request,flash,jsonify
from flask_login import login_required,current_user
from .models import Blog
from . import db
import json

#Defining a blueprint
views = Blueprint('views',__name__)


#for the homepage
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        blog=request.form.get('blog')

        if len(blog) <=1:
            flash('Blog too short', category='error')
        else:
            new_blog = Blog(data=blog, user_id=current_user.id)
            db.session.add(new_blog)
            db.session.commit()
            flash("Blog added!", category="success")

    return render_template("home.html", user=current_user)

@views.route('/delete-blog', methods=['POST'])
def delete_blog():
    blog=json.loads(request.data) #used to take in data from post request
    blogId = blog['blogId']# used to access the blog id from he index.js
    blog=blog.query.get(blogId)
    # .get goes to find the quote
    if blog:
        if blog.user_id==current_user.id: #this line ensures its a user who deletes their own quote, not somebody else's
            db.session.delete(blog)
            db.session.commit()
            return jsonify({})
