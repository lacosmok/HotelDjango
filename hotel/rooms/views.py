from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from .models import Hotel, Reservation
from .forms import UserForm
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

class ReservationCreateView(CreateView):
    model = Reservation
    template_name = "registration_form.html"

    def get_context_data(self, **kwargs):
        context = super(ReservationCreateView, self).get_context_data(**kwargs)
        context['reservation_create'] = True
        return context

    def form_valid(self, form, **kwargs):
        context = super(ReservationCreateView, self).form_valid(form, **kwargs)
        form.save()
        return context


@method_decorator(login_required, name='dispatch')
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
    template_name = "registration_form.html"

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user.set_password(password)
            user.save()

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')