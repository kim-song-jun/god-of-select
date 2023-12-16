from django.test import TestCase
from django.urls import reverse

class CreateIssueTest(TestCase):

    def test_create_issue(self):
        # reqeust data
        data = {
            'user_id': '6eef438e-7adf-4638-93aa-bc123e434f65',
            'title': 'test1 issue',
            'content_1': 'test1 content_1',
            'content_2': 'test1 content_2',
        }

        response = self.client.post(reverse('vote_issue'), data=data)

        print(response.data)


