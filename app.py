import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

# Initialize SQLAlchemy
db = SQLAlchemy()

def create_app(config_name=None):
    """Application factory"""
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')
    
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize database
    db.init_app(app)
    
    with app.app_context():
        # Create instance folder if it doesn't exist
        instance_path = os.path.join(os.path.dirname(__file__), 'instance')
        os.makedirs(instance_path, exist_ok=True)
        
        # Create database tables
        db.create_all()
    
    # Register blueprints
    from routes.home import home_bp
    from routes.kontakt import kontakt_bp
    
    app.register_blueprint(home_bp)
    app.register_blueprint(kontakt_bp)
    
    return app

# Create app instance for production
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
