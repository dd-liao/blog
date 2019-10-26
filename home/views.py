# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import home.models

# Create your views here.

def index(request):
	context = {}
	context['docs'] = ['doc1','doc2','doc3']
	return render(request, 'home.html', context)
