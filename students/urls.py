from django.urls import path
from . import views



urlpatterns = [
    
    path("",views.home, name="home"),
    path("student_register/", views.regi_form, name='student_regi'),
    path('studentinfo/',views.StudentOp.as_view(), name="student_add"),
    path('studentDetail/<int:pk>', views.StudentDetails.as_view({ 'delete': 'del_std'}), name="student_pk"),
    path('student_edit/<int:pk>', views.StudentEdit, name="edit_student"),
    

]