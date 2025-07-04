
from django.urls import path
from .views import HtmlFileSendView

urlpatterns = [
    path('get-html/', HtmlFileSendView.as_view(), name='get-html'),
]
