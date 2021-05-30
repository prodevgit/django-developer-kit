import json
import os
import sys
from os import path
from db_operations import SettingsDb

def get_django_project_dir():
    root_dir = os.getcwd().rsplit('/',1)[0]
    django_dir = None
    for dir in os.listdir(root_dir):
        try:
            if 'manage.py' in os.listdir(f"{root_dir}/{dir}"):
                django_dir = f"{root_dir}/{dir}"
                break
        except NotADirectoryError:
            pass
    return django_dir

#SQLite DB SETUP
db = SettingsDb()

#DJANGO ENVIRONMENT SETUP
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
sys.path.append(os.path.abspath(get_django_project_dir()))
APP_NAME="EPMS"
DJANGO_DIR = get_django_project_dir()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"{APP_NAME}.settings")

from django.apps import apps
from django.conf import settings
from django.urls import set_script_prefix
from django.utils.log import configure_logging

class DjangoConfigurator():

    def __init__(self):
        self.installed_apps = None
        self.django_dir  = DJANGO_DIR
        pass

    def django_init(self):
        configure_logging(None, settings.LOGGING)
        if True:
            set_script_prefix(
                '/' if settings.FORCE_SCRIPT_NAME is None else settings.FORCE_SCRIPT_NAME
            )
        settings.DATABASES={}
        apps.populate(settings.INSTALLED_APPS)

    def get_django_apps(self):
        installed_apps = [app for app in settings.INSTALLED_APPS
                          if not app.startswith("django.")]
        cleaned_apps = []
        for app in installed_apps:
            if os.path.exists(DJANGO_DIR+'/'+app):
                cleaned_apps.append(app)
        self.installed_apps = cleaned_apps
        return cleaned_apps

    def get_django_models(self):
        if self.installed_apps:
            django_models = []
            for app in self.installed_apps:
                app_models = apps.get_app_config(app).get_models()
                for model in app_models:
                    django_models.append(model)
            return django_models
        else:
            print("Call get_django_apps before get_django_models")