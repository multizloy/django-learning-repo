from django.test import TestCase
from django.shortcuts import reverse

# Create your tests here.


class LandingPageView(TestCase):
    def test_get(self):
        # TODO some sort of test
        response = self.client.get(reverse("landing-page"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "landing.html")