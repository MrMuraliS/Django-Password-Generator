import random

from django.shortcuts import render
from .forms import HomePageForm
import string
from random import choice


# Create your views here.


def home(request):
    home_form = HomePageForm()
    if request.method == 'POST':
        form = HomePageForm(request.POST)
        if form.is_valid():
            target = form.cleaned_data
            values = []
            if target['Upper']:
                values.extend([*list(string.ascii_uppercase)])
            if target['Lower']:
                values.extend([*list(string.ascii_lowercase)])
            if target['Numbers']:
                values.extend(list('1234567890'))
            if target['Special']:
                values.extend(list('!@#$%^&*()'))
            else:
                values.extend(list(string.ascii_letters))

            password = ''.join([char for _ in range(target['Length']) for char in random.choice(values)])
            return render(request, 'password.html', {'password': password})

    return render(request, 'home.html', {'home_form': home_form})
