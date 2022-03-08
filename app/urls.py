from unicodedata import name
from django.urls import path,include
from .import views

urlpatterns = [
    path("",views.Insert,name="insert"),
    path('insert/',views.InsertData,name="insertdata"),
    path('show/',views.Show,name="showdata"),
    path('edit/<int:pk>',views.Edit,name='editdata'),
    path('update/<int:pk>',views.Update,name='updatedata'),
    path('delete/<int:pk>',views.Delete,name='deletedata')
]
