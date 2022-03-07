from django.urls import path
from . import views
from .views import RequestCreateView, RequestDetailView, RequestListView, RequestByZoneListView, InProgressView, \
    ResolvedView, ContactCreateView, ContactListView
from django.contrib import admin
admin.site.site_header="Waste Management System"
admin.site.site_title="Waste Management System"
admin.site.index_title="ADMIN PANEL"
urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("complaint/list", RequestListView.as_view(), name="CompList"),
    path("manager/complaint/list", RequestByZoneListView.as_view(), name="ManagerCompList"),
    path("complaint/", RequestCreateView.as_view(), name="complaint"),
    path("complaint/<int:pk>/", RequestDetailView.as_view(), name="request_detail"),
    path("complaint/status/processing/<int:pk>/", InProgressView.as_view(), name="inprocess"),
    path("complaint/status/resolved/<int:pk>/", ResolvedView.as_view(), name="resolved"),
    path("services/mechanicalSweeping", views.MechanicalSweeping, name="mechanicalSweeping"),
    path("services/WasteCollection", views.WasteCollection, name="wasteCollection"),
    path("services/MechanicalWashing", views.MechanicalWashing, name="mechanicalWashing"),

    # path("login/",views.Login, name="login"),
    # path("signup/",views.Signup,name="Signup"),
    path("services/", views.Services, name="services"),
    path('contact/', ContactCreateView.as_view(), name="contact"),
    path("messages/list", ContactListView.as_view(), name="ContactList"),
    path("Manager_panel/", views.ManagerPanel, name="managerPanel"),

]
