from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator


class User(AbstractUser):
    username = models.CharField(unique=True, max_length=120, null=False, blank=False)
    email = models.EmailField(max_length=255, 
        unique=True, 
        null=False, 
        blank=False,
        default="default_username"
        )
    password = models.CharField(max_length=100)

    class Meta:
        app_label = 'blogs'

    def __str__(self):
        return f"{self.username}, {self.email}"
   

class Blogs(models.Model):
    title = models.CharField(max_length=150)
    blog_poster = models.ImageField(upload_to='blog_images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    article = models.FileField(
        upload_to='documents/',
        validators=[FileExtensionValidator(['pdf', 'docx', 'txt'])]
    )
    author_image = models.ImageField(upload_to='blog_images/')
    blog_subtitle = models.CharField(max_length=250)
    date_published = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'blogs'

    def __str__(self):
        return self.title

class SideBlog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    author_image = models.ImageField(upload_to='blog_images/')
    article = models.FileField(
        upload_to='documents/',
        validators=[FileExtensionValidator(['pdf', 'docx', 'txt'])]
    )
    title = models.CharField(max_length=150)
    date_published = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'blogs'

    def __str__(self):
        return self.title