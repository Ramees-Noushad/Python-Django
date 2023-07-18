from . import views
from django.urls import include, path

urlpatterns=[
    path('',views.home,name='home'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvhome/',views.listview.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>',views.detailveiw.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>',views.updateview.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>',views.deleteview.as_view(),name='cbvdelete'),
]