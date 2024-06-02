

# to be configured in production

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_web_app.settings')

application = get_wsgi_application()
