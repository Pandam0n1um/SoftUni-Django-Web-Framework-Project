from django.views import generic as views


# Create your views here.

class HomeView(views.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['hide_additional_nav_items'] = True
        return context
