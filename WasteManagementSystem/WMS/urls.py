from django.urls import path
from . import views
from .views import RequestCreateView,RequestDetailView,RequestListView
urlpatterns = [
    path("",views.home, name="home"),
    path("about/", views.about, name="about"),
    path("complaint/list",RequestListView.as_view(), name="CompList"),
    path("complaint/",RequestCreateView.as_view(), name="complaint"),
    path("complaint/<int:pk>/",RequestDetailView.as_view(), name="request_detail"),
    path("services/mechanicalSweeping",views.MechanicalSweeping, name="mechanicalSweeping"),
    path("services/WasteCollection",views.WasteCollection, name="wasteCollection"),
    path("services/MechanicalWashing",views.MechanicalWashing, name="mechanicalWashing"),

    #path("login/",views.Login, name="login"),
    #path("signup/",views.Signup,name="Signup"),
    path("services/",views.Services, name="services"),
    path('contact/',views.Contact,name="contact")
]
