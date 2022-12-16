from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from django.views.generic import ListView
from .models import CustomUser
from .forms import CustomUserCreationForm
from .forms import CustomUserChangeForm


class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class ProfileView(generic.DetailView):
    model = CustomUser
    template_name = 'users/profileView.html'
    success_url = reverse_lazy('login')
    context_object_name = 'profile' 

class EditAccountView(generic.UpdateView):
    form_class = CustomUserChangeForm
    model = CustomUser
    context_object_name = 'createAccount'
    template_name = 'users/createAccount.html' #

class AuthorsView(ListView):
    model = CustomUser
    template_name = 'users/viewAuthors.html'

    def get_queryset(self):
        return CustomUser.object.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = CustomUser.objects.all()
        return context