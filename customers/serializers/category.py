from rest_framework import serializers

from customers.models import Category


class ListCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
