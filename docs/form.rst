
.. module:: feedback_form.forms

Built-in form classes
=====================

You can create your own form inherited from the Base Form class. And then pass your new class as the value of the
"form_class" parameter to the **FeedbackView.as_view()** call.

ContactFormBase class
-----------------

.. class:: ContactFormBase

    The base contact form class from which all contact form classes should inherit.
    It will collect name, email address and message. You can to override this class attributes:

    .. attribute:: subject_template

        A :class:`str`, the name of the template to use when rendering the subject line of the message.
        By default, this is `feedback_form/email_subject.txt`.

    .. attribute:: message_template

        A :class:`str`, the name of the template to use when rendering the body of the message.
        By default, this is `feedback_form/email_template.txt`.


    And two methods are involved in producing the contents of the message to send:

    .. py:method:: get_message

        Returns the body of the message to send. By default, this is accomplished by rendering the template
        name specified in :attr:`message_template`.

        :rtype: str

    .. py:method:: get_subject

        Returns the subject line of the message to send. By default, this is accomplished by rendering the template
        name specified in :attr:`subject_template`.

       :rtype: str

    .. py:method:: **Subject must be a single line**

       The subject of an email is sent in a header (named
       `Subject:`). Because email uses newlines as a separator between
       headers, newlines in the subject can cause it to be interpreted
       as multiple headers; this is the `header injection attack
       <https://en.wikipedia.org/wiki/Email_injection>`_. To prevent
       this, :meth:`subject` will always force the subject to a single
       line of text, stripping all newline characters. If you override
       :meth:`subject`, be sure to either do this manually, or use
       :func:`super` to call the parent implementation.


    .. py:method:: prepare_mail

        This method loops through :meth:`get_message` and :meth:`get_subject`, collecting those parts into
        a dictionary with keys corresponding to the arguments to Django's `mail_admins` function, then returns the
        dictionary. Overriding this allows essentially unlimited customization of how the message is
        generated.

        :rtype: dict

    .. py:method:: get_request_meta

        Returns the selected metadata from the :attr:`request_meta`. It is used if *CONTACT_SEND_META_INFO* is True
        in 'settings' module of the your project.

        :rtype: dict

    Meanwhile, the following attributes/methods generally should not be overridden; doing so may interfere
    with functionality, may not accomplish what you want, and generally any desired customization can be
    accomplished in a more straightforward way through overriding one of the attributes/methods listed above.

    .. attribute:: request_meta

        The dict with some meta data from :class:`~django.http.HttpRequest` object representing the current request.
        This is set automatically in `__init__()`, and  is used if *CONTACT_SEND_META_INFO* is True in 'settings' module
        of the your project.