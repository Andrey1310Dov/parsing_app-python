from setuptools import setup, find_packages
from os.path import join, dirname
import parsing_app

setup(
    name='parsing_app',
    version=parsing_app.__version__,
    packages=find_packages(),
    test_suite='test',
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
    entry_points={
        'console_scripts':
        ['parsing = parsing_app.parsing_app:start']
        }
)
