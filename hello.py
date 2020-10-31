from flask import Flask, render_template, url_for, flash, redirect
from forms import Registrationform, Loginform
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Text

app = Flask(__name__)
app.config["SECRET_KEY"] = '7bfbfd13359d702c4d340a1aedf5fd74'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:/// site.db"
db = SQLAlchemy(app)


class User(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True, nullable=False)
    Email = Column(String(120), unique=True, nullable=False)
    image_file = Column(String(20), nullable=False, default="default")
    password = Column(String(60), nullable=False)
    posts = relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"user('{self.username}','{self.Email}','{self.image_file}')"


class Post(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
 #   date_posted = Column(datetime, nullable=False, default=datetime.utcnow)
    content = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}'"


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


if __name__ == '__main__':
    app.run(debug=True)
