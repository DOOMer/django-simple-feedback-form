#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup 

setup(
    name='django-simple-feedback-form',
    version=__import__('feedback_form').__version__,
    author='Artem Galichkin',
    author_email='doomer3d@gmail.com',
    packages=['feedback_form'],    
    url='https://github.com/DOOMer/django-simple-feedback-form',
    download_url='https://github.com/DOOMer/django-simple-feedback-form',
    license='LICENSE.txt',
    description='Simple feedback form for your django project.',
    long_description=open('README.rst').read(),
    install_requires=["Django >= 1.3.0",],
    include_package_data=True,
)