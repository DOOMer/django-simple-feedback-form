
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, CreateView, FormView

from django.shortcuts import render_to_response
from django.template import RequestContext

from feedback_form import forms

class CompletedPage(TemplateView):
    template_name = "feedback_form/feedback_done.html"

class ContactFormMixin(object):
    """
    Form view that sends email when form is valid. You'll need
    to define your own form_class and template_name.
    """    
    def form_valid(self, form):
        form.send_email(self.request)
        return super(ContactFormMixin, self).form_valid(form)

    def get_success_url(self):		
        return reverse("feedback_form:completed")

	def get_context_data(self, **kwargs):
		context = super(ContactFormObject, self).get_context_data(**kwargs)
		return context
	
class ContactFormView(ContactFormMixin, FormView):
  template_name="feedback_form/feedback.html"
  form_class=forms.ContactForm
