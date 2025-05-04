# Alharis Feysel's Portfolio Website

A modern, responsive portfolio website built with Flask and Tailwind CSS.

## Features

- Responsive design
- Modern UI with glass morphism effects
- Mobile-friendly navigation
- Smooth animations and transitions
- Contact form functionality

## Local Development

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the development server:
   ```bash
   flask run
   ```

## Deployment

The website can be deployed on various platforms:

### Render (Recommended)

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Set the following environment variables:
   - `FLASK_APP=app.py`
   - `FLASK_ENV=production`
4. Deploy!

### Heroku

1. Create a new app on Heroku
2. Connect your GitHub repository
3. Set the following environment variables:
   - `FLASK_APP=app.py`
   - `FLASK_ENV=production`
4. Deploy!

## Technologies Used

- Flask
- Tailwind CSS
- Font Awesome
- JavaScript
- HTML5
- CSS3

## Customization

### Personal Information
- Update the content in each template file to reflect your personal information
- Modify the `about.html` template to include your bio
- Update the projects in `projects.html` to showcase your work
- Add your own images to the `static/images` directory

### Styling
- Colors can be modified in `static/css/style.css` by updating the CSS variables in the `:root` selector
- Responsive breakpoints can be adjusted in the media queries

### Contact Form
- The contact form in `contact.html` needs to be connected to a backend service
- You can use services like EmailJS, Formspree, or implement your own email functionality

## Contributing

Feel free to fork this project and customize it for your own use. If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is open source and available under the [MIT License](LICENSE). 