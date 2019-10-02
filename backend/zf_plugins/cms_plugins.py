from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from . import models

@plugin_pool.register_plugin
class ArticlePlugin(CMSPluginBase):
    allow_children = True
    child_classes = ['TextPlugin', 'WideImagePlugin']
    model = models.ArticleConfig
    name = 'Article'
    render_template = 'zf_plugins/article.html'


@plugin_pool.register_plugin
class BlurbPlugin(CMSPluginBase):
    allow_children = True
    child_classes = ['ButtonPlugin']
    model = models.BlurbConfig
    name = 'Blurb'
    render_template = 'zf_plugins/blurb.html'


@plugin_pool.register_plugin
class BlurbGridPlugin(CMSPluginBase):
    allow_children = True
    child_classes = ['BlurbPlugin']
    name = 'Blurb Grid'
    render_template = 'zf_plugins/blurb_grid.html'


@plugin_pool.register_plugin
class ButtonPlugin(CMSPluginBase):
    model = models.ButtonConfig
    name = 'Button'
    render_template = 'zf_plugins/button.html'


@plugin_pool.register_plugin
class FAQAccordionPlugin(CMSPluginBase):
    name = 'FAQ Accordion'
    render_template = 'zf_plugins/faq_accordion.html'


@plugin_pool.register_plugin
class FeaturePlugin(CMSPluginBase):
    allow_children = True
    child_classes = ['ButtonPlugin']
    model = models.FeatureConfig
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
    allow_children = True
    child_classes = ['HistoryEventPlugin']
    model = models.HistoryTimelineConfig
    name = 'History Timeline'
    render_template = 'zf_plugins/history_timeline.html'


@plugin_pool.register_plugin
class HistoryEventPlugin(CMSPluginBase):
    model = models.HistoryEventConfig
    name = 'Timeline event'
    render_template = 'zf_plugins/history_event.html'


@plugin_pool.register_plugin
class MediaHeroPlugin(CMSPluginBase):
    allow_children = True
    child_classes = ['ButtonPlugin']
    model = models.MediaHeroConfig
    name = 'Media Hero'
    render_template = 'zf_plugins/media_hero.html'


@plugin_pool.register_plugin
class NavMenu(CMSPluginBase):
    allow_children = True
    child_classes = ['NavMenuColumn']
    model = models.NavMenuConfig
    name = 'Navigation menu'
    render_template = 'zf_plugins/navigation/menu.html'


@plugin_pool.register_plugin
class NavDeeplinkItemPlugin(CMSPluginBase):
    allow_children = True
    child_classes = ['LinkPlugin']
    model = models.NavDeeplinkItemConfig
    name = 'Deeplinking menu item'
    render_template = 'zf_plugins/navigation/deeplink_item.html'


@plugin_pool.register_plugin
class NavImageItemPlugin(CMSPluginBase):
    model = models.NavImageItemConfig
    name = 'Image menu item'
    render_template = 'zf_plugins/navigation/image_item.html'


@plugin_pool.register_plugin
class NavMenuColumn(CMSPluginBase):
    allow_children = True
    child_classes = ['NavSimpleItemPlugin', 'NavDeeplinkItemPlugin', 'NavImageItemPlugin']
    child_classes = ['NavDeeplinkItemPlugin', 'NavImageItemPlugin', 'NavSimpleItemPlugin']
    render_template = 'zf_plugins/navigation/column.html'


@plugin_pool.register_plugin
class NavSimpleItemPlugin(CMSPluginBase):
    model = models.NavSimpleItemConfig
    name = 'Simple menu item'
    render_template = 'zf_plugins/navigation/simple_item.html'


@plugin_pool.register_plugin
class WideImagePlugin(CMSPluginBase):
    model = models.WideImageConfig
    name = 'Wide Image'
    render_template = 'zf_plugins/wide_image.html'


@plugin_pool.register_plugin
class QuoteHeroPlugin(CMSPluginBase):
    allow_children = True
    child_classes = ['ButtonPlugin']
    model = models.QuoteHeroConfig
    name = 'Quote Hero'
    render_template = 'zf_plugins/quote_hero.html'


@plugin_pool.register_plugin
class SectionHeadPlugin(CMSPluginBase):
    model = models.SectionHeadConfig
    name = 'Section Head'
    render_template = 'zf_plugins/section_head.html'


@plugin_pool.register_plugin
class SimpleHeroPlugin(CMSPluginBase):
    model = models.SimpleHeroConfig
    name = 'Simple Hero'
    render_template = 'zf_plugins/simple_hero.html'
