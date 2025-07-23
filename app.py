from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv
import logging
import requests

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'default-secret-key-for-development')

# Email configuration
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 587))
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', 'True').lower() == 'true'
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_USERNAME')

# Initialize Flask-Mail
mail = Mail(app)

GITHUB_USERNAME = "Harisfeysel"  # TODO: Replace with your GitHub username

def fetch_github_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    repos = fetch_github_repos(GITHUB_USERNAME)
    return render_template('projects.html', repos=repos)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Check if email configuration is available
        if not all([app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD']]):
            flash('Email service is currently unavailable. Please try again later.', 'error')
            return redirect(url_for('contact'))

        try:
            # Send email to yourself
            msg = Message(
                subject=f'New Contact Form Message from {name}',
                recipients=[app.config['MAIL_USERNAME']],
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
            logger.error(f"Error sending email: {str(e)}")
            flash('There was an error sending your message. Please try again later.', 'error')
            return redirect(url_for('contact'))

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=False)  # Set debug to False in production
else:
    app = app 