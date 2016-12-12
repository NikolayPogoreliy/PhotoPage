from django.contrib import admin
from inform.models import AboutUs, ContactType, Contacts, Articles
# Register your models here.

class AboutUsAdmin(admin.ModelAdmin):
    list_editable = ['title','slug','published']
    list_display = ['title','published','slug']

class ContactsAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact', 'published', 'pic']
    list_editable = ['name', 'contact', 'published']

class ArticlesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name','pub_date','published','pic']
    list_editable = ['name','published']

admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(Contacts, ContactsAdmin)
admin.site.register(ContactType)
admin.site.register(Articles, ArticlesAdmin)