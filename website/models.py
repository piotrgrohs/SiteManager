# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.


class Model(models.Model):
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    file = models.FileField(upload_to='website/templates/uploads/', default='upload file' )

    def __str__(self):
        return self.title
