from django.test import TestCase

from . import CreateTemplateMixin
from ..models import Template


class TestTag(CreateTemplateMixin, TestCase):
    """
    tests for Tag model
    """
    template_model = Template

    def test_tag(self):
        t = self._create_template()
        t.tags.add('mesh')
        self.assertEqual(t.tags.filter(name='mesh').count(), 1)
