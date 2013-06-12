
from django.conf.urls.defaults import url, patterns
from feedback_form import views

urlpatterns = patterns('',
    url(r'^$', views.ContactFormView.as_view(), name="feedback"),
	url(r'^$', views.ContactFormView.as_view(), name="completed"),    
)