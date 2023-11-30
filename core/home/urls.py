from django.urls import path
# from .views import apiTest

from .views import TestClass

urlpatterns = [
    path('test', TestClass.as_view()),
]   