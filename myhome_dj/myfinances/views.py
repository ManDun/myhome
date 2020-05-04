from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView
from myfinances import forms
from myfinances.models import Files


def index(request):

    return render(request, 'index.html')


def expensehome(request):

    return render(request, 'expenses/expenseshome.html')


def addexpense(request):
    form = forms.ExpenseForm()

    if request.method == 'POST':
        form = forms.ExpenseForm(request.POST, request.FILES)

        if form.is_valid():
            print('POST')
            print(form.cleaned_data['name'])
            Files.name = request.FILES['bill']
            form.instance.user = request.user
            form.save(commit=True)
            print(request.FILES['bill'])

    return render(request, 'expenses/addexpense.html', {'form': form})


def incomeshome(request):

    return render(request, 'incomes/incomeshome.html')


def addincome(request):

    return render(request, 'incomes/addincome.html')

# Create your views here.
