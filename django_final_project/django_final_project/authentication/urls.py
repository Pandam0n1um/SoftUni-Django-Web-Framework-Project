from django.urls import path

from django_final_project.authentication.views import UserLoginView, UserLogoutView, UserDetailsView, UserRegisterView

urlpatterns = (
    path('register/', UserRegisterView.as_view(), name='register user'),
    path('login/', UserLoginView.as_view(), name='login user'),
    path('logout/', UserLogoutView.as_view(), name='logout user'),
    path('<int:pk>/', UserDetailsView.as_view(), name='profile details'),
    # path('restricted/', RestrictedView.as_view(), name='restricted'),
)
