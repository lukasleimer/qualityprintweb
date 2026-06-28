import os
import logging
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import config
from utils.logging_config import setup_logging
from utils.security import generate_secure_headers

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
    
    # Setup logging
    setup_logging(app)
    
    # Add security headers
    generate_secure_headers(app)
    
    with app.app_context():
        # Create instance folder if it doesn't exist
        instance_path = os.path.join(os.path.dirname(__file__), 'instance')
        os.makedirs(instance_path, exist_ok=True)
        
        try:
            # Create database tables
            db.create_all()
        except Exception as e:
            app.logger.warning(f"Could not create database tables: {e}")
    
    # Register blueprints
    from routes.home import home_bp
    from routes.kontakt import kontakt_bp
    
    app.register_blueprint(home_bp)
    app.register_blueprint(kontakt_bp)
    
    # Error handlers
    @app.errorhandler(404)
    def not_found_error(error):
        """Handle 404 errors"""
        app.logger.warning(f'404 error: {error}')
        return render_template('errors/404.html'), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        """Handle 500 errors"""
        app.logger.error(f'500 error: {error}')
        db.session.rollback()
        return render_template('errors/500.html'), 500
    
    @app.errorhandler(403)
    def forbidden_error(error):
        """Handle 403 errors"""
        app.logger.warning(f'403 error: {error}')
        return render_template('errors/404.html'), 403
    
    @app.shell_context_processor
    def make_shell_context():
        """Add database object to shell context"""
        return {'db': db}
    
    return app

# Create app instance for production
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
