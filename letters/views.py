from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView

from .models import Letter
# from .forms import LetterForm

# @login_required
# def letters(request):
#     letters = Letter.objects.all()
#
#     return render(request, 'letters/letters.html', {'letters': letters})


class LetterListView(LoginRequiredMixin, ListView):
    model = Letter
    template_name = 'letters/letters.html'
    context_object_name = 'letters'
    ordering = '-time'
    paginate_by = 5


class LetterCreateView(LoginRequiredMixin, CreateView):
    model = Letter
    fields = ['recipient', 'text']
    template_name = 'letters/letter.html'

    def form_valid(self, form):
        form.instance.sender = self.request.user
        return super().form_valid(form)


class LetterDetailView(LoginRequiredMixin, DetailView):
    model = Letter
    template_name = 'letters/letter_id.html'
    context_object_name = 'letter_id'

