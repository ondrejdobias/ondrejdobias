from django.urls import path

from . import views

urlpatterns = {
    path('matrix/', views.models_list)
}

