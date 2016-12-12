from django.conf.urls import url


urlpatterns = [
    url(r'^services/(?P<slug>[-\w]+)/$', 'catalog.views.category', name="category"),
    url(r'^services/$', 'catalog.views.services', name="services"),
    url(r'^$', 'catalog.views.category_main', name="home"),

]

