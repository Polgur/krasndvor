from django.db import models
from django.core.urlresolvers import reverse
from sorl.thumbnail import ImageField
from django.utils import timezone

class Techno(models.Model):
    mnemo = models.CharField(max_length=16, unique=True)
    name = models.CharField(max_length=40, unique=True)

    class Meta:
        verbose_name = 'Технология'
        verbose_name_plural = 'Технологии'

    def __str__(self):
        return self.name.title()

class Project(models.Model):
    name = models.CharField(max_length=25, unique=True)
    slug = models.SlugField()
    techs = models.ManyToManyField(Techno)
    img  = models.ImageField(upload_to='projects')
    size = models.CharField(max_length=25)
    square = models.PositiveSmallIntegerField
    price = models.IntegerField
    description = models.TextField

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.name.title()

    def get_absolute_url(self):
        return reverse('project_detail',
                       kwargs={'slug': self.slug})


class Article(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField()
    techs = models.ManyToManyField(Techno)
    publish = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    body = models.TextField()

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.name.title()

    def get_absolute_url(self):
        return reverse('article_detail',
                       kwargs={'slug': self.slug})
