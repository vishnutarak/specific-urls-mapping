from django.urls import path
from app1.views import *
app_name='tarak'# we can provide any name.But we easly understand perpose function name and this name should be same.
urlpatterns=[
    path('a1_first/',a1_first,name='a1_first'),
]