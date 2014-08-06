from django.db import models

from cms.models import CMSPlugin


class AccordionHeader(CMSPlugin):
    """
    A plugin that has Collapsible objects as children.
    """

    show_first = models.BooleanField(
        default=True,
        help_text="If selected, the first collapsible will be displayed "
        "in the open state."
        )

    def __unicode__(self):
        return u"{0} Collapsibles".format(self.cmsplugin_set.all().count())


class Collapsible(CMSPlugin):
    """
    An individual Tab for the TabHeader plugin.
    """
    title = models.CharField(max_length=64)

    def __unicode__(self):
        return u"{0}".format(self.title)
