from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)

    def test_login_url(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login(self):
        # send login data
        response = self.client.post('/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_authenticated)


class RegisterTest(TestCase):    
    def test_register_url(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_signup_form(self):
        response = self.client.post(reverse('register'), data={
            'username': 'testuser',
            'email': 'test@email.com',
            'password1': 'password',
            'password2': 'password'
        })
        self.assertEqual(response.status_code, 200)