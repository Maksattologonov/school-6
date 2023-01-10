from modeltranslation.translator import translator, TranslationOptions
from .models import ScheduleFiles, Gallery


class ScheduleTranslationOptions(TranslationOptions):
    fields = ('schedule_id', 'file')


translator.register(ScheduleFiles, ScheduleTranslationOptions)


class GalleryTranslationOption(TranslationOptions):
    fields = ('title', )


translator.register(Gallery, GalleryTranslationOption)
