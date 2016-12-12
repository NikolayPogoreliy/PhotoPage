from django.contrib import admin
from django.db.models import F
from catalog.models import Services, ServicesImages, Category, Sizes, Materials
# Register your models here.

class ServicesImagesInline(admin.StackedInline):
    model = ServicesImages
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['name', 'slug', 'published', 'ordering', 'image', 'pic',]
    list_editable = ['slug', 'published', 'ordering',]
    #list_select_related = ['name']


class ServicesAdmin(admin.ModelAdmin):

    prepopulated_fields = {"slug": ('name',)}

    list_display = ['category','material','size','image', 'pic', 'slug', 'published', 'ordering','price',]
    list_editable = ['slug', 'published', 'ordering','price']
    inlines = [ServicesImagesInline,]
    list_filter = ['category',]
    search_fields = ['size','material',]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(ServicesImages)
admin.site.register(Sizes)
admin.site.register(Materials)