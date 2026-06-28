from flask import Blueprint, render_template, send_file
import os

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def index():
    """Home page"""
    return render_template('home.html')

@home_bp.route('/impressum')
def impressum():
    """Impressum page"""
    return render_template('impressum.html')

@home_bp.route('/datenschutz')
def datenschutz():
    """Datenschutz page"""
    return render_template('datenschutz.html')

@home_bp.route('/sitemap.xml')
def sitemap():
    """Sitemap.xml for search engines"""
    sitemap_path = os.path.join(os.path.dirname(__file__), '..', 'static', 'sitemap.xml')
    return send_file(sitemap_path, mimetype='application/xml')

@home_bp.route('/robots.txt')
def robots():
    """Robots.txt for search engines"""
    robots_path = os.path.join(os.path.dirname(__file__), '..', 'static', 'robots.txt')
    return send_file(robots_path, mimetype='text/plain')
