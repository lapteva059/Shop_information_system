from django.shortcuts import render
from .forms import AuthorizationForm


def landing(request):
    name = "Belle"
    current_day = "13.11.2018"
    form = AuthorizationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["email"])

    return render(request, 'landing/landing.html', locals())

