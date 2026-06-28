from flask import Blueprint, render_template, request, jsonify, current_app
from services.mail import send_contact_email
from forms import ContactForm
from app import db
from models import Message
from utils.logging_config import log_form_error, log_form_submission, log_email_error

kontakt_bp = Blueprint('kontakt', __name__, url_prefix='/kontakt')

@kontakt_bp.route('/')
def kontakt():
    """Contact page"""
    form = ContactForm()
    return render_template('kontakt.html', form=form)

@kontakt_bp.route('/send', methods=['POST'])
def send_message():
    """Send contact message with form validation"""
    try:
        form = ContactForm()
        
        # Validate form
        if not form.validate_on_submit():
            log_form_error(form, request.form.get('email'))
            return jsonify({
                'success': False,
                'errors': form.errors
            }), 400
        
        # Sanitize data
        name = form.name.data.strip()
        email = form.email.data.strip().lower()
        subject = form.subject.data.strip()
        message = form.message.data.strip()
        
        # Save to database
        contact_message = Message(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        db.session.add(contact_message)
        db.session.commit()
        
        # Log successful submission
        log_form_submission(name, email, subject)
        
        # Send email notification
        email_data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        }
        
        if not send_contact_email(email_data):
            current_app.logger.warning(f"Email sending failed for {email}, but message saved to database")
        
        return jsonify({
            'success': True,
            'message': 'Vielen Dank! Ihre Nachricht wurde erfolgreich versendet. Wir werden Sie in Kürze kontaktieren.'
        }), 200
        
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"Error processing contact form: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Ein Fehler ist aufgetreten. Bitte versuchen Sie es später erneut.'
        }), 500

