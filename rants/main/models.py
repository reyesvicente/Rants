from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

User = get_user_model()


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
    user = models.ForeignKey(User, default='', null=True, related_name='users_rant', on_delete=models.PROTECT)

    class Meta:
        verbose_name = "rant"
        verbose_name_plural = 'rants'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Rant, self).save(*args, **kwargs)
        return self.slug

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('main:detail', kwargs={'slug': self.slug})