from django.urls import path
from .views import SweetTypeList

urlpatterns = [
    path('sweettypes/', SweetTypeList.as_view()),
]
