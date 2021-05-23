import os
import platform
import shutil

VIRTUALENV = None

if platform.system()=="Linux":

    if shutil.which('pip') == None :
        os.system(f'sudo -S apt install python3-pip',)
    if shutil.which('virtualenv') == None:
            os.system(f'sudo -S apt install python3-virtualenv')
            os.system(f'sudo -S apt install python3-venv')
    else:
        if 'env' in os.listdir(os.getcwd()):
            if 'activate' in os.listdir(f"{os.getcwd()}/env/bin"):
                print("Virtual env exists")
                print(os.system(f'env/bin/easy_install `cat {os.getcwd()}/requirements.txt`'))
        else:
            os.system('sudo -S python3 -m venv env')

    root_dir = os.getcwd().rsplit('/', 1)[0]
    django_dir = None
    for dir in os.listdir(root_dir):
        if 'manage.py' in os.listdir(f"{root_dir}/{dir}"):
            django_dir = f"{root_dir}/{dir}"
            break
    print('#####################')
    os.system(f'env/bin/python3 form-data-generator.py')
