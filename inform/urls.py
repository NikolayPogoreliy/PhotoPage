from django.conf.urls import url


urlpatterns = [

    url(r'^about/$', 'inform.views.about', name="about_us"),
    url(r'^contacts/$', 'inform.views.contacts', name="contacts"),

]

