from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from . import forms
# Create your views here.
class SignUp(generic.CreateView):
    form_class = forms.UserCreateForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')
