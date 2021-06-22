from django.urls import path
from django.urls.resolvers import URLPattern
from .views import *


app_name = "cmsapp"

urlpatterns = [
    path("", IndexView),
    #teacher
    path("teacher/home/", TeacherHomeView.as_view(), name="teacherhome"),
    path("teacher/signup/", TeacherSignupView.as_view(), name="teachersignup"),
    path("teacher/logout/", TeacherLogoutView.as_view(), name="teacherlogout"),
    path("teacher/login/", TeacherLoginView.as_view(), name="teacherlogin"),

    #student
    path("student/home/", StudentHomeView.as_view(), name="studenthome"),
    path("student/signup/", StudentSignupView.as_view(), name="studentsignup"),
    path("student/login/", StudentLoginView.as_view(), name="studentlogin"),
    path("student/logout/", StudentLogoutView.as_view(), name="studentlogout"),




]