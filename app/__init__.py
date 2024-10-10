from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    # Set up configurations
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'supersecretkey')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///yourdatabase.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Specify the view to redirect to when the user needs to log in
    login_manager.login_view = 'login'  # 'login' should be the name of your login route
    login_manager.login_message_category = 'info'  # Category for the login required message

    # Import the User model and create the user_loader function for Flask-Login
    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        """
        This callback is used to reload the user object from the user ID stored in the session.
        """
        return User.query.get(int(user_id))

    # Register the routes (blueprints or direct imports)
    from app.routes import main  # Import your blueprint here
    app.register_blueprint(main)  # Register the blueprint

    return app

# Ensure everything is initialized properly
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

