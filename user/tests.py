from django.test import TestCase
from django.urls import reverse

class CreateUserTest(TestCase):

    def test_create_user(self):
        # reqeust data
        data = {
            'user_name': 'test1 user',
        }

        response = self.client.post(reverse('create_user'), data=data)

        print(response.data)

