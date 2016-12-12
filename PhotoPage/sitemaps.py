from django.contrib.sitemaps import Sitemap
from inform.models import AboutUs, Contacts
from catalog.models import Category
from django.core.urlresolvers import reverse


class SitemapCategory(Sitemap):
    def items(self):
        return Category.objects.all()


class SitemapAboutUs(Sitemap):
    changefreq = 'never'

    def items(self):
        return ['about_us']

    def location(self, items):
        return reverse(items)


class SitemapContacts(Sitemap):
    changefreq = 'never'

    def items(self):
        return ['contacts']

    def location(self, items):
        return reverse(items)