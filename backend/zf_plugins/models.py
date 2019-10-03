from cms.models.pluginmodel import CMSPlugin
from cms.models.fields import PageField
from django.db import models
from filer.fields.image import FilerImageField

SYMBOL_CHOICES = (
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
)


class ArticleConfig(CMSPlugin):
    title = models.CharField(max_length=100)
    kicker = models.TextField(max_length=400)

class BlurbConfig(CMSPlugin):
    header = models.CharField(max_length=200)
    symbol = models.CharField(null=True, blank=True, max_length=20, choices=SYMBOL_CHOICES)
    text = models.TextField()


class ButtonConfig(CMSPlugin):
    label = models.CharField(max_length=200)
    link_href = models.CharField(max_length=256)

    def get_link(self):
        return self.link_href


class FeatureConfig(CMSPlugin):
    image = FilerImageField(on_delete=models.CASCADE)
    header = models.CharField(max_length=200)
    symbol = models.CharField(null=True, blank=True, max_length=20, choices=SYMBOL_CHOICES)
    text = models.TextField()


class HistoryTimelineConfig(CMSPlugin):
    header = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.header


class HistoryEventConfig(CMSPlugin):
    image = FilerImageField(blank=True, null=True, on_delete=models.SET_NULL)
    header = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.header


class MediaHeroConfig(CMSPlugin):
    header = models.CharField(max_length=200)
    sub_header = models.CharField(max_length=200)
    background = FilerImageField(null=True, blank=True, on_delete=models.SET_NULL)


class NavDeeplinkItemConfig(CMSPlugin):
    label = models.CharField(max_length=100)
    description = models.TextField(max_length=400, blank=True)
    link_format = models.CharField(max_length=8, choices=(
        ('short', 'Short (columns)'),
        ('long', 'Long (full-width)'),
    ))
    summary_link_label = models.CharField(max_length=100, blank=True)
    summary_link_target = PageField(blank=True)


class NavImageItemConfig(CMSPlugin):
    image = FilerImageField(on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
    description = models.TextField(max_length=400, blank=True)
    link_page = PageField()


class NavMenuConfig(CMSPlugin):
    label = models.CharField(max_length=100)
    symbol = models.CharField(null=True, blank=True, max_length=20, choices=SYMBOL_CHOICES)
    section_page = PageField()

    def __str__(self):
        return self.label


class NavSimpleItemConfig(CMSPlugin):
    label = models.CharField(max_length=100)
    description = models.TextField(max_length=400, blank=True)
    link_page = PageField()


class SectionHeadConfig(CMSPlugin):
    header = models.CharField(max_length=100)
    intro = models.TextField(blank=True)


class SimpleHeroConfig(CMSPlugin):
    text = models.TextField()
    background = FilerImageField(blank=True, null=True, on_delete=models.SET_NULL)


class WideImageConfig(CMSPlugin):
    image = FilerImageField(on_delete=models.CASCADE)
    caption = models.TextField(null=True, blank=True)


class QuoteHeroConfig(CMSPlugin):
    background = FilerImageField(null=True, blank=True, on_delete=models.SET_NULL, related_name='quote_hero_background')
    citation = models.CharField(max_length=400)
    portrait = FilerImageField(null=True, blank=True, on_delete=models.SET_NULL, related_name='quote_hero_portrait')
    quote = models.CharField(max_length=200)
