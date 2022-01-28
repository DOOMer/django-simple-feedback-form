
.. module:: feedback_form.views

Built-in view classes
=====================

.. class:: FeedbackView

    The base view class from which most custom contact-form views should inherit. If you don't need any custom
    functionality, and it is inherited from the  :class:`~feedback_form.views.FeedbackBaseView` class.

    You can also use it as-is (and the provided URLConf, `feedback_form.urls`, does exactly this).

.. class:: FeedbackBaseView

    The base view class from which most custom contact-form views should inherit. If you don't need any custom
    functionality, and are content with the default :class:`~feedback_form.forms.ContactFormBase` class.

    This is a subclass of Django's :class:`~django.views.generic.edit.FormView`, so refer to the
    Django documentation for a list of attributes/methods which can be overridden to customize behavior.

    The following standard (from :class:`~django.views.generic.edit.FormView`) methods and
    attributes are commonly useful to override (all attributes below can also be passed to
    :meth:`~django.views.generic.base.View.as_view()` in the URLconf, permitting customization without
    the need to write a full custom subclass of this class):

    .. attribute:: form_class

        The form class to use. By default, will be :class:`~feedback_form.forms.ContactForm`.
        This can also be overridden as a method named :meth:`~django.views.generic.edit.FormMixin.form_class`;
        this permits, for example, per-request customization (by inspecting attributes of `self.request`).

.. attribute:: success_message

        A :class:`str`, the text, which displayed to user, after successful form submission. By default,
        will be "Message is sent successfully".

.. attribute:: success_url

       A :class:`str`, the name of urlpattern to redirect to after successful form submission.

.. attribute:: template_name

       A :class:`str`, the template to use when rendering the form. By
       default, will be `feedback_form/feedback.html`.

.. py:method:::: get_form_kwargs

       Returns additional keyword arguments (as a dictionary) to pass
       to the form class on initialization.

       By default, this will return a dictionary containing the
       current :class:`~django.http.HttpRequest` :attr:'META' (as the key
       `request_meta`).

       .. warning:: If you override :meth:`get_form_kwargs`, you
          **must** ensure that, at the very least, the keyword
          argument `request_meta` is still provided, or
          :class:`~feedback_form.forms.ContactFormBase` initialization will
          raise :exc:`TypeError`. The easiest approach is to use
          :func:`super` to call the base implementation in
          :class:`FeedbackbaseView`, and modify the dictionary it
          returns.

       :rtype: dict
