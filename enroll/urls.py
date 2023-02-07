from django.urls import path
from .import views
urlpatterns = [
    path('',views.Signup_det, name='Signup'),
    path('success/',views.stu_details, name='Success'),
    path('delete/<int:id>/',views.delete_data, name='Deletedata'),
    path('update/<int:id>/',views.update_data,name='Update')
]