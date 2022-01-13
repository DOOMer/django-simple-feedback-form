Setup
=====

Installation
------------

Install into your python path using pip or github version::

  pip install django-simple-feedback-form

or::

  pip install git+https://github.com/DOOMer/django-simple-feedback-form.git

Preparing your project
----------------------

Add ADMINS list to your settings.py, like that:

    ADMIN = [
        ('John', 'john@example.com'), ('Mary', 'mary@example.com')
    ]

In addition, you can add MANAGERS list to your settings.py, like that^

    MANAGERS = [
        ('John', 'john@example.com'), ('Mary', 'mary@example.com')
    ]

**IMPORTANT**: If you don't, you will get an exception (ImproperlyConfigured with message \You must add ADMINS list
variable in 'settings' module of your project'.) when sending mail.