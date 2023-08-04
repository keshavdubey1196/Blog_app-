from flask import Flask
from dotenv import load_dotenv
import os
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from flask_bcrypt import Bcrypt


load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt=Bcrypt(app)

# migrate=Migrate(app,db)

from app import views
