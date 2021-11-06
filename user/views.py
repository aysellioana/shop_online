from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from user.models import ExtendUser
from user.forms import UserForm

class UserCreateView(CreateView):
    template_name = 'create_user.html'
    model = ExtendUser
    form_class = UserForm
    success_url = reverse_lazy('create-user')
    # form_class = UserForm

