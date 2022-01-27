Advanced usage
==============

Using without including 'feedback.forms.urls'
---------------------------------------------

You can directly use FeedbackView in your 'urls.py' module, without including 'feedback_form.urls' in the main
urlconf of your project.

    from feedback_form.views import FeedbackView

And use it in the urlpattern^

    path('feedback/', FeedbackView.as_view(), name='feedback-view'),

.. warning:: Name of your urlpattern must be a 'feedback-view', because there is a reference to this name in the code of view.