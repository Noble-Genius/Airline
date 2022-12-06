from django.urls import path
from . import views
urlpatterns = [
	path('', views.home, name = "home"),
	path('our-flight/', views.flight_create, name="our_flight"),
	path('new-passenger/', views.passenger_create, name="new_passenger"),
	path('group-members/', views.group_members, name="group_members"),
]
