import os
import sys
import django

# Add project to path
sys.path.insert(0, '/var/task')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dualityhotel.settings')

# Configure Django
django.setup()

from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()
