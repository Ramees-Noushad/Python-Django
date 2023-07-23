from . import views
from django.urls import path

urlpatterns = [
    path('',views.index, name= 'home'),
    # path('add/',views.addition,name='addition'),
    # path('contact/',views.contact,name='contact')
]
