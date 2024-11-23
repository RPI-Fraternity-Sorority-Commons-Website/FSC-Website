# myapp/models.py

from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser, User
from django.conf import settings


"""
EXAMPLE OF HOW TO MAKE A TABLE:
class table_name(models.Model):
    name = models.CharField(max_length=100)   # This creates a VARCHAR column
    age = models.IntegerField()               # This creates an INTEGER column
    price = models.DecimalField(max_digits=10, decimal_places=2) # This creates a DECIMAL column

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'table_table'   # Explicitly set the table name
"""


class Chapter(models.Model):
    name = models.CharField(max_length=255)
    letters = models.CharField(max_length=10)  # Assuming Greek letters are short
    rush_chair = models.CharField(max_length=255)
    president = models.CharField(max_length=255)
    info = models.TextField(max_length=900)  # A 900 character info blob
    chapter_size = models.PositiveIntegerField()  # Non-negative integer
    image = models.ImageField(upload_to='chapters/', blank=False, default='chapters/default.jpg')
    council = models.CharField(max_length=100, default="none")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return f'/chapters/{self.name}'

    def __str__(self):
        return self.name

class Leadership(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    chapter = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    image = models.ImageField(upload_to='leadership/', default='leadership/default.jpg')

class FSCUser(AbstractUser):
    affiliation = models.CharField(max_length=255)

class Upload(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    media_file = models.FileField(upload_to='uploads/')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} by {self.user.username}"