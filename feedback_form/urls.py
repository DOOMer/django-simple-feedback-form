from django.conf.urls import url, patterns
from feedback_form import views

urlpatterns = patterns('',
                       url(r'^$', views.ContactFormView.as_view(), name="feedback"),
                       url(r'^$', views.CompletedPage.as_view(), name="completed"),
)
