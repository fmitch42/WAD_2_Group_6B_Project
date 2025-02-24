from django.test import TestCase

# Create your tests here.


from django.test import TestCase
from django.conf import settings
import os


class TournamentTest(TestCase):
    def test_index_exists(self):
        template_base_path = os.path.join(settings.TEMPLATE_DIR, 'base.html')
        self.assertTrue(os.path.exists(template_base_path))

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
