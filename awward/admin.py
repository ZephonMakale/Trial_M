from django.contrib import admin
from .models import Project,Location,Profile,Image,Review

# Register your models here.

admin.site.register(Project)
admin.site.register(Profile)
admin.site.register(Image)
admin.site.register(Location)
admin.site.register(Review)
