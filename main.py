print "Hello World"

import os, sys
PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
# proj_path = "C:\Users\lamng\PycharmProjects\untitled"
# This is so Django knows where to find stuff.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
sys.path.append(PROJECT_DIR)

# This is so my local_settings.py gets loaded.
os.chdir(PROJECT_DIR)

# This is so models get loaded.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Your application specific imports
from data.models import *

#Add user
User.objects.all().delete()
user = User(name="someone", email="someone@example.com")
user.save()

# Application logic

first_user = User.objects.all()[0]

print(first_user.name)
print(first_user.email)