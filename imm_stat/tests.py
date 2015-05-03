from django.test import TestCase
from django.core.urlresolvers import reverse


class IndexViewTest(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['userdata'], [])


class AuthViewsTest(TestCase):
    def test_login_view(self):
        response = self.client.get(reverse('django.contrib.auth.views.login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, ' or register here')

    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Registration')
