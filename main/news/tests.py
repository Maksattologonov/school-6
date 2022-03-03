from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from json import JSONEncoder

from news.models import News, NewsFiles


class TestViews(APITestCase):
    def setUp(self) -> None:
        self.list_url = reverse('list')
        self.data = b'{"message":"List of the main information\'s","data":[],"status":200}'
        News.objects.create(title="main title",
                            description="description")
        News.objects.create(title="main title2",
                            description="description2")

        # self.file = AboutUsFiles.objects.create(title="file title", about_us=self.main.id)
        self.detail_url = reverse('detail', kwargs={"pk": 1})

    def test_get(self) -> None:
        response = self.client.get(self.list_url, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_params(self):
        response = self.client.get(self.list_url + '?count=1&page=0', format='json')
        response_path = self.client.get(self.list_url + '?count=0&', format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(type(response_path.content), bytes)
        self.assertEqual(self.data, response.content)
        self.assertEqual(response_path.content, b'{"message":"List of the main information\'s","data":[],"status":200}')

    def test_id_param(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
        self.assertEqual(response.content, b'{"detail":"Information not found"}')
