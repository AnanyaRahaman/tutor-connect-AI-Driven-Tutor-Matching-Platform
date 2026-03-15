from django.urls import path
from .views import tutor_requests

urlpatterns = [

path("requests/",tutor_requests),

]