===========================
Django Simple Feedback Form
===========================

This `Django <http://djangoproject.com>`_ app has for provide simple form for sending mail forom users to admins your django-based site.

Requirements
------------

Django 3.0+

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

Using in your project
---------------------
  
Add *'feedback_form'* to your INSTALLED_APPS in settings.py,

  INSTALLED_APPS = (
    ...
    
    'feedback_form',

  )
  
Add *'feedback_form.urls'* in your main urls configuration::

  path('feedback/', include("feedback_form.urls", namespace="feedback_form")),
  
and add in your template add link to feedback view::

  <a href="{% url 'feedback_form:feedback' %}">Feedback form</a>
  
And override the template "feedback_form/feedback.html" for your site.

Additional settings 
-------------------

You can override these settings in your main settngs.py file:

**CONTACT_ADMINS_ONLY** - send email only to users which added in ADMINS tuple. By default is enabled. If it is a disabled, send to MANAGERS mails too.

**CONTACT_SEND_META_INFO**- send meta information about user (IP and user-agent). By default is disabled.
