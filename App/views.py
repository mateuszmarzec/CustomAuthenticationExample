from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from App.forms import SignUpForm


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('signin-view')
    template_name = 'signup.html'


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
