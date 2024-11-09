from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Chapter, Council

# Register all models with the admin site
admin.site.register(Chapter)
admin.site.register(Council)
admin.site.register(get_user_model())
