from atexit import register
from unicodedata import name
from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', csrf_exempt(views.Payment.as_view()), name="payment"),
]
