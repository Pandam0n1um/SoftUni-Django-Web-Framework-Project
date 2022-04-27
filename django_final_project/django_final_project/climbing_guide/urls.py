from django.urls import path, include

from django_final_project.climbing_guide.views import HomeView

urlpatterns = (
    path('', HomeView.as_view(), name='index'),
)
