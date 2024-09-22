# Social Media API Deployment Guide

## Table of Contents

1. Introduction
2. Prerequisites
3. Project Preparation
4. Heroku Setup
5. Database Configuration
6. Static and Media Files Configuration
7. Deployment Process
8. Post-Deployment Tasks
9. Monitoring and Maintenance
10. Troubleshooting

## 1. Introduction

This guide details the process of deploying the Social Media API project to Heroku using MySQL as the database and AWS S3 for static and media file storage.

## 2. Prerequisites

- Git installed on your local machine
- Heroku account (https://signup.heroku.com/)
- Heroku CLI installed (https://devcenter.heroku.com/articles/heroku-cli)
- AWS account for S3 (https://aws.amazon.com/)
- Python 3.9 or higher

## 3. Project Preparation

### 3.1 Update settings

Create a new file `social_media_api/settings_prod.py`:

```python
from .settings import *

DEBUG = False
ALLOWED_HOSTS = ['your-app-name.herokuapp.com']

SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'your_database_host',
        'PORT': '3306',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = 'your-access-key'
AWS_SECRET_ACCESS_KEY = 'your-secret-key'
AWS_STORAGE_BUCKET_NAME = 'your-bucket-name'
AWS_S3_REGION_NAME = 'your-region'
AWS_DEFAULT_ACL = None
```

### 3.2 Update requirements.txt

Add the following to your `requirements.txt`:

- gunicorn
- mysqlclient
- django-storages
- boto3

### 3.3 Create Procfile

Create a file named `Procfile` in the project root:
web: gunicorn social_media_api.wsgi --log-file -

### 3.4 Specify Python runtime

Create a `runtime.txt` file in the project root:

```txt
python-3.12.4
```

## 4. Heroku Setup

### 4.1 Create Heroku app

```bash
heroku create your-app-name
```

### 4.2 Set environment variables

```bash
heroku config:set DJANGO_SETTINGS_MODULE=social_media_api.settings_prod
heroku config:set SECRET_KEY='your-secret-key'
```

## 5. Database Configuration

### 5.1 Add ClearDB MySQL add-on

```bash
heroku addons:create cleardb:ignite
```

### 5.2 Get database URL

```bash
heroku config | grep CLEARDB_DATABASE_URL
```

### 5.3 Update settings_prod.py

Update the DATABASES configuration in `settings_prod.py` with the information from the CLEARDB_DATABASE_URL.

## 6. Static and Media Files Configuration

### 6.1 Create S3 bucket

1. Log in to AWS Console
2. Navigate to S3 and create a new bucket
3. Set up bucket policy for public read access

### 6.2 Create IAM user

1. Navigate to IAM in AWS Console
2. Create a new user with programmatic access
3. Attach AmazonS3FullAccess policy to the user

### 6.3 Update settings_prod.py

Update the AWS settings in `settings_prod.py` with your S3 bucket information and IAM user credentials.

## 7. Deployment Process

7.1 Initialize Git repository (if not already done)

```bash
git init
git add .
git commit -m "Initial commit"
```

### 7.2 Add Heroku remote

```bash
heroku git:remote -a your-app-name
```

### 7.3 Push to Heroku

```bash
git push heroku main
```

## 8. Post-Deployment Tasks

### 8.1 Run migrations

```bash
heroku run python manage.py migrate
```

### 8.2 Collect static files

```bash
heroku run python manage.py collectstatic --noinput
```

### 8.3 Create superuser (optional)

```bash
heroku run python manage.py createsuperuser
```

## 9. Monitoring and Maintenance

### 9.1 View logs

```bash
heroku logs --tail
```

### 9.2 Set up Papertrail for advanced logging (optional)

```bash
heroku addons:create papertrail:choklad
```

### 9.3 Regular maintenance tasks

- Regularly update dependencies and redeploy
- Set up database backups
- Monitor application performance and scale as needed

## 10. Troubleshooting

### 10.1 Application errors

- Check Heroku logs: heroku logs --tail
- Verify all environment variables are set correctly: heroku config

### 10.2 Database issues

- Ensure ClearDB add-on is properly installed: heroku addons
- Check database connection settings in settings_prod.py

### 10.3 Static files not serving

- Verify AWS S3 bucket permissions
- Check AWS credentials in settings_prod.py

### 10.4 Deployment failures

- Ensure all dependencies are in requirements.txt
- Check for syntax errors in your Python code
- Verify Procfile is correctly configured

For any persistent issues, consult the Heroku Dev Center or seek assistance from the Django and Heroku communities.

- This comprehensive guide covers all aspects of deploying your Social Media API to Heroku, from project preparation to troubleshooting. It provides step-by-step instructions for setting up the production environment, configuring the database and static file storage, and maintaining the deployed application.

- Remember to replace placeholder values (like 'your-app-name', 'your-secret-key', etc.) with your actual values when following this guide. Also, ensure that sensitive information like secret keys or passwords are not committed to version control, but rather managed through environment variables or Heroku config vars.
