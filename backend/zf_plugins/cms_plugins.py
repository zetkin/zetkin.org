from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

@plugin_pool.register_plugin
class Blurb(CMSPluginBase):
    name = 'Blurb'
    render_template = 'zf_plugins/blurb.html'


@plugin_pool.register_plugin
class BlurbGrid(CMSPluginBase):
    allow_children = True
    child_classes = ['Blurb']
    name = 'Blurb Grid'
    render_template = 'zf_plugins/grid.html'
