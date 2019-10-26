# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from home.models import ArticleTab

from django.http import HttpResponse

import time

# Create your views here.

def index(request):
	article_list = ArticleTab.objects.all()

	for article in article_list:
		#转换成localtime
		time_local = time.localtime(article.update_time)
		#转换成新的时间格式(2016-05-05 20:28:54)
		dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
		article.update_time = dt


	context = {}
	context['article_list'] = article_list
	
	return render(request, 'home.html', context)
