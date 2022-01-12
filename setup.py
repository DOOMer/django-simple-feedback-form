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
    'version': '2.0.dev0',
    'description': 'This is a Django application for providing a simple form for users to send emails to the administrators of your django-based site.',
    'long_description': '===========================\nDjango Simple Feedback Form\n===========================\n\nThis `Django <http://djangoproject.com>`_ app has for provide simple form for sending mail forom users to admins your django-based site.\n\nRequirements\n------------\n\nDjango 3.0+\n\nInstallation \n------------\n \nInstall into your python path using pip or github version::\n\n  pip install django-simple-feedback-form\n\nor::\n  \n  pip install git+https://github.com/DOOMer/django-simple-feedback-form.git\n\nPreparing your project\n----------------------\n\nAdd ADMINS list to your settings.py, like that:\n\n    ADMIN = [\n        (\'John\', \'john@example.com\'), (\'Mary\', \'mary@example.com\')\n    ]\n\nIn addition, you can add MANAGERS list to your settings.py, like that^\n\n    MANAGERS = [\n        (\'John\', \'john@example.com\'), (\'Mary\', \'mary@example.com\')\n    ]\n\nUsing in your project\n---------------------\n  \nAdd *\'feedback_form\'* to your INSTALLED_APPS in settings.py,\n\n  INSTALLED_APPS = (\n    ...\n    \n    \'feedback_form\',\n\n  )\n  \nAdd *\'feedback_form.urls\'* in your main urls configuration::\n\n  path(\'feedback/\', include("feedback_form.urls", namespace="feedback_form")),\n  \nand add in your template add link to feedback view::\n\n  <a href="{% url \'feedback_form:feedback\' %}">Feedback form</a>\n  \nAnd override the template "feedback_form/feedback.html" for your site.\n\nAdditional settings \n-------------------\n\nYou can override these settings in your main settngs.py file:\n\n**CONTACT_ADMINS_ONLY** - send email only to users which added in ADMINS tuple. By default is enabled. If it is a disabled, send to MANAGERS mails too.\n\n**CONTACT_SEND_META_INFO**- send meta information about user (IP and user-agent). By default is disabled.\n',
    'author': 'Artem Galichkin',
    'author_email': 'doomer3d@gmail.com',
    'maintainer': 'Artem Galichkin',
    'maintainer_email': 'doomer3d@gmail.com',
    'url': 'https://github.com/DOOMer/django-simple-feedback-form',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
