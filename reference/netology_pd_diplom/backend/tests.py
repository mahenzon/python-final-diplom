from .models import User

from rest_framework import status
from rest_framework.test import APITestCase


class RegistrationTestCase(APITestCase):
    def test_register_account(self):
        """
        Ensure we can create a new account object.
        """
        data = {'first_name': 'test_name', 'last_name': 'test_last_name',
                'email': 'test@email.test', 'password': 'test_passw',
                'company': 'test_company', 'position': 'test_position'}

        response = self.client.post('/user/register', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().first_name, 'test_name')