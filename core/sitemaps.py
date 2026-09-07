from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Project


class StaticViewSitemap(Sitemap):

    priority = 1.0
    changefreq = 'monthly'

    def items(self):
        return [
            'home',
            'projects',
        ]

    def location(self, item):
        if item == 'home':
            return reverse('core:home')

        if item == 'projects':
            return reverse('core:projects')


class ProjectSitemap(Sitemap):

    changefreq = 'monthly'
    priority = 0.8

    def items(self):
        return Project.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return reverse(
            'core:project_detail',
            kwargs={'slug': obj.slug}
        )