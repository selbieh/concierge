from modeltranslation.translator import register, TranslationOptions
from .models import Service , HomeBanner ,HomePromotion ,Prerequisite

@register(HomeBanner)
class HomeBannerTranslation(TranslationOptions):
    fields=('title','image')


@register(Service)
class ServiceTranslation(TranslationOptions):
    fields=('name','description','image')

@register(HomePromotion)
class HomePromotionTranslation(TranslationOptions):
    fields=('title','image')

@register(Prerequisite)
class PrerequisiteTranslation(TranslationOptions):
    fields=('name',)