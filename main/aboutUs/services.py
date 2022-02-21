from typing import List

from aboutUs.models import MainAboutUs
from common.exceptions import ObjectNotFoundException


class AboutUsService:
    model = MainAboutUs

    @classmethod
    def get(cls, **filters) -> MainAboutUs:
        try:
            return cls.model.objects.get(**filters)
        except cls.model.DoesNotExist:
            raise ObjectNotFoundException('Poll not found')

    @classmethod
    def filter(cls, **filters) -> List[MainAboutUs]:
        try:
            return cls.model.objects.filter(**filters)
        except cls.model.DoesNotExist:
            raise ObjectNotFoundException('Poll not found')
