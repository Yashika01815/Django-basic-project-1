from django.urls import path
from . import views
urlpatterns=[
 path('', views.index), #'' used because index is used as by default,
 path('instruction',views.instruction)
]