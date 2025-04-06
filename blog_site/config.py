# Configuration settings like SECRET_KEY, DB URI
# config.py
import os
basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'your_secret_key'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database', 'blog.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'admin123'



