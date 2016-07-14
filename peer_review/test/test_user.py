from django.core.urlresolvers import reverse
from django.test import TestCase, Client

from peer_review.models import User


#
#from django.test.utils import setup_test_environment
#setup_test_environment()
#


class UserTests(TestCase):
    def test_test(self):
        """
        2 + 2 should equal 4
        """
        ans = 2 + 2
        self.assertEqual(ans, 4)

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('bob@bob.com', 'bob', userId=str(1234))

    # Simple test to see if questionAdmin is rendered
    def test_questionAdmin(self):
        self.client.login(username='bob@bob.com', password='bob')
        url = reverse('questionAdmin')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'peer_review/questionAdmin.html')

    # Simple test to see if questionnaireAdmin is rendered
    def test_questionnaireAdmin(self):
        self.client.login(username='bob@bob.com', password='bob')
        url = reverse('questionnaireAdmin')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'peer_review/questionnaireAdmin.html')

    # Simple test to see if userdAdmin is rendered
    def test_user_list(self):
        self.client.login(username='bob@bob.com', password='bob')
        url = reverse('userAdmin')
        response = self.client.get(url)
        print(response.context['users']())
        self.assertIn(self.user, response.context['users']())

    # Simple test to see if accountDetails is rendered
    def test_account_details(self):
        self.client.login(username='bob@bob.com', password='bob')
        url = '/accountDetails/1234'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'peer_review/accountDetails.html')

    # Simple test to see if login is rendered
    def test_login(self):
        self.client.login(username='bob@bob.com', password='bob')
        url = reverse('login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'peer_review/login.html')

    # Simple test to see if maintainRound is rendered
    def test_maintain_round(self):
        self.client.login(username='bob@bob.com', password='bob')
        url = reverse('maintainRound')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'peer_review/maintainRound.html')

    # Simple test to see if activeRounds is rendered
    def test_active_rounds(self):
        self.client.login(username='bob@bob.com', password='bob')
        url = 'activeRounds/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'peer_review/activeRounds.html')

    # Simple test to see if maintainTeam is rendered
    def test_maintain_team(self):
        self.client.login(username='bob@bob.com', password='bob')
        url = 'maintainTeam'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'peer_review/maintainTeam.html')
