from django.urls import path
from projectInformation import views

urlpatterns = [
    path("get_project_list/", views.get_project_list),
    path("filter_projects/", views.filter_projects),
]
