from django.urls import path
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    path('secret/', TemplateView.as_view(template_name="info/secret.html")),
    path('', profile, name='home'),
]
