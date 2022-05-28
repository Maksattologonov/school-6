from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from json import JSONEncoder

from aboutUs.models import MainAboutUs, AboutUsFiles, Teachers, GloryBoard


class TestViews(APITestCase):
    def setUp(self) -> None:
        self.list_url = reverse('list')
        MainAboutUs.objects.create(title="main title",
                                   description="description")
        MainAboutUs.objects.create(title="main title2",
                                   description="description2")
        self.teachers_url = reverse('teachers')

        self.teacher = Teachers.objects.create(
                                                  name="Test name",
                                                  position="Math",
                                                  lesson="Math",
                                                  timetable="Something",
                                                  progress="None",
                                                  contacts="13213131",
                                                  avatar="/media/avatars/Screenshot_from_2021-10-29_21-24-35.png")
        self.glory_board_url = reverse('glory-board')
        self.glory_board = GloryBoard.objects.create(
            name='Test Name',
            class_no="11-B",
            avatar='/media/avatars/IMG_1859.JPG',
            glory_whom='Окуучу'
        )
        self.detail_url = reverse('detail', kwargs={"pk": 1})

    def test_get(self) -> None:
        response = self.client.get(self.list_url, format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_params(self):
        data = b'{"message":"List of the main information\'' \
               b's","data":[{"id":9,"title":"main title","description":"description","file":[]}],"status":200}'
        response = self.client.get(self.list_url + '?count=1&page=0', format='json')
        response_path = self.client.get(self.list_url + '?count=0&', format='json')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(type(response_path.content), bytes)
        self.assertEqual(data, response.content)
        self.assertEqual(response_path.content, b'{"message":"List of the main information\'s","data":[],"status":200}')

    def test_id_param(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
        self.assertEqual(response.content, b'{"detail":"Information not found"}')

    def test_get_teachers(self):
        data = b'{"message":"Teachers information","data":[{"id":2,"name":"Test name","position":"Math",' \
               b'"lesson":"Math","timetable":"Something","progress":"None","contacts":"13213131",' \
               b'"avatar":"/media/media/avatars/Screenshot_from_2021-10-29_21-24-35.png"}],"status":200}'
        response = self.client.get(self.teachers_url, format="json")
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.content, data)

    def test_glory_board(self):
        data = b'{"message":"Glory Board information","data":[{"id":3,"name":"Test Name","class_no":"11-B",' \
               b'"avatar":"/media/media/avatars/IMG_1859.JPG",' \
               b'"glory_whom":"\xd0\x9e\xd0\xba\xd1\x83\xd1\x83\xd1\x87\xd1\x83"}],"status":200}'
        response = self.client.get(self.glory_board_url, format="json")
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(response.content, data)
