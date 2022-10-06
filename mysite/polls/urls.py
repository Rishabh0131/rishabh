from django.urls import path,include

from rest_framework import routers
from .views import Questionsviewset

router =routers.DefaultRouter()

router.register(r'Names',Questionsviewset)

urlpatterns = [
    path('', include(router.urls)),
    path('polls-auth',include('rest_framework.urls'))
]

