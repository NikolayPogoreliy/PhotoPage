from django.db import models
from mptt.models import MPTTModel
from ckeditor.fields import RichTextField
from utils import ImageUploader

# Create your models here.

class AboutUs(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True, verbose_name='Заголовок')
    text = RichTextField(blank=True, null=True, verbose_name='Описание')
    published = models.BooleanField(verbose_name='Опубликовать', default=1)
    slug = models.SlugField(max_length=250,default="about_us", blank=True, verbose_name='УРЛ')
    pub_date = models.DateTimeField(verbose_name='Время создания')

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = verbose_name_plural = 'Информация о нас'


class ContactType (models.Model):
    type = models.CharField(max_length=250, blank=True, verbose_name='Тип контакта')

    def __str__(self):
        return self.type

    class Meta():
        verbose_name = 'Тип контакта'
        verbose_name_plural = 'Типы контактов'


class Contacts (models.Model, ImageUploader):
    name = models.ForeignKey(ContactType, null=True, blank=True, verbose_name='Тип контакта')
    contact = models.CharField(max_length=300, blank=True, null=True, verbose_name='Контакт')
    published = models.BooleanField(verbose_name='Доступен')
    image = models.ImageField(upload_to=ImageUploader.make_upload_path, default="", blank=True, verbose_name='Иконка')

    def __str__(self):
        return self.contact

    def pic(self):
        if self.image:
            return '<img src="%s" width="25"/>' % self.image.url
        else:
            return '(none)'

    pic.short_description = 'Иконка'
    pic.allow_tags = True

    class Meta():
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Articles(models.Model, ImageUploader):
    name = models.CharField(max_length=150, blank=True, null=True, verbose_name='Название статьи')
    article = RichTextField(blank=True, null=True, verbose_name='Статья')
    title = models.CharField(max_length=150, blank=True, null=True, verbose_name='Заголовок')
    meta_key = models.CharField(max_length=150, blank=True, null=True, verbose_name='Ключевые слова')
    meta_desc = models.CharField(max_length=255, blank=True, null=True, verbose_name='Мета-описание')
    published = models.BooleanField(default=True, verbose_name='Опубликовать')
    pub_date = models.DateTimeField(auto_now=True, verbose_name='Дата публикации')
    slug = models.SlugField(max_length=250, default="", blank=True, verbose_name='УРЛ')
    image = models.ImageField(upload_to=ImageUploader.make_upload_path, default="", blank=True, verbose_name='Изображение для заголовка')

    def __str__(self):
        return self.title

    def pic(self):
        if self.image:
            return '<img src="%s" width="25"/>' % self.image.url
        else:
            return '(none)'

    pic.short_description = 'Изображение'
    pic.allow_tags = True

    class Meta():
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'