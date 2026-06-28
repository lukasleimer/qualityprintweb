"""
Flask-WTF Form Definitions
"""
from wtforms import StringField, TextAreaField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email, Length, ValidationError
from flask_wtf import FlaskForm
import re


class ContactForm(FlaskForm):
    """Contact form with validation"""
    
    name = StringField(
        'Name',
        validators=[
            DataRequired(message='Name ist erforderlich'),
            Length(min=2, max=120, message='Name muss zwischen 2 und 120 Zeichen sein')
        ],
        render_kw={
            'placeholder': 'Ihr Name',
            'autocomplete': 'name',
            'required': True
        }
    )
    
    email = EmailField(
        'Email',
        validators=[
            DataRequired(message='Email ist erforderlich'),
            Email(message='Gültige Email-Adresse erforderlich')
        ],
        render_kw={
            'placeholder': 'ihre.email@example.com',
            'autocomplete': 'email',
            'required': True
        }
    )
    
    subject = StringField(
        'Betreff',
        validators=[
            DataRequired(message='Betreff ist erforderlich'),
            Length(min=5, max=200, message='Betreff muss zwischen 5 und 200 Zeichen sein')
        ],
        render_kw={
            'placeholder': 'Wie können wir helfen?',
            'autocomplete': 'off',
            'required': True
        }
    )
    
    message = TextAreaField(
        'Nachricht',
        validators=[
            DataRequired(message='Nachricht ist erforderlich'),
            Length(min=10, max=5000, message='Nachricht muss zwischen 10 und 5000 Zeichen sein')
        ],
        render_kw={
            'placeholder': 'Ihre Nachricht...',
            'rows': 6,
            'required': True
        }
    )
    
    submit = SubmitField('Nachricht senden')
    
    def validate_name(self, field):
        """Validate name contains only allowed characters"""
        if not re.match(r"^[a-zA-Z\s\-\.\äöüßÄÖÜ]+$", field.data):
            raise ValidationError('Name darf nur Buchstaben, Leerzeichen, Bindestriche und Punkte enthalten')
    
    def validate_email(self, field):
        """Validate email format more strictly"""
        email = field.data.lower()
        if len(email) > 254:  # RFC 5321
            raise ValidationError('Email-Adresse ist zu lang')
    
    def validate_subject(self, field):
        """Validate subject doesn't contain spam patterns"""
        subject = field.data.lower()
        spam_patterns = ['viagra', 'casino', 'lottery', 'prize', 'click here']
        if any(pattern in subject for pattern in spam_patterns):
            raise ValidationError('Betreff enthält nicht erlaubte Wörter')
    
    def validate_message(self, field):
        """Validate message for spam patterns"""
        message = field.data.lower()
        spam_patterns = ['viagra', 'casino', 'lottery', 'click here', 'buy now']
        if any(pattern in message for pattern in spam_patterns):
            raise ValidationError('Nachricht enthält nicht erlaubte Wörter')
        
        # Check for excessive URLs
        url_count = len(re.findall(r'http[s]?://', message))
        if url_count > 2:
            raise ValidationError('Zu viele URLs in der Nachricht')
