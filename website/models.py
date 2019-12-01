# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import uuid
import os

def get_file_path(instance, filename):
    folder = "%s/%s" % (uuid.uuid4(),filename)
    return os.path.join('website/templates/uploads/',folder)

class Model(models.Model):
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    file = models.FileField(upload_to=get_file_path,
                        null=True,
                        blank=True,
                        verbose_name='Website')
    def filepath(self):
        return str(self.file).replace('website/templates/','')

    def __str__(self):
        return self.title
