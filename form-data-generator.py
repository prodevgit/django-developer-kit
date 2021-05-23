import os
import re
#DJANGO ENVIRONMENT SETUP
APP_NAME="EPMS"
DJANGO_DIR = os.getcwd().rsplit('/',1)[0]
os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"{APP_NAME}.settings")
from django.apps import apps
from django.conf import settings
from django.urls import set_script_prefix
from django.utils.log import configure_logging

def setup():
    configure_logging(None, settings.LOGGING)
    if True:
        set_script_prefix(
            '/' if settings.FORCE_SCRIPT_NAME is None else settings.FORCE_SCRIPT_NAME
        )
    settings.DATABASES={}
    apps.populate(settings.INSTALLED_APPS)


# EXCLUDE = ['site-packages']

def get_django_apps():
    installed_apps = [app for app in settings.INSTALLED_APPS
                      if not app.startswith("django.")]
    cleaned_apps = []
    for app in installed_apps:
        if os.path.exists(DJANGO_DIR+'/'+app):
            cleaned_apps.append(app)
    return cleaned_apps

# def get_django_models(model_files):
#     model_list = []
#     print(model_files)
#     class_regex_string=None
#     for file in model_files:
#         with open(file) as f:
#             for line in f:
#                 class_regex_string = re.search("^class\s\w*[(]", line.rstrip("\n"))
#                 if(class_regex_string):
#                     model_list.append(class_regex_string.string)
#
#     print(model_list)
#                 # break
#     return model_list

def get_django_models(installed_apps):
    django_models = []
    for app in installed_apps:
        app_models = apps.get_app_config(app).get_models()
        for model in app_models:
            django_models.append(model)
    return django_models

def model_to_json(model):
    for i in model._meta.get_fields():
        print(i)

def main():
    setup()
    django_user_apps = get_django_apps()
    django_user_models = get_django_models(django_user_apps)
    model_to_json(django_user_models[3])

main()