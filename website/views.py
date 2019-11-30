# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Model
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['models'] = Model.objects.all()
        return context

class AboutPageView(TemplateView):
    template_name = 'about.html'

def file_detail(request, pk):
    file = get_object_or_404(Model, pk=pk)
    return render(request, 'file_detail.html', {'file': file})
    

