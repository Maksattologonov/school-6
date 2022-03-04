from typing import List
from common.exceptions import ObjectNotFoundException
from news.models import News, Notification


class NewsService:
    model = News

    @classmethod
    def get(cls, **filters) -> News:
        try:
            return cls.model.objects.get(**filters)
        except cls.model.DoesNotExist:
            raise ObjectNotFoundException('News not found')

    @classmethod
    def filter(cls, **filters) -> List[News]:
        try:
            return cls.model.objects.filter(**filters)
        except cls.model.DoesNotExist:
            raise ObjectNotFoundException('News not found')


class NotificationService:
    model = Notification

    @classmethod
    def get(cls, **filters):
        try:
            return cls.model.objects.get(**filters)
        except cls.model.DoesNotExist:
            raise ObjectNotFoundException('Notifications not found')

    @classmethod
    def filter(cls, **filters) -> List[Notification]:
        try:
            return cls.model.objects.filter(**filters)
        except cls.model.DoesNotExist:
            raise ObjectNotFoundException('Notifications not found')