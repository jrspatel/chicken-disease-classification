"""
    keeps track of project artifacts i.e.
    --> the current version of the project, author
    -->  reads the readme.md file
    --> can be easily shared to pypi community
"""

import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    descrition = f.read() 

__version__ = '0.0.0'

REPO_NAME = 'chicken-disease-classification'
AUTHOR_NAME = 'jrspatel'
SRC_REPO = 'CNN_CLASSIFIER'
AUTHOR_EMAIL = 'jrspatel12@gmail.com' 

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email= AUTHOR_EMAIL,
    description= 'python package wiht cnn app',
    long_description= descrition ,
    url = f'https://github.com/{AUTHOR_NAME}/{REPO_NAME}',
    project_urls = {
        'bug_tracker' : f'https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues'
    },
    package_dir={'':'src'},
    packages = setuptools.find_packages(where='src')
)