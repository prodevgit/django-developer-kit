import os
import re
from django.urls import reverse
from glob import glob

class API:

    def __init__(self,django_configurator):
        self.django_configurator = django_configurator
        self.url_paths = self.get_url_paths()
        self.url_namespace = self.process_urls()


    def get_url_paths(self):
        raw_paths = []
        url_paths = []
        raw_paths.extend([y for x in os.walk(self.django_configurator.django_dir) for y in glob(os.path.join(x[0], 'urls.py'))])
        for path in raw_paths:
            if 'venv' not in path:
                url_paths.append(path)
        print(url_paths)
        return url_paths

    def process_urls(self):
        processed_namespaces = []
        for path in self.url_paths:
            file = open(path,'r')
            for line in file.readlines():
                line = line.replace("\n","")
                if re.search("name=",line):
                    f_line = line.split('name=')[1].replace("'",'"').split('"')[1]
                    try:
                        processed_namespaces.append(reverse(f"v1:{f_line}"))
                    except:
                        print(re.search("<[a-z]*[:]",line) or re.search("<[a-z]*>",line))
                        print(line)
                        pass
        print(processed_namespaces)
        return processed_namespaces

