"""
WSGI entry point for production deployments

Use with Gunicorn:
    gunicorn -w 4 -b 0.0.0.0:5000 wsgi:app

Or with other WSGI servers (uWSGI, etc.)
"""
import os
import logging
from app import create_app, db

# Set production environment if not specified
if 'FLASK_ENV' not in os.environ:
    os.environ['FLASK_ENV'] = 'production'

# Create application instance
app = create_app()

# Setup production-specific logging
if not app.debug and not app.testing:
    logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    # This should not be used in production
    app.run()
