from __future__ import absolute_import

from django.test import TestCase

from .models import AccordionHeader, Collapsible


class AccordionTest(TestCase):
    """
    Simple CRUD test for Collapsible and CollapsibleHeader.
    """

    def setUp(self):
        self.collapsible = Collapsible()
        self.collapsible.title = "Test Collapsible"
        self.header = AccordionHeader()

    def test_plugin(self):
        self.assertEquals(unicode(self.header), "0 Collapsibles")
        self.assertEquals(unicode(self.collapsible), "Test Collapsible")
