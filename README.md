# Personal Portfolio Site

This is a professional portfolio website built with Django. It allows you to showcase your profile, education, skills, projects, and references dynamically from the backend. The site is designed for easy customization and deployment.

## Features
- Dynamic About, Education, Skills, and References sections (editable from Django admin)
- Project showcase with category filtering
- Contact form with pop-up confirmation
- Social and contact icons (Font Awesome)
- Certificate view-only (no download)
- Signature upload for Declaration section
- Responsive design with custom CSS/JS
- Media uploads for profile picture, certificates, and signature

## Tech Stack
- Python 3
- Django
- HTML, CSS, JavaScript
- Font Awesome
- Pillow (for image support)
- django-ckeditor (for rich text fields)

## Getting Started
1. **Clone the repository:**
   ```
   git clone https://github.com/Janon04/personal-site.git
   ```
2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```
3. **Apply migrations:**
   ```
   python manage.py migrate
   ```
4. **Create a superuser:**
   ```
   python manage.py createsuperuser
   ```
5. **Run the development server:**
   ```
   python manage.py runserver
   ```
6. **Access the site:**
   - Visit `http://127.0.0.1:8000/` for the portfolio
   - Visit `http://127.0.0.1:8000/admin/` for the admin panel

## Deployment
- The site is ready for deployment on platforms like Render.
- Update `ALLOWED_HOSTS` and static/media settings as needed.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License.
