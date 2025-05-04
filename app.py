from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

# Email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_USERNAME')

# Initialize Flask-Mail
mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        try:
            # Send email to yourself
            msg = Message(
                subject=f'New Contact Form Message from {name}',
                recipients=[os.getenv('MAIL_USERNAME')],
                body=f'''
                Name: {name}
                Email: {email}
                Message: {message}
                '''
            )
            mail.send(msg)

            # Send confirmation email to the sender
            confirmation_msg = Message(
                subject='Thank you for contacting me!',
                recipients=[email],
                body=f'''
                Dear {name},

                Thank you for reaching out! I have received your message and will get back to you as soon as possible.

                Best regards,
                Alharis Feysel
                '''
            )
            mail.send(confirmation_msg)

            flash('Your message has been sent successfully!', 'success')
            return redirect(url_for('contact'))

        except Exception as e:
            flash('There was an error sending your message. Please try again later.', 'error')
            return redirect(url_for('contact'))

    return render_template('contact.html')

# This is required for Vercel
if __name__ == '__main__':
    app.run(debug=True)
else:
    # This is required for Vercel
    app = app 