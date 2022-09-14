from django.contrib import admin
from .models import Project

# Register your models here.
# import the model class first
# and with the code below you make the model available on the site
admin.site.register(Project)
