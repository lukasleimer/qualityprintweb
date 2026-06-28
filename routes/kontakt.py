from flask import Blueprint, render_template, request, jsonify
from services.mail import send_contact_email
from app import db
from models import Message

kontakt_bp = Blueprint('kontakt', __name__, url_prefix='/kontakt')

@kontakt_bp.route('/')
def kontakt():
    """Contact page"""
    return render_template('kontakt.html')

@kontakt_bp.route('/send', methods=['POST'])
def send_message():
    """Send contact message"""
    try:
        data = request.get_json()
        
        # Validation
        if not all([data.get('name'), data.get('email'), 
                   data.get('subject'), data.get('message')]):
            return jsonify({'success': False, 'error': 'Alle Felder sind erforderlich'}), 400
        
        # Save to database
        message = Message(
            name=data['name'],
            email=data['email'],
            subject=data['subject'],
            message=data['message']
        )
        db.session.add(message)
        db.session.commit()
        
        # Send email
        send_contact_email(data)
        
        return jsonify({'success': True, 'message': 'Nachricht erfolgreich versendet'}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500
