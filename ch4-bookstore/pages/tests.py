from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView
# Create your tests here.

class HomePageTests(SimpleTestCase):
    # def test_url_exists_at_correct_location(self):
    #     response = self.client.get('/')
    #     self.assertEqual(response.status_code, 200)
        
    # def test_homepage_url(self):
    #     response = self.client.get(reverse('home'))
    #     self.assertEqual(response.status_code, 200)
        
    # def test_homepage_template(self):
    #     response = self.client.get("/")
    #     self.assertTemplateUsed(response, 'home.html')
        
    # def test_homepage_contains_correct_html(self):
    #     response = self.client.get('/')
    #     self.assertContains(response, 'This is our Home Page')
    
    # def test_homepage_does_not_contain_incorrect_html(self):
    #     response = self.client.get('/')
    #     self.assertNotContains(response, 'This text should not be on the page')
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)
        
    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)
        
    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')
        
    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'This is our Home Page')
    def test_homepage_does_not_contain_incorrect_html(self):    
        self.assertNotContains(self.response, 'This text should not be on the page')
        
    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)