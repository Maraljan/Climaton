from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'climaton_app/home_page.html'


# Create your views here.
