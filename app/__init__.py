from flask import Flask
from dotenv import load_dotenv
# import os
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from app.config import Config

load_dotenv()

app = Flask(__name__)
# app.secret_key = os.environ.get('SECRET_KEY')
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
#     'SQLALCHEMY_DATABASE_URI')
app.config.from_object(Config)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail(app)

# migrate=Migrate(app,db)

from app.users.views import users
from app.main.views import main
from app.posts.views import posts

app.register_blueprint(users)
app.register_blueprint(main)
app.register_blueprint(posts)
