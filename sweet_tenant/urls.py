from django.urls import path
from .views import SweetList

urlpatterns = [
    path('sweets/', SweetList.as_view()),
]
