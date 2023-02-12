from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'MY-SECRET-KEY'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    # Initializing SQLAlchemy
    db.init_app(app)    

    # Initializing flask login manager
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app=app)

    # Registering blueprints
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .views import view as view_blueprint
    app.register_blueprint(view_blueprint)

    # Import Models
    from .models import User

    # Loads the user from DB with the userID present in session cookie
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

        

    return app
    