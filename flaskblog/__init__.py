from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = '7bfbfd13359d702c4d340a1aedf5fd74'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:/// site.db"
db = SQLAlchemy(app)


from flaskblog import routes
