from django.urls import path
from lunchgroups import views

urlpatterns = [
    path('all/', views.get_all_lunch_groups),
    path('runner/', views.runner_lunch_group),
]