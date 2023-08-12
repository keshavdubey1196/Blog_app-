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

# app = Flask(__name__)
# app.secret_key = os.environ.get('SECRET_KEY')
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
#     'SQLALCHEMY_DATABASE_URI')
# app.config.from_object(Config)
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()

# migrate=Migrate(app,db)

# from app.users.views import users
# from app.main.views import main
# from app.posts.views import posts

# app.register_blueprint(users)
# app.register_blueprint(main)
# app.register_blueprint(posts)


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    # migrate=Migrate(app,db)

    from app.users.views import users
    from app.main.views import main
    from app.posts.views import posts

    app.register_blueprint(users)
    app.register_blueprint(main)
    app.register_blueprint(posts)

    return app
