from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from . import models

@plugin_pool.register_plugin
class ArticlePlugin(CMSPluginBase):
    allow_children = True
    child_classes = ['TextPlugin', 'PicturePlugin', 'MediaSpreadPlugin']
    name = 'Article'
    render_template = 'zf_plugins/article.html'


@plugin_pool.register_plugin
class BlurbPlugin(CMSPluginBase):
    name = 'Blurb'
    render_template = 'zf_plugins/blurb.html'


@plugin_pool.register_plugin
class BlurbGridPlugin(CMSPluginBase):
    allow_children = True
    child_classes = ['BlurbPlugin']
    name = 'Blurb Grid'
    render_template = 'zf_plugins/blurb_grid.html'


@plugin_pool.register_plugin
class FAQAccordionPlugin(CMSPluginBase):
    name = 'FAQ Accordion'
    render_template = 'zf_plugins/faq_accordion.html'


@plugin_pool.register_plugin
class FeaturePlugin(CMSPluginBase):
    name = 'Feature'
    render_template = 'zf_plugins/feature.html'


@plugin_pool.register_plugin
class FeatureGridPlugin(CMSPluginBase):
    name = 'Feature Grid'
    allow_children = True
    child_classes = ['FeaturePlugin']
    render_template = 'zf_plugins/feature_grid.html'


@plugin_pool.register_plugin
class HistoryTimelinePlugin(CMSPluginBase):
    name = 'History Timeline'
    render_template = 'zf_plugins/history_timeline.html'


@plugin_pool.register_plugin
class MediaHeroPlugin(CMSPluginBase):
    model = models.MediaHeroConfig
    name = 'Media Hero'
    render_template = 'zf_plugins/media_hero.html'


@plugin_pool.register_plugin
class MediaSpreadPlugin(CMSPluginBase):
    name = 'Media Spread'
    render_template = 'zf_plugins/media_spread.html'


@plugin_pool.register_plugin
class QuoteHeroPlugin(CMSPluginBase):
    name = 'Quote Hero'
    render_template = 'zf_plugins/quote_hero.html'


@plugin_pool.register_plugin
class SectionHeadPlugin(CMSPluginBase):
    name = 'Section Head'
    render_template = 'zf_plugins/section_head.html'


@plugin_pool.register_plugin
class SimpleHeroPlugin(CMSPluginBase):
    name = 'Simple Hero'
    render_template = 'zf_plugins/simple_hero.html'
