import os
import django
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dualityhotel.settings')
django.setup()

app = get_wsgi_application()

def handler(request):
    return app(request.environ, request.start_response)
