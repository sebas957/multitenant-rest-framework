from django.urls import path
from .views import SweetTypeList

urlpatterns = [
    path('sweets/', SweetTypeList.as_view()),
]
