from distutils.core import setup
from setuptools import find_packages

setup(name='ul23utyn',
    version='0.1',
    author='DSSS', 
    author_email='belen.lojo@fau.de',   
    packages=find_packages(),   
    install_requires=['numpy', 'Pillow', 'ipywidgets'])