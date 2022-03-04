from typing import List

from common.exceptions import ObjectNotFoundException
from files.models import Gallery, Schedule


class FilesService:
    model = Gallery
    model_schedule = Schedule

    @classmethod
    def get_gallery(cls, **filters) -> Gallery:
        try:
            return cls.model.objects.get(**filters)
        except cls.model.DoesNotExist:
            raise ObjectNotFoundException('Images not found')

    @classmethod
    def filter_gallery(cls, **filters) -> List[Gallery]:
        try:
            return cls.model.objects.filter(**filters)
        except cls.model.DoesNotExist:
            raise ObjectNotFoundException('Images not found')

    @classmethod
    def get_gallery_titles(cls):
        try:
            return cls.model.objects.values("title", "id")
        except cls.model.DoesNotExist:
            raise ObjectNotFoundException('Title not found')

    @classmethod
    def get_schedule(cls, **filters) -> Schedule:
        try:
            return cls.model_schedule.objects.get(**filters)
        except cls.model_schedule.DoesNotExist:
            raise ObjectNotFoundException('Schedule not found')

    @classmethod
    def filter_schedule(cls, **filters) -> List[Schedule]:
        try:
            return cls.model_schedule.objects.filter(**filters)
        except cls.model_schedule.DoesNotExist:
            raise ObjectNotFoundException('Schedule not found')

    @classmethod
    def get_schedule_titles(cls):
        try:
            return cls.model_schedule.objects.values("class_no", "id")
        except cls.model_schedule.DoesNotExist:
            raise ObjectNotFoundException('Title not found')
