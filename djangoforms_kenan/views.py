from django.shortcuts import render
from .forms import Contact_form


def contact(request):
    if request == 'POST':
        form = Contact_form(request.POST)
        if form.is_valid():
            return render(request, 'success.html')
    else:
        form = Contact_form
        return render(request, 'contact.html', {'form': form})
