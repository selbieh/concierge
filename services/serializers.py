from rest_framework import serializers

from .models import Service, HomeBanner, HomePromotion, Prerequisite


class PrerequisiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prerequisite
        fields = "__all__"

class ListServicesSerializer(serializers.ModelSerializer):
    prerequisites=PrerequisiteSerializer(many=True)
    class Meta:
        model = Service
        fields = "__all__"


class ListHomeBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeBanner
        fields = "__all__"


class ListHomePromotionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePromotion
        fields = "__all__"
