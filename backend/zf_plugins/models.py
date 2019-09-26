from cms.models.pluginmodel import CMSPlugin
from django.db import models
from filer.fields.image import FilerImageField

class BlurbConfig(CMSPlugin):
    header = models.CharField(max_length=200)
    symbol = models.CharField(null=True, blank=True, max_length=20, choices=(
        (None, '-'),
        ('book', 'Book'),
        ('calendar', 'Calendar'),
        ('chat', 'Chat'),
        ('feed', 'Feed'),
        ('info', 'Info'),
        ('money', 'Money'),
        ('person', 'Person'),
        ('pin', 'Pin'),
        ('point', 'Point'),
        ('question', 'Question'),
        ('share', 'Share'),
        ('sound', 'Sound'),
        ('time', 'Time'),
    ))
    text = models.TextField()


class ButtonConfig(CMSPlugin):
    label = models.CharField(max_length=200)
    link_href = models.CharField(max_length=256)

    def get_link(self):
        return self.link_href


class MediaHeroConfig(CMSPlugin):
    header = models.CharField(max_length=200)
    sub_header = models.CharField(max_length=200)
    background = FilerImageField(null=True, blank=True, on_delete=models.SET_NULL)


class QuoteHeroConfig(CMSPlugin):
    background = FilerImageField(null=True, blank=True, on_delete=models.SET_NULL, related_name='quote_hero_background')
    citation = models.CharField(max_length=400)
    portrait = FilerImageField(null=True, blank=True, on_delete=models.SET_NULL, related_name='quote_hero_portrait')
    quote = models.CharField(max_length=200)
