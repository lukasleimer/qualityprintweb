"""
Security utilities and middleware
"""
from flask import request, current_app
from functools import wraps
import re


def generate_secure_headers(app):
    """
    Add security headers to all responses
    
    Args:
        app: Flask application instance
    """
    
    @app.after_request
    def set_security_headers(response):
        """Set security headers on every response"""
        
        # Content Security Policy - strict to prevent XSS
        response.headers['Content-Security-Policy'] = (
            "default-src 'self'; "
            "script-src 'self' 'unsafe-inline'; "
            "style-src 'self' 'unsafe-inline'; "
            "img-src 'self' data: https:; "
            "font-src 'self' data:; "
            "connect-src 'self'; "
            "frame-ancestors 'none'; "
            "base-uri 'self'; "
            "form-action 'self'"
        )
        
        # Prevent MIME type sniffing
        response.headers['X-Content-Type-Options'] = 'nosniff'
        
        # Enable XSS filter in older browsers
        response.headers['X-XSS-Protection'] = '1; mode=block'
        
        # Prevent clickjacking
        response.headers['X-Frame-Options'] = 'DENY'
        
        # Referrer policy
        response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
        
        # Permissions policy
        response.headers['Permissions-Policy'] = (
            'accelerometer=(), camera=(), geolocation=(), '
            'gyroscope=(), magnetometer=(), microphone=(), '
            'payment=(), usb=()'
        )
        
        # HSTS - only in production
        if not current_app.debug:
            response.headers['Strict-Transport-Security'] = (
                'max-age=31536000; includeSubDomains; preload'
            )
        
        return response


def validate_email(email):
    """
    Validate email format and safety
    
    Args:
        email: Email address to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not email or len(email) > 254:
        return False
    
    # Simple regex validation
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(email_pattern, email))


def sanitize_input(text, max_length=5000):
    """
    Sanitize user input to prevent injection attacks
    
    Args:
        text: Text to sanitize
        max_length: Maximum allowed length
        
    Returns:
        str: Sanitized text
    """
    if not isinstance(text, str):
        return ''
    
    # Limit length
    text = text[:max_length]
    
    # Remove control characters
    text = ''.join(char for char in text if ord(char) >= 32 or char in '\n\r\t')
    
    # Strip leading/trailing whitespace
    text = text.strip()
    
    return text


def rate_limit_key(endpoint):
    """
    Generate a rate limit key based on user IP and endpoint
    
    Args:
        endpoint: Flask endpoint name
        
    Returns:
        str: Rate limit key
    """
    # Get real IP address (handles proxies)
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    if ',' in ip:
        ip = ip.split(',')[0].strip()
    
    return f"{endpoint}:{ip}"


def get_client_ip():
    """
    Get client IP address, handling proxies
    
    Returns:
        str: Client IP address
    """
    if request.headers.get('X-Forwarded-For'):
        return request.headers.get('X-Forwarded-For').split(',')[0].strip()
    return request.remote_addr
