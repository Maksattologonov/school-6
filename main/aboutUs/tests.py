from django.test import TestCase
import pytest
import factory


class TestViews(TestCase):
    def test_get(self) -> None:
        factory = RequestsClient()
        response = factory.get('')
        print(response.status)