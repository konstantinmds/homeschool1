from django.urls import reverse
from django.test import TestCase
from django.test.client import Client

from homeschool.users.tests.factories import UserFactory

class TestApp(TestCase):
  

  def test_ok(self):
    """the app returns 200 for loged in user
    """ #use django test client
    client = Client()
    user = UserFactory()

    client.force_login(user)

    response = client.get(reverse("app"))

    #302 anonimni user kada dodje pred login required
    self.assertEqual(response.status_code, 200)


  def test_unauthenticated_access(self):
    """the app redirects to login """ #use django test client

    client = Client()

    response = client.get(reverse("app"))

    #302 anonimni user kada dodje pred login required
    self.assertEqual(response.status_code, 302)
    self.assertIn(reverse("account_login"), response.get("Location"))
    print(response.get("Location"), "lokacija")
    print(reverse("account_login"))