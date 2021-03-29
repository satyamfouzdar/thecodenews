from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=80)
    slug = models.SlugField(max_length=80)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    description = models.TextField()

    # Will change this to some user after we implement some cleaning logic.
    author = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
