from django.urls import path
from .views import *

urlpatterns = [
    path("advocate_list/", advocate_list),
    # path("advocate_detail/<str:username>/", advocate_detail),
    path("advocate_detail/<str:username>/", AdvocateDetail.as_view()),
]
