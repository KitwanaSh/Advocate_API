from django.urls import path
from .views import *

urlpatterns = [
    path("advocates/", advocate_list),
    # path("advocate_detail/<str:username>/", advocate_detail),
    path("advocate_detail/<str:username>/", AdvocateDetail.as_view()),
    path("companies/", company_list)
]
