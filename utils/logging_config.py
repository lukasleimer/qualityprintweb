"""
Logging Configuration and Utilities
"""
import logging
import logging.handlers
import os
from datetime import datetime


def setup_logging(app):
    """
    Configure logging for the Flask application
    
    Args:
        app: Flask application instance
    """
    
    # Create logs directory if it doesn't exist
    logs_dir = os.path.join(os.path.dirname(__file__), '..', 'logs')
    os.makedirs(logs_dir, exist_ok=True)
    
    # File handler - logs all messages
    file_handler = logging.handlers.RotatingFileHandler(
        os.path.join(logs_dir, 'app.log'),
        maxBytes=10485760,  # 10MB
        backupCount=10
    )
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    
    # Error file handler - logs only errors and above
    error_handler = logging.handlers.RotatingFileHandler(
        os.path.join(logs_dir, 'errors.log'),
        maxBytes=10485760,  # 10MB
        backupCount=5
    )
    error_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    error_handler.setLevel(logging.ERROR)
    
    # Apply handlers
    app.logger.addHandler(file_handler)
    app.logger.addHandler(error_handler)
    
    # Set minimum log level based on environment
    if app.config.get('DEBUG'):
        app.logger.setLevel(logging.DEBUG)
    else:
        app.logger.setLevel(logging.INFO)
    
    app.logger.info('Application logging initialized')


def log_form_error(form, user_email=None):
    """
    Log form validation errors
    
    Args:
        form: WTForms form object
        user_email: Optional user email for tracking
    """
    from flask import current_app
    
    errors = []
    for field, field_errors in form.errors.items():
        for error in field_errors:
            errors.append(f"{field}: {error}")
    
    error_msg = f"Form validation errors - {'; '.join(errors)}"
    if user_email:
        error_msg += f" [User: {user_email}]"
    
    current_app.logger.warning(error_msg)


def log_form_submission(name, email, subject):
    """
    Log successful form submission
    
    Args:
        name: Submitter name
        email: Submitter email
        subject: Form subject
    """
    from flask import current_app
    current_app.logger.info(f"Form submitted - Name: {name}, Email: {email}, Subject: {subject}")


def log_email_error(recipient, subject, error):
    """
    Log email sending errors
    
    Args:
        recipient: Email recipient
        subject: Email subject
        error: Error message
    """
    from flask import current_app
    current_app.logger.error(f"Email error - Recipient: {recipient}, Subject: {subject}, Error: {error}")
