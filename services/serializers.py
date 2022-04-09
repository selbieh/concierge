from rest_framework import serializers

from services.models import Service, HomeBanner, HomePromotion


class ListServicesSerializer(serializers.ModelSerializer):
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
