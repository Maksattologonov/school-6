from typing import List

from aboutUs.models import MainAboutUs, AboutUsFiles, Teachers, GloryBoard, SchoolAdmission
from common.exceptions import ObjectNotFoundException


class AboutUsService:
    model = MainAboutUs

    @classmethod
    def get(cls, **filters) -> MainAboutUs:
        try:
            return cls.model.objects.get(**filters)
        except cls.model.DoesNotExist:
            raise ObjectNotFoundException('Information not found')

    @classmethod
    def filter(cls, **filters) -> List[MainAboutUs]:
        try:
            return cls.model.objects.filter(**filters).order_by('-id')
        except cls.model.DoesNotExist:
            raise ObjectNotFoundException('Information not found')

    @classmethod
    def get_files(cls, **filters):
        try:
            return AboutUsFiles.objects.get(**filters)
        except Exception as ex:
            raise ObjectNotFoundException(ex)

    @classmethod
    def filter_files(cls, **filters):
        try:
            return AboutUsFiles.objects.filter(**filters).order_by('-id')
        except Exception as ex:
            raise ObjectNotFoundException('Files not found')


class TeachersService:
    model = Teachers

    @classmethod
    def get(cls, **filters):
        try:
            return cls.model.objects.get(**filters)
        except cls.model.DoesNotExist:
            raise ObjectNotFoundException('Teacher not found')

    @classmethod
    def filter(cls, **filters) -> List[Teachers]:
        try:
            return cls.model.objects.filter(**filters).order_by('-id')
        except cls.model.DoesNotExist:
            raise ObjectNotFoundException('Teachers not found')


class GloryBoardService:
    model = GloryBoard

    @classmethod
    def get(cls, **filters):
        try:
            return cls.model.objects.get(**filters)
        except cls.model.DoesNotExist:
            raise ObjectNotFoundException('GloryBoard not found')

    @classmethod
    def filter(cls, **filters) -> List[GloryBoard]:
        try:
            return cls.model.objects.filter(**filters).order_by('-id')
        except cls.model.DoesNotExist:
            raise ObjectNotFoundException('GloryBoard not found')


class SchoolAdmissionService:
    model = SchoolAdmission

    @classmethod
    def get(cls, **filters):
        try:
            return cls.model.objects.get(**filters)
        except cls.model.DoesNotExist:
            raise ObjectNotFoundException('SchoolAdmission not found')
