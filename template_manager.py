from django.template import Template, Context
from django.utils.encoding import smart_str
from django.utils.safestring import SafeText

class TemplateManager():

    def __init__(self):
        self.form_html = None
        self.api_html = None
        pass

    def generate_index(self,menu_data):
        html_template_file = open("template/index.html", "r")
        body_template_html = Template(html_template_file.read())
        context_data = Context({'menu_data':menu_data})
        body_template_html = body_template_html.render(context_data)
        content = smart_str(body_template_html)
        html_stripped = ' '.join(str(smart_str(content)).split())
        html = SafeText(html_stripped)
        file = open("index.html", "w")
        file.write(html)
        self.api_html = html

    def set_form_template(self,data):
        html_template_file = open("template/form.html", "r")
        body_template_html = Template(html_template_file.read())
        context_data = Context({'model_data':data})
        body_template_html = body_template_html.render(context_data)
        content = smart_str(body_template_html)
        html_stripped = ' '.join(str(smart_str(content)).split())
        html = SafeText(html_stripped)
        self.form_html = html

    def set_api_template(self,data):
        html_template_file = open("template/api.html", "r")
        body_template_html = Template(html_template_file.read())
        context_data = Context({'api_data':data})
        body_template_html = body_template_html.render(context_data)
        content = smart_str(body_template_html)
        html_stripped = ' '.join(str(smart_str(content)).split())
        html = SafeText(html_stripped)
        self.api_html = html

    def make_template(self):
        menu_data = []
        if self.form_html:
            file = open("form.html", "w")
            file.write(self.form_html)
            menu_data.append('Form')
        if self.api_html:
            file = open("api.html", "w")
            file.write(self.form_html)
            menu_data.append('Api')

        self.generate_index(menu_data)


