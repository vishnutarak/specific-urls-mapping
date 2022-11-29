from django.urls import path
from app2.views import *
app_name='vishnu' # we can provide any name.But we easly understand perpose function name and this name should be same.
urlpatterns=[
    path('a2_one/',a2_one,name='a2_one')
]