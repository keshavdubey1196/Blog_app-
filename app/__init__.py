from flask import Flask
from dotenv import load_dotenv
import os
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ['EMAIL_USER']
app.config['MAIL_PASSWORD'] = os.environ['EMAIL_PASS']



db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
mail = Mail(app)

# migrate=Migrate(app,db)

from app import views
