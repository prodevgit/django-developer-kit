import json
from django.db.models import ManyToOneRel, OneToOneRel, ManyToManyRel


class FormGenerator():

    def __init__(self,models):
        self.models = models

    def models_to_json(self):
        sub_json_dict = {}
        parent_json_dict ={}
        for model in self.models:
            for i in model._meta.get_fields():
                if type(i) != ManyToOneRel and type(i) != OneToOneRel and type(i) != ManyToManyRel:
                    sub_json_dict[(str(i).rsplit(".",1)[1])]=''
            # parent_json_dict[str(model).rsplit('.',1)[1].split("'")[0]]=json.dumps(sub_json_dict).replace(',',',<br>')
            parent_json_dict[str(model).rsplit('.', 1)[1].split("'")[0]] = json.dumps(sub_json_dict).replace(',', '<br>').replace('"','')
            sub_json_dict={}
        return parent_json_dict
