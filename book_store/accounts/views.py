from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import CustomUserCreationForm


class Registration(FormView):
    form_class = CustomUserCreationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super(Registration, self).form_valid(form)
