import os
import re
from django.urls import reverse
from glob import glob
from django.conf import settings
from django.urls import URLPattern, URLResolver



class API:

    def __init__(self,django_configurator):
        self.django_configurator = django_configurator
        self.url_paths = self.get_urls()


    def list_urls(self,lis,acc=None):
        if acc is None:
            acc = []
        if not lis:
            return
        l = lis[0]
        if isinstance(l, URLPattern):
            yield acc + [str(l.pattern)]
        elif isinstance(l, URLResolver):
            yield from self.list_urls(l.url_patterns, acc + [str(l.pattern)])
        yield from self.list_urls(lis[1:], acc)

    def get_urls(self):
        urls=[]
        self.urlconf = __import__(settings.ROOT_URLCONF, {}, {}, [''])
        for p in self.list_urls(self.urlconf.urlpatterns):
            urls.append(''.join(p))
        return urls


