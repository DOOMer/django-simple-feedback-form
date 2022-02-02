# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['feedback_form', 'feedback_form.migrations']

package_data = \
{'': ['*'], 'feedback_form': ['templates/feedback_form/*']}

install_requires = \
['django>=3.0']

setup_kwargs = {
    'name': 'django-simple-feedback-form',
    'version': '2.0.1',
    'description': 'This is a Django application for providing a simple form for users to send emails to the administrators of your django-based site.',
    'long_description': '===========================\nDjango Simple Feedback Form\n===========================\n\nThis `Django <http://djangoproject.com>`_ app has for provide simple form for sending mail forom users to admins your django-based site.\n\nRequirements\n------------\n\nDjango 3.0+\n\n\nInstallation and configuration\n------------------------------\n\nSee `setup part`_ in documentation.\n\n.. _setup part: https://django-simple-feedback-form.readthedocs.io/en/latest/setup.html\n\nUsage\n-----\n\nSee `usage part`_ in documentation.\n\n.. _usage part: https://django-simple-feedback-form.readthedocs.io/en/latest/usage.html\n\n\nLicense\n-------\n\nLicensed under BSD license. See `license link`_ in documentation.\n\n.. _license link: LICENSE.rst',
    'author': 'Artem Galichkin',
    'author_email': 'doomer3d@gmail.com',
    'maintainer': 'Artem Galichkin',
    'maintainer_email': 'doomer3d@gmail.com',
    'url': 'https://github.com/DOOMer/django-simple-feedback-form',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
