from django.http import HttpResponse
from django.urls import path

from .views import *

urlpatterns = [
    path('users/', lambda r: HttpResponse('<h1> hello, user </h1>')),
    path('groups/', lambda r: HttpResponse('<h1> hello, group </h1>')),
]
