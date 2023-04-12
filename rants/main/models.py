from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)
        return self.slug


class Rant(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    categories = models.ManyToManyField(
        Category, related_name='rants_categories')

    class Meta:
        verbose_name = "rant"
        verbose_name_plural = 'rants'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Rant, self).save(*args, **kwargs)
        return self.slug
