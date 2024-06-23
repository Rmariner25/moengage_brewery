import os
import blog

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# secret key used in production should be hidden!
SECRET_KEY = 'fill_here'

# configure in production
DEBUG = True

ALLOWED_HOSTS = ['*']

HOST = os.environ.get("HOST", default="http://localhost:8000/")

EMAIL_HOST = 'fill_here'
EMAIL_HOST_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'fill_here'
EMAIL_HOST_PASSWORD = 'fill_here'

INSTALLED_APPS = [
    'blog.apps.BlogConfig',
    'users.apps.UsersConfig',
    'crispy_forms',
    'crispy_bootstrap4',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
]

CSRF_TRUSTED_ORIGINS=['http://localhost', 'http://127.0.0.1']

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_web_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_web_app.wsgi.application'

HOST = os.environ.get("HOST", default="http://localhost:8000/")

# Configuring AWS RDS
DATABASES = {
    'default': {

        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR + 'db.sqlite3',
        
        
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

PASSWORD_RESET_TIMEOUT = 3600


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'utc' # see django documentation 

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

# Configuring AWSS3
"""
STORAGES = {
    "default" : {
        "BACKEND" : "storages.backends.s3boto3.S3StaticStorage",
    },
    "staticfiles" : {
        "BACKEND" : "storages.backends.s3boto3.S3StaticStorage",
    },
}
"""

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'blog-home'
LOGIN_URL = 'login'

# Configuring AWSS3
"""
AWS_ACCESS_KEY_ID = 'fill_here'
AWS_SECRET_ACCESS_KEY = 'fill_here'
AWS_STORAGE_BUCKET_NAME = 'fill_here'
AWS_S3_SIGNATURE_VERSION = 'fill_here'
DEFAULT_FILE_STORAGE = 'fill_here'
AWS_S3_REGION_NAME = 'fill_here'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL =  None
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.{region}.amazonaws.com'
AWS_LOCATION = 'static'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'
STATICFILES_STORAGE = 'blog.storage_backends.StaticStorage'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
"""

STATIC_URL = '/static/'
STATIC_ROOT= os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
