from django.db import models
from django.core.urlresolvers import reverse
from sorl.thumbnail import ImageField
from django.utils import timezone
from ckeditor.fields import RichTextField

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
    img  = ImageField(upload_to='projects')
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

class PrjPhoto(models.Model):
    prn = models.ForeignKey(Project, related_name='Photos')
    type_choices = (
        (1, 'Вид'),
        (2, 'План 1 этажа'),
        (3, 'План 2 этажа'),
    )
    type = models.SmallIntegerField(choices=type_choices)
    img = ImageField(upload_to='projects')

    def __str__(self):
        return self.prn.name.title()

    class Meta:
        verbose_name = 'Фото проекта'
        verbose_name_plural = 'Фото проекта'

class Article(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField()
    techs = models.ManyToManyField(Techno)
    publish = models.DateTimeField(default=timezone.now)
    description = RichTextField()
    body = RichTextField()

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.name.title()

    def get_absolute_url(self):
        return reverse('article_detail',
                       kwargs={'slug': self.slug})
