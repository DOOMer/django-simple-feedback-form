
from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ImproperlyConfigured
from django.core.mail import mail_admins, mail_managers
from django.views.generic import FormView
from django.urls import reverse
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
    success_url = 'feedback-view'
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
        result, counts = self._check_receivers_list()

        if result:
            if CONTACT_ADMINS_ONLY:
                if counts[0] > 0:
                    mail_admins(data['subject'], data['message'])
                else:
                    self._raise_config_exception(counts)
            else:
                mail_managers(data['subject'], data['message'])
            messages.success(self.request, self.get_success_message())
        else:
            self._raise_config_exception(counts)

    def get_success_message(self) -> str:
        return self.success_message

    def get_success_url(self):
        return reverse(self.success_url)

    def _check_receivers_list(self) -> (bool, (int, int, )):
        """ Check settings ADMINS and MANAGERS is non empty """
        admin = len(settings.ADMINS)
        managers = len(settings.MANAGERS)

        result = True if admin + managers > 0 else False
        return result, (admin, managers, ),

    def _raise_config_exception(self, counts: tuple):
        """ Raise ImproperlyConfigured with messages about non configured ADMINS or MANAGERS lists """
        r_substr = '__receivers__'
        msg = f"You must add {r_substr} list variable in 'settings' module of your project."
        if CONTACT_ADMINS_ONLY:
            if counts[0] == 0:
                msg = msg.replace(r_substr, 'ADMINS')
        else:
            if counts[0] + counts[1] == 0:
                msg = msg.replace(r_substr, 'ADMINS or MANAGERS')

        raise ImproperlyConfigured(msg)


class FeedbackView(FeedbackBaseView):
    pass
