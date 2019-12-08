from django.shortcuts import render

# Create your views here.
import models

from django.views.generic import (
    TemplateView, DetailView, ListView, CreateView, UpdateView
)

class IndexView(TemplateView):
    template_name = 'job_management/index.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['companies'] = Company.objects.all().order_by('name', 'id')
        return context