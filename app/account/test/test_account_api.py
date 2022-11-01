"""
Tests for recipe APIs.
"""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Account, Team

from account.serializers import AccountSerializer


ACCOUNTS_URL = reverse('account:account-list')

def detail_url(account_id):
    """Create and return a account detail URL."""
    return reverse('account:account-detail', args=[account_id])

def create_account(**params):
    """Create and return a sample account."""
    defaults = {
        'account_name': 'Sample account name',
        'account_customer': 'Sample account customer',
    }
    defaults.update(params)
    account = Account.objects.create(**defaults)
    return account

def create_team(**params):
    """Create and return a sample team."""
    defaults = {
        'team_name' : 'Sample Team Name',
    }
    defaults.update(params)
    team = Team.objects.create(**defaults)  
    return team

def create_user(**params):
    """Create and return a new user."""
    return get_user_model().objects.create_user(**params)



class PublicAccountAPITests(TestCase):
    """Test unauthenticated API requests."""
    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Test auth is required to call API."""
        res = self.client.get(ACCOUNTS_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateAccountApiTests(TestCase):
    """Test authenticated API requests."""

    def setUp(self):
        self.client = APIClient()
        self.user = create_user(email='user@example.com', password='test123')
        self.team = create_team()
        self.client.force_authenticate(self.user)


    def test_retrieve_accounts(self):
        """Test retrieving a list of accounts."""
        create_account()
        create_account()

        res = self.client.get(ACCOUNTS_URL)

        accounts = Account.objects.all().order_by('-id')
        serializer = AccountSerializer(accounts, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_get_account_detail(self):
        """Test get account detail."""
        account = create_account()

        url = detail_url(account.id)
        res = self.client.get(url)

        serializer = AccountSerializer(account)
        self.assertEqual(res.data, serializer.data)

    def test_create_account(self):
        """Test creating a account."""
        payload = {
            'account_name': 'Sample account name',
            'account_customer': 'Sample account customer',
        }
        res = self.client.post(ACCOUNTS_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        account = Account.objects.get(id=res.data['id'])
        for k, v in payload.items():
            self.assertEqual(getattr(account, k), v)

    def test_partial_update(self):
        """Test partial update of a account."""
        original_account_name = 'Original account name'
        account = create_account(
            account_name=original_account_name,
            account_customer='Sample account customer',
            operational_responsable = self.user,
            team_id = self.team
        )

        payload = {'account_customer': 'New account customer'}
        url = detail_url(account.id)
        res = self.client.patch(url, payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        account.refresh_from_db()
        self.assertEqual(account.account_customer, payload['account_customer'])
        self.assertEqual(account.account_name, original_account_name)
        self.assertEqual(account.operational_responsable, self.user)
        self.assertEqual(account.team_id, self.team)

    def test_full_update(self):
        """Test full update of account."""
        account = create_account(
            account_name='Sample account name',
            account_customer='Sample account customer',
            operational_responsable = self.user,
            team_id = self.team
        )

        payload = {
            'account_name': 'Sample account name',
            'account_customer': 'Sample account customer',
        }
        url = detail_url(account.id)
        res = self.client.put(url, payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        account.refresh_from_db()
        for k, v in payload.items():
            self.assertEqual(getattr(account, k), v)
        self.assertEqual(account.operational_responsable, self.user)
        self.assertEqual(account.team_id, self.team)

    def test_delete_account(self):
        """Test deleting a account successful."""
        account = create_account()

        url = detail_url(account.id)
        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Account.objects.filter(id=account.id).exists())
