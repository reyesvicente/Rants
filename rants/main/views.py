from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Rant, Category


class RantListView(ListView):
    model = Rant
    template_name = 'main/rant_list.html'
    context_object_name = 'rants'


class RantDetailView(LoginRequiredMixin, DetailView):
    model = Rant