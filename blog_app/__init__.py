from flask import Flask
from flask_admin import Admin

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'mysecret'

admin = Admin(app, name='app',url='/admin_interface')
login = LoginManager(app)

from blog_app import route,admin
