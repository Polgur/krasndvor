from django.db import models
from django.core.urlresolvers import reverse
from sorl.thumbnail import ImageField
from django.utils import timezone
from ckeditor.fields import RichTextField

class Techno(models.Model):
    mnemo = models.CharField(max_length=16, unique=True)
    name = models.CharField(max_length=40, unique=True)
    main = models.BooleanField()
    show_in_menu = models.BooleanField()

    class Meta:
        verbose_name = 'Технология'
        verbose_name_plural = 'Технологии'

    def __str__(self):
        return self.mnemo.title()

class Project(models.Model):
    name = models.CharField(max_length=25, unique=True)
    slug = models.SlugField()
    techs = models.ManyToManyField(Techno)
    vid_choices = (
        (1, 'Коттедж'),
        (2, 'Дуплекс'),
        (3, 'Баня'),
    )
    vid = models.SmallIntegerField(choices=vid_choices)
    house_choices = (
        (1, 'Одноэтажный'),
        (2, 'С мансардой'),
        (3, 'Двухэтажный'),
        (4, 'Баня'),
        (5, 'Дуплекс'),
    )
    house = models.SmallIntegerField(choices=house_choices)
    img  = ImageField(upload_to='projects')
    size = models.CharField(max_length=25)
    square = models.PositiveSmallIntegerField()
    price = models.IntegerField()
    description = models.TextField()

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.name.title()

    def get_absolute_url(self):
        return reverse('project_detail',
                       kwargs={'slug': self.slug})

class PrjPhoto(models.Model):
    prn = models.ForeignKey(Project, related_name='photos')
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

class PrjKit(models.Model):
    prn = models.ForeignKey(Project, related_name='kits')
    tech = models.ForeignKey(Techno)
    price1 = models.IntegerField()
    price2 = models.IntegerField()
    kit1 = RichTextField()
    kit2 = RichTextField()

    class Meta:
        verbose_name = 'Комплектация'
        verbose_name_plural = 'Комплектации'

    def __str__(self):
        return "{} {}".format(self.prn.name.title(),self.tech.mnemo.title())

class Article(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название статьи")
    slug = models.SlugField(verbose_name="Урл")
    title = models.CharField(max_length=250, blank=True, verbose_name="Заголовок в браузере")
    metakey = models.CharField(max_length=250, blank=True, verbose_name="Ключевые слова")
    metadesc = models.CharField(max_length=250, blank=True, verbose_name="Мета описание")
    techs = models.ManyToManyField(Techno)
    publish = models.DateTimeField(default=timezone.now, verbose_name="Дата публикации")
    description = RichTextField(verbose_name="Краткое описание")
    body = RichTextField(verbose_name="Текст статьи")

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.name.title()

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})

class Calculation(models.Model):
    fio = models.CharField(max_length=80)
    created = models.DateTimeField(default=timezone.now)
    email = models.EmailField(null=True,blank=True)
    phone = models.CharField(max_length=20,null=True,blank=True)
    note = models.CharField(max_length=400)
    file = models.FileField(upload_to='calc_files',null=True,blank=True)
    kit = models.ForeignKey(PrjKit,null=True,blank=True)
    kit_numb = models.PositiveSmallIntegerField(null=True,blank=True)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def get_absolute_url(self):
        return reverse('thanks')

class PhoneCall(models.Model):
    fio = models.CharField(max_length=80)
    created = models.DateTimeField(default=timezone.now,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    phone = models.CharField(max_length=20)
    wtime = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Обратный звонок'
        verbose_name_plural = 'Звонки'

    def get_absolute_url(self):
        return reverse('thanks')
