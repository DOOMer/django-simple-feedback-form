
from django import forms
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _
from .conf import CONTACT_SEND_META_INFO


class ContactFormBase(forms.Form):
    name = forms.CharField(label=_("Your name"), max_length=64)
    subject = forms.CharField(label=_("Subject"), max_length=129)
    email = forms.EmailField(label=_("Your email address"), max_length=200)
    body = forms.CharField(label=_("Your message"),
                           widget=forms.Textarea(attrs={'cols': '30', 'rows': '5'}))

    # Non field members
    subject_template = 'feedback_form/email_subject.txt'
    message_template = 'feedback_form/email_template.txt'
    request_meta: dict = None  # request.META

    def __init__(self, request_meta, *args, **kwargs):
        self.request_meta = request_meta
        super().__init__(*args, **kwargs)

    def prepare_mail(self) -> dict:
        mail_dict = {
            'subject': self.get_subject(),
            'message': self.get_message(),
        }
        return mail_dict

    def get_subject(self) -> str:
        return render_to_string(self.subject_template, {'subject': self.cleaned_data['subject'], })

    def get_request_meta(self) -> dict:
        meta = {'IP': self.request_meta['REMOTE_ADDR'], 'USER_AGENT': self.request_meta['HTTP_USER_AGENT']}
        return meta

    def get_message(self) -> str:
        message_context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'subject': self.get_subject().strip(),
            'body': self.cleaned_data['body'],
        }

        if CONTACT_SEND_META_INFO:
            message_context['meta'] = self.get_request_meta()

        return render_to_string(self.message_template, message_context)