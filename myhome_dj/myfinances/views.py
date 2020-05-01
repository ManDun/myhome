from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView


def index(request):

    return render(request, 'index.html')


def expensehome(request):

    return render(request, 'expenses/expenseshome.html')


def addexpense(request):

    return render(request, 'expenses/addexpense.html')


def incomeshome(request):

    return render(request, 'incomes/incomeshome.html')


def addincome(request):

    return render(request, 'incomes/addincome.html')

# Create your views here.
