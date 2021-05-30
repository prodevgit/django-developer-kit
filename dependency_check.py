import os
from glob import glob

root_dir = os.getcwd().rsplit('/', 1)[0]
django_dir = None
for dir in os.listdir(root_dir):
    try:
        if 'manage.py' in os.listdir(f"{root_dir}/{dir}"):
            django_dir = f"{root_dir}/{dir}"
            break
    except NotADirectoryError:
        pass

if django_dir == None:
    print("Django project not found. Place this folder outside django project folder and rerun")
    exit()

#Virtual Env check
result = [y for x in os.walk(django_dir) for y in glob(os.path.join(x[0], 'bin/activate'))]
if result:
    os.system(f'{result[0].rsplit("/",1)[0]}/python3 main.py')
else:
    print("Virtual environment not found. Please check if your project has vitrual environment configured")