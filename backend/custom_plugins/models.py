# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from cms.models.fields import PageField
from cms.models import CMSPlugin


class Blurb(CMSPlugin):
    #TODO: Insert icon here
    headline = models.CharField(
        max_length=200,
    )
    text = models.TextField(
        blank=True,
    )
    #TODO: Get link generation to work and enable linking to other sites
    link = PageField()
    def __str__(self):
        return self.headline
