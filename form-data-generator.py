import json
import os
import sys
from os import path
from form_data_server import start_server
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
from django.db.models import ManyToOneRel, OneToOneRel, ManyToManyRel
from django.template import Template, Context
from django.utils.encoding import smart_str
from django.utils.safestring import SafeText
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

def get_django_apps():
    installed_apps = [app for app in settings.INSTALLED_APPS
                      if not app.startswith("django.")]
    cleaned_apps = []
    for app in installed_apps:
        if os.path.exists(DJANGO_DIR+'/'+app):
            cleaned_apps.append(app)
    return cleaned_apps

def get_django_models(installed_apps):
    django_models = []
    for app in installed_apps:
        app_models = apps.get_app_config(app).get_models()
        for model in app_models:
            django_models.append(model)
    return django_models

def models_to_json(models):
    sub_json_dict = {}
    parent_json_dict ={}
    for model in models:
        for i in model._meta.get_fields():
            if type(i) != ManyToOneRel and type(i) != OneToOneRel and type(i) != ManyToManyRel:
                sub_json_dict[(str(i).rsplit(".",1)[1])]=''
        # parent_json_dict[str(model).rsplit('.',1)[1].split("'")[0]]=json.dumps(sub_json_dict).replace(',',',<br>')
        parent_json_dict[str(model).rsplit('.', 1)[1].split("'")[0]] = json.dumps(sub_json_dict).replace(',', '<br>').replace('"','')
        sub_json_dict={}
    return parent_json_dict

def make_model_tabs_html():
    pass

def get_template(data):
    html_template_file = open("template/index.html", "r")
    body_template_html = Template(html_template_file.read())
    context_data = Context(data)
    body_template_html = body_template_html.render(context_data)
    content = smart_str(body_template_html)
    html_stripped = ' '.join(str(smart_str(content)).split())
    html = SafeText(html_stripped)
    file = open("index.html", "w")
    file.write(html)
    return html

def main():
    setup()
    django_user_apps = get_django_apps()
    django_user_models = get_django_models(django_user_apps)
    json_dict = models_to_json(django_user_models)
    get_template({"json_model_data":json_dict})

    start_server()
main()