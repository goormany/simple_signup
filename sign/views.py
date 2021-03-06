from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'
