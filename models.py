from django.db import models


# Create your models here.
class BlogPost(models.Model):
    # id - Django automatically creates an auto-incrementing primary key for every model!
    title = models.CharField(max_length=120, null=True, blank=False)
    subtitle = models.CharField(max_length=180, null=True, blank=False)
    slug = models.SlugField(unique=True, null=True, blank=False)
    body = models.TextField()
    image = models.ImageField(upload_to='uploads/', null=False, default=None)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return self.title