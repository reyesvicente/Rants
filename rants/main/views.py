from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Rant


class HomePageView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_rant'] = Rant.objects.all()[:4]
        return context


class RantListView(ListView):
    model = Rant
    template_name = 'main/rant_list.html'
    context_object_name = 'rants'


class RantDetailView(LoginRequiredMixin, DetailView):
    model = Rant