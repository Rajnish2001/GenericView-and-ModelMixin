from django.urls import path
from .import views

urlpatterns = [
    path('lcstudentapi/',views.LCStudent.as_view()),
    # path('studentcreate/',views.StudentCreate.as_view()),
    path('rustudent/<int:pk>/',views.RUStudent.as_view()),
    # path('studentupdate/<int:pk>/',views.StudentUpdate.as_view()),
    path('studentdestroy/<int:pk>/',views.StudentDestroy.as_view()),
]
