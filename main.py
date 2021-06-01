from api_crawler import API

try:
    from django_setup import DjangoConfigurator,DJANGO_DIR
    from form_generator import FormGenerator
    from server import start_server
    from template_manager import TemplateManager

    cf = DjangoConfigurator()
    cf.django_init()

    django_user_apps = cf.get_django_apps()
    django_user_models = cf.get_django_models()

    form_gen = FormGenerator(django_user_models)
    form_dict = form_gen.models_to_json()
    template_manager = TemplateManager()
    template_manager.set_form_template(form_dict)
    template_manager.make_template()

    api = API(cf)
    urls = api.get_urls()

    print(urls)

    start_server()
except ModuleNotFoundError:
    print("Run using run.py")