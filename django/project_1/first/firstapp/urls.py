from importlib.resources import path
from xml.etree.ElementInclude import include
from django.urls import path

from . import views
#now import the views.py file into this code

urlpatterns=[
  path('',views.Form,name='Form'),
  path('table/',views.table,name='Table')
  ]
 