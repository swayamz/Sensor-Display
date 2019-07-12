from django.urls import path
from django.conf.urls import url

from . import views
from .views import getJSONdata

urlpatterns = [
    path('',views.home, name='home'),
    url(r'^api/getJSONdata', getJSONdata, name='getJSONdata')

]