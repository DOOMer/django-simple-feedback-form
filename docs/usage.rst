Usage
=====

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

  <a href="{% url 'feedback_form:feedback-view' %}">Feedback form</a>

And override the template on path "feedback_form/feedback.html" for your site.

Additional settings
-------------------

You can override these settings in your main settngs.py file:

**CONTACT_ADMINS_ONLY** - send email only to users which added in ADMINS tuple. By default is enabled. If it is a disabled, send to MANAGERS mails too.

**CONTACT_SEND_META_INFO**- send meta information about user (IP and user-agent). By default is disabled.
