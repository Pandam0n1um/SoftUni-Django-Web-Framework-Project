from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth import views as auth_views, login
from django.urls import reverse_lazy
from django.views import generic as views

# from django.contrib import mixins as auth_mixins
# Create your views here.
from django_final_project import settings
from django_final_project.authentication.forms import UserRegistrationForm
from django_final_project.authentication.models import Profile


class UserRegisterView(views.CreateView):
    form_class = UserRegistrationForm
    template_name = 'authentication/user_registration.html'
    success_url = reverse_lazy('index')

    def form_valid(self, *args, **kwargs):
        result = super().form_valid(*args, **kwargs)
        login(self.request, self.object)
        return result


class UserLoginView(auth_views.LoginView):
    template_name = 'authentication/user_login.html'
    success_url = reverse_lazy('index')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserLogoutView(auth_views.LogoutView):
    next_page = settings.LOGOUT_REDIRECT_URL


class RestrictedView(auth_mixins.LoginRequiredMixin, views.TemplateView):
    template_name = 'index.html'


class UserDetailsView(views.DetailView):
    model = Profile
    template_name = 'authentication/user_details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'is_owner': self.object.user_id == self.request.user.id,
        })

        return

