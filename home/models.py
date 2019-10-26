# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ArticleTab(models.Model):
	id = models.BigAutoField(primary_key=True)
	title = models.CharField(max_length=128,default="")
	author = models.CharField(max_length=128,default="")
	create_time = models.PositiveIntegerField(default=1218154088)
	update_time = models.PositiveIntegerField(default=1218154088)
	body = models.TextField(default="")

	class Meta:
		db_table = 'article_tab'


		