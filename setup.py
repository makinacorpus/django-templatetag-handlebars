import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name='django-templatetag-handlebars',
    version='1.0.1',
    author='Mathieu Leplatre',
    author_email='mathieu.leplatre@makina-corpus.com',
    url='https://github.com/makinacorpus/django-templatetag-handlebars',
    download_url = "http://pypi.python.org/pypi/django-templatetag-handlebars/",
    description="Easily embed Handlebars.js templates in your django templates",
    long_description=open(os.path.join(here, 'README.rst')).read(),
    install_requires=[],
    packages=find_packages(),
    package_data = {
        '': ['*.js', '*.html'],
    },
    classifiers  = ['Topic :: Utilities', 
                    'Natural Language :: English',
                    'Operating System :: OS Independent',
                    'Intended Audience :: Developers',
                    'Environment :: Web Environment',
                    'Framework :: Django',
                    'Development Status :: 5 - Production/Stable',
                    'Programming Language :: Python :: 2.7'],
)
