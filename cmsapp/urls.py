from django.urls import path
from django.urls.resolvers import URLPattern
from .views import *


app_name = "cmsapp"

urlpatterns = [
    path("", IndexView),
]