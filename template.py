import os
from pathlib import Path
import logging 

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'CNN CLASSIFIER' 

file_list = [
    '.github/workflows/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/constants/__init__.py',
    f'src/{project_name}/pipeline/__init__.py',
    'config/config.yaml',
    'params/params.yaml',
    'setup.py',
    'dvc.yaml',
    'research/trails.ipynb'
]

print(1)

for file in file_list:
    # converting the filepath to windows supported format
    filepath = Path(file)
    
    filedir , filename = os.path.split(filepath)

    if filedir!='':
        os.makedirs(filedir, exist_ok=True) 
        logging.info(f'created file dir : {filedir} for filename : {filename}') 
    

    if not os.path.exists(filepath):
        with open(filepath,'w'):
            pass 
            logging.info(f'created empty filename : {filename}') 

