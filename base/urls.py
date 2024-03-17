from django.urls import path
from .views import *

urlpatterns = [
    path("advocate_list/", advocate_list)
]
