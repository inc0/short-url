# -*- coding: utf-8 -*-
from django.db import models
from utils import generate_suffix
from django.conf import settings


class Url(models.Model):
    original_url = models.URLField(verbose_name=u"original url")
    suffix = models.CharField(verbose_name=u"url suffix", max_length=10, unique=True)
    created = models.DateTimeField(verbose_name=u"created", auto_now=True)
    
    def save(self, force_insert=False, force_update=False):
        if self.suffix == "" or self.suffix == None:
            self.suffix = generate_suffix()
        
        super(Url, self).save(force_insert, force_update)
        
    
    def __unicode__(self):
        return settings.BASE_URL+self.suffix
    