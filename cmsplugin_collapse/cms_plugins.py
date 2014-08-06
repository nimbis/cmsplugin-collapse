from __future__ import absolute_import

from django.contrib import admin

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from .models import AccordionHeader, Collapsible


class AccordionHeaderPlugin(CMSPluginBase):
    model = AccordionHeader
    name = "Accordion Header"
    render_template = "cmsplugin_collapse/accordionheader.html"
    allow_children = True
    child_classes = ["CollapsiblePlugin"]

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            })
        return context


class CollapsiblePlugin(CMSPluginBase):
    model = Collapsible
    name = "Collapsible"
    render_template = "cmsplugin_collapse/accordioncollapsible.html"
    parent_classes = ["AccordionHeaderPlugin"]
    allow_children = True

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            })
        return context

plugin_pool.register_plugin(AccordionHeaderPlugin)
plugin_pool.register_plugin(CollapsiblePlugin)
