from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView, View
from .models import Hotel
from .forms import UserForm

class HotelListView(ListView):
    model = Hotel
    template_name = "hotel_list.html"

    def get_context_data(self, **kwargs):
        context = super(HotelListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return self.model.objects.all()

class UserFormView(View):
    form_class = UserForm
    Template = "registration_form.html"