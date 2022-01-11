
from django.urls import path
from .views import FeedbackView

urlpatterns = [
    path('', FeedbackView.as_view(), name='feedback-view'),
]