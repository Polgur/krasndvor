from django.db import models
from django.core.urlresolvers import reverse
from sorl.thumbnail import ImageField
from django.utils import timezone

class Techno(models.Model):
    name = models.CharField(max_length=25, null=False, unique=True)

    def __str__(self):
        return self.name.title()

class Project(models.Model):
    name = models.CharField(max_length=25, null=False, unique=True)
    slug = models.SlugField()
    tech = models.PositiveSmallIntegerField(null=False)
    img  = models.ImageField(upload_to='projects')
    size = models.CharField(max_length=25, null=False)
    square = models.PositiveSmallIntegerField(null=False)
    price = models.IntegerField(null=False)
    description = models.TextField(null=False)

    def __str__(self):
        return self.name.title()

    def get_absolute_url(self):
        return reverse('project_detail',
                       kwargs={'slug': self.slug})


class Article(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)
    slug = models.SlugField()
    techs = models.ManyToManyField(Techno)
    publish = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    body = models.TextField()

    def __str__(self):
        return self.name.title()
