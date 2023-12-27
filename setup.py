# setup.py
from setuptools import setup, find_packages

setup(
    name='dockona',
    description = 'docker wrapper for local dev env',
    author = 'ashraf minhaj',
    author_email = 'ashraf_minhaj@yahoo.com',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'typer',
    ],
    entry_points='''
        [console_scripts]
        dockona=dockona.dockona:app
    ''',
)