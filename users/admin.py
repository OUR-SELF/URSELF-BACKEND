from django.contrib import admin
from users.models import Consumer_Users, Company_Users

# Register your models here.
admin.site.register(Consumer_Users)
admin.site.register(Company_Users)

