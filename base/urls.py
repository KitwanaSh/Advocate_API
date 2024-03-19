from django.urls import path
from .views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    # TokenRefreshView,
)

urlpatterns = [
    path("advocates/", advocates),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # path("advocate_detail/<str:username>/", advocate_detail),
    path("advocate_detail/<str:username>/", AdvocateDetail.as_view()),
    path("companies/", company_list)
]
