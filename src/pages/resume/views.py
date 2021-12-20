from django.urls import reverse_lazy
from django.views.generic import CreateView
from pages.resume import forms


class ResumeView(CreateView):
    form_class = forms.ResumeForm
    success_url = reverse_lazy('pages:login')
    template_name = 'pages/resume.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
