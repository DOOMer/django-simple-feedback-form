
from django.contrib import messages
from django.core.mail import mail_admins, mail_managers
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from .conf import CONTACT_ADMINS_ONLY
from .forms import ContactFormBase


class FeedbackBaseView(FormView):
    """
    Form view that sends email when form is valid. You can subclass it
    and define your own form_class, success_message, success_url and template_name.

    Attributes:
        cls.form_class: Django form class for use to create feedback message. The form must be subclassed from
        'ContactFormBase' at this app.
        cls.success_message (str): Django form class for use to create feedback message.
        cls.success_url (str): URl to redirect user when feedback is sent successfully.
        cls.template_name (str): Name of template file for this view.

    """
    form_class = ContactFormBase
    success_message = _("Message is sent successfully")
    success_url = reverse_lazy('feedback-view')
    template_name = "feedback_form/feedback.html"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        kwargs.update({'request_meta': self.request.META, })

        return kwargs

    def form_valid(self, form):
        mail_data = form.prepare_mail()
        self.send_mail(mail_data)
        return super().form_valid(form)

    def send_mail(self, data: dict):
        if CONTACT_ADMINS_ONLY:
            mail_admins(data['subject'], data['message'])
        else:
            mail_managers(data['subject'], data['message'])
        messages.success(self.request, self.get_success_message())

    def get_success_message(self) -> str:
        return self.success_message


class FeedbackView(FeedbackBaseView):
    pass
