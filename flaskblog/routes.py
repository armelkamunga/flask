from flaskblog.models import User, Post
from flask import render_template, url_for, flash, redirect
from flaskblog.forms import Registrationform, Loginform
from flaskblog import app


posts = [
    {"author": " Armel kamunga ",
     "title": "Blog post 1",
     "content": "First post content",
     "date_posted": "october 21, 2020"

     },
    {"author": " Tback ",
     "title": "Blog post 2",
     "content": "second post content",
     "date_posted": "october 25, 2020"

     }

]


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", posts=posts)


@app.route('/about')
def about():
    return render_template("about.html", title="about")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = Registrationform()
    if form.validate_on_submit():
        flash(f"account created for {form.username.data}!", 'success')
        return redirect(url_for('home'))

    return render_template("register.html", title="register", form=form)


@app.route('/login')
def login():
    form = Loginform()
    return render_template("login.html", title="login", form=form)

