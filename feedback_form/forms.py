
from django import forms
from django.conf import settings
from django.core.mail.message import EmailMessage
from django.template import loader
from django.utils.translation import ugettext_lazy as _
from feedback_form.settings import *
from django.contrib import messages
from django.http import HttpRequest

class BaseEmailFormObject(object):		
	#if settings.CONTACT_ADMINS_ONLY:
	if CONTACT_ADMINS_ONLY:
		recipient_list = [email for _, email in settings.ADMINS]
	else:
		recipient_list = [email for _, email in settings.MANAGERS]

	subject_template = 'feedback_form/email_subject.txt'
	message_template = 'feedback_form/email_template.txt'
	from_template = 'feedback_form/email_from.txt'

	def get_message(self):
		return loader.render_to_string(self.message_template, self.get_context())

	def get_from_email(self):
		return loader.render_to_string(self.from_template, self.get_context())

	def get_subject(self):
		subject = loader.render_to_string(self.subject_template, self.get_context())
		return ''.join(subject.splitlines())
		
	def get_request_meta(self):
		meta = {}
		meta['UP'] = self.request.META['REMOTE_ADDR']
		meta['USER_AGENT'] = self.request.META['HTTP_USER_AGENT']
		return meta	

	def get_context(self):
		if not self.is_valid():
			raise ValueError("Cannot generate Context when form is invalid.")
		data = self.cleaned_data
		if CONTACT_SEND_META_INFO:
			data['meta'] = self.get_request_meta()
		return data

	def get_message_dict(self):
		return {
			"from_email": self.get_from_email(),
			"to": self.recipient_list,
			"subject": self.get_subject(),			
			"body": self.get_message(),
		}

	def send_email(self, request, fail_silently=False):
		self.request = request

		if EmailMessage(**self.get_message_dict()).send(fail_silently=fail_silently):
			messages.success(request, _('Message is sent successufully!'))


class ContactForm(forms.Form, BaseEmailFormObject):
	"""
	Subclass this and declare your own fields.
	"""
	name = forms.CharField(label=_(u'Your name'), max_length=64)
	subject = forms.CharField(label=_(u'Subject'), max_length=128)
	email = forms.EmailField(label=_(u'Your email address'), max_length=200)
	body = forms.CharField(label=_(u'Your message'), widget=forms.Textarea(attrs={'cols':'30', 'rows':'5'}))