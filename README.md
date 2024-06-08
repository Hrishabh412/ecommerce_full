# ecommerce_full

below are the steps to deploy any to Heroku
Backend: Using Heroku for Django
Create a Heroku Account and Install Heroku CLI

Go to Heroku and create an account.
Install the Heroku CLI: Heroku CLI installation guide
Prepare Your Django Application for Heroku

Install gunicorn and django-heroku

Add these to your requirements.txt if not already included:
gunicorn
django-heroku
Update settings.py

Add the following at the bottom of backend/ecommerce/settings.py:
import django_heroku
django_heroku.settings(locals())

Create a Procfile in the root directory
web: gunicorn ecommerce.wsgi
Create runtime.txt for Python version

Example:
python-3.9.6

Deploy to Heroku:
heroku login
heroku create
git push heroku master
heroku run python manage.py migrate
Add Static Files Support

If you're using Heroku, you might need to add Whitenoise for static files:

Install Whitenoise:
pip install whitenoise
Update settings.py

Add whitenoise middleware:
MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    ...
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
Open the Application:
heroku open
Frontend: Using Vercel for React
Create a Vercel Account and Install Vercel CLI

Go to Vercel and create an account.
Install the Vercel CLI: Vercel CLI installation guide

Deploy the React Application:
cd frontend
vercel
Follow the prompts to deploy the application.

Final Steps: Share the Links
After successfully deploying the backend and frontend, you should have two URLs:

One for the Django backend hosted on Heroku
One for the React frontend hosted on Vercel

Example Links
Backend URL: https://your-heroku-app.herokuapp.com/
Frontend URL: https://your-vercel-app.vercel.app/

By following these steps, you'll have successfully hosted the application on free web hosting services, fulfilling the assignment requirements.
