import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import render_template_string, current_app

def send_contact_email(data):
    """
    Send contact form email
    
    Args:
        data: Dictionary with keys: name, email, subject, message
    """
    try:
        # Get mail configuration
        mail_server = current_app.config['MAIL_SERVER']
        mail_port = current_app.config['MAIL_PORT']
        mail_username = current_app.config['MAIL_USERNAME']
        mail_password = current_app.config['MAIL_PASSWORD']
        contact_mail = current_app.config['CONTACT_MAIL']
        
        # Create message
        msg = MIMEMultipart()
        msg['From'] = mail_username
        msg['To'] = contact_mail
        msg['Subject'] = f"Neue Kontaktanfrage: {data['subject']}"
        
        # Email body
        body = f"""
        <h2>Neue Kontaktanfrage</h2>
        <p><strong>Name:</strong> {data['name']}</p>
        <p><strong>Email:</strong> {data['email']}</p>
        <p><strong>Betreff:</strong> {data['subject']}</p>
        <p><strong>Nachricht:</strong></p>
        <p>{data['message']}</p>
        """
        
        msg.attach(MIMEText(body, 'html'))
        
        # Send email
        with smtplib.SMTP(mail_server, mail_port) as server:
            server.starttls()
            server.login(mail_username, mail_password)
            server.send_message(msg)
        
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

def send_confirmation_email(recipient_email, name):
    """Send confirmation email to user"""
    try:
        mail_server = current_app.config['MAIL_SERVER']
        mail_port = current_app.config['MAIL_PORT']
        mail_username = current_app.config['MAIL_USERNAME']
        mail_password = current_app.config['MAIL_PASSWORD']
        
        msg = MIMEMultipart()
        msg['From'] = mail_username
        msg['To'] = recipient_email
        msg['Subject'] = "Wir haben Ihre Nachricht erhalten"
        
        body = f"""
        <h2>Vielen Dank für Ihre Nachricht!</h2>
        <p>Lieber {name},</p>
        <p>wir haben Ihre Nachricht erhalten und werden Sie schnellstmöglich kontaktieren.</p>
        <p>Mit freundlichen Grüßen</p>
        """
        
        msg.attach(MIMEText(body, 'html'))
        
        with smtplib.SMTP(mail_server, mail_port) as server:
            server.starttls()
            server.login(mail_username, mail_password)
            server.send_message(msg)
        
        return True
    except Exception as e:
        print(f"Error sending confirmation email: {e}")
        return False
