from cms.models.pluginmodel import CMSPlugin
from django.db import models
from filer.fields.image import FilerImageField

class ButtonConfig(CMSPlugin):
    label = models.CharField(max_length=200)
    link_href = models.CharField(max_length=256)

    def get_link(self):
        return self.link_href


class MediaHeroConfig(CMSPlugin):
    header = models.CharField(max_length=200)
    sub_header = models.CharField(max_length=200)
    background = FilerImageField(null=True, blank=True, on_delete=models.SET_NULL)
