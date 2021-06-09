from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView
from third_app import models


# Create your views here.
class IndexView(TemplateView):
    context_object_name = 'people_list'
    model = models.People
    template_name = 'third_app/index.html'
