from flask import Blueprint, render_template

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
