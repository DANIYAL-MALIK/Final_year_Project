from django.urls import path
from . import views
urlpatterns = [
    path("",views.home, name="home"),
    path("about/", views.about, name="about"),
    path("complaint/",views.Complaint, name="complaint"),
    #path("login/",views.Login, name="login"),
    path("signup/",views.Signup,name="Signup"),
    path("services/",views.Services, name="services"),
    path('contact/',views.Contact,name="contact")
]
