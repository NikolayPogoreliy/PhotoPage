from django.db import models
from django.conf import settings
import random
from mptt.models import MPTTModel, TreeForeignKey
from tinymce import models as model_tinymce
from ckeditor.fields import RichTextField
from utils import ImageUploader


# Create your models here.

def make_upload_path(self, filename):
    # Переопределение имени загружаемого файла.
    n1 = random.randint(0,10000)
    n2 = random.randint(0,10000)
    n3 = random.randint(0,10000)
    filename = str(n1)+"_"+str(n2)+"_"+str(n3)+"_"+filename
    return '{}/{}'.format(settings.IMAGE_UPLOAD_DIR, filename)


class Category(MPTTModel, ImageUploader):
    name = models.CharField(max_length=150, blank=True, default="", verbose_name='Категория')
    parent = TreeForeignKey('self',null=True, blank=True, default=0, related_name='children')
    title = models.CharField(max_length=200,default="",blank=True,verbose_name='Заголовок')
    shot_description = model_tinymce.HTMLField(blank=True, help_text='Этот текст будет выведен до подчиненных категорий'
                                                                     ' или сервисов', verbose_name='Краткое описание')
    description = RichTextField(blank=True, help_text='Этот текст будет выведен после подчиненных категорий '
                                                      'или сервисов', verbose_name='Описание')
    meta_desc = models.CharField(max_length=200,default="",blank=True, verbose_name='Мета описание')
    meta_key = models.CharField(max_length=200,default="",blank=True, verbose_name='Ключевые слова')
    slug = models.SlugField(max_length=250, default="", blank=True, verbose_name='УРЛ')
    image = models.ImageField(upload_to=ImageUploader.make_upload_path, default="", blank=True, verbose_name='Изображение')
    published = models.BooleanField(verbose_name='Опубликовать')
    ordering = models.IntegerField(default=0, blank=True, null=True, verbose_name='Порядок сортировки')

    def __str__(self):
        return self.name

    def pic(self):
        if self.image:
            return u'<img src="%s" width="70"/>' % self.image.url
        else:
            return '(none)'

    pic.short_description = u'Изображение'
    pic.allow_tags = True

    def get_absolute_url(self):
        return "/services/%id/" % self.id

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    class MPTTMeta:
        order_insertion_by = ['name']


class Sizes(models.Model):
    size = models.CharField(max_length=250,blank=True, verbose_name='Размер')

    def __str__(self):
        return self.size

    class Meta():
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'


class Materials(models.Model):
    material = models.CharField(max_length=250,blank=True, verbose_name='Материал')
    description = RichTextField(blank=True, verbose_name='Описание')
    meta_desc = models.CharField(max_length=200, default="", blank=True, verbose_name='Мета описание')
    meta_key = models.CharField(max_length=200, default="", blank=True, verbose_name='Ключевые слова')
    title = models.CharField(max_length=200, default="", blank=True, verbose_name='Заголовок')
    def __str__(self):
        return self.material

    class Meta():
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'


class Services(models.Model, ImageUploader):

    folder_name = 'category'
    category = models.ForeignKey(Category, null=True, blank=True, verbose_name='Категория')
    size = models.ForeignKey(Sizes, blank=True, null=True, verbose_name='Размер')
    material = models.ForeignKey(Materials, blank=True, null=True, verbose_name='Материал')

    name = models.CharField(max_length=250, blank=True, verbose_name='Название')

    title = models.CharField(max_length=200, default="", blank=True, verbose_name='Заголовок')
    meta_desc = models.CharField(max_length=200, default="", blank=True, verbose_name='Мета описание')
    meta_key = models.CharField(max_length=200, default="", blank=True, verbose_name='Ключевые слова')
    slug = models.SlugField(max_length=250, default='', blank=True, verbose_name='УРЛ')

    image = models.ImageField(upload_to= ImageUploader.make_upload_path, default="", blank=True, verbose_name='Изображение')
    #shot_text = model_tinymce.HTMLField(blank=True, verbose_name='Краткое описание')
    #full_text = RichTextField(blank=True, verbose_name='Полное описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, verbose_name='Цена', null=True)
    published = models.BooleanField(verbose_name='Опубликовать')
    ordering = models.IntegerField(default=0, blank=True, null=True, verbose_name='Порядок сортировки')

    def __str__(self):
        return '_'.join(map(str,[self.category, self.size, self.material]))

    def pic(self):
        if self.image:
            return '<img src="%s" width="70"/>' % self.image.url
        else:
            return '(none)'

    pic.short_description = 'Изображение'
    pic.allow_tags = True


    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class ServicesImages(models.Model, ImageUploader):
    name = models.ForeignKey(Services, null=True, blank=True)#product
    image = models.ImageField(upload_to=ImageUploader.make_upload_path, default="", blank=True, verbose_name='Изображение')
    #image = Services(self).image

    def __str__(self):
        return self.image.url

    def pic(self):
        if self.image:
            return '<img src="%s" width="70"/>' % self.image.url
        else:
            return '(none)'

    pic.short_description = 'Изображение'
    pic.allow_tags = True

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'




