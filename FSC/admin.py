from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Chapter, Leadership, ChapterSemesterData

# Register all models with the admin site
admin.site.register(get_user_model())
admin.site.register(Chapter)
admin.site.register(Leadership)
admin.site.register(ChapterSemesterData)