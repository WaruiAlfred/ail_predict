from django.contrib import admin
from .models import User, Diabetes, Results

# Register your models here.
admin.site.register(User)
admin.site.register(Diabetes)
admin.site.register(Results)