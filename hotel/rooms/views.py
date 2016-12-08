from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from .models import Hotel

class HotelListView(ListView):
    model = Hotel

    def get_context_data(self, **kwargs):
        context = super(HotelListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return self.model.objects.all()