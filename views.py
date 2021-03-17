from django.http import HttpResponse
from .forms import SnippetForm
from django.shortcuts import render


def snippet_detail(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()

    form = SnippetForm()
    return render(request, 'form.html', {'form': form})