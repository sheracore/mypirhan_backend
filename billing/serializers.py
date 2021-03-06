from django.forms import fields
from rest_framework import serializers

from core import models


class ShipperSerializer(serializers.ModelSerializer):
    """Serializer for shipper object"""

    class Meta:
        model = models.Shipper
        fields = ('id', 'company_name')
        read_only_fields = ('id',)


class DesignAppendCategorySerializer(serializers.ModelSerializer):
    """Seializer for OrderItemAppendCategory object"""

    class Meta:
        model = models.DesignAppendCategory
        fields = ('id', 'type_name')
        read_only_fields = ("id",)


class DesignAppendSerializer(serializers.ModelSerializer):
    """Serializer for OrderItemAppend objects"""
    class Meta:
        model = models.DesignAppend
        fields = ('id', 'name', 'image', 'design_append_category',
                  'design_append_price_irr')
        read_only_fields = ('id',)

    def to_representation(self, instance):
        data = super(DesignAppendSerializer, self).to_representation(instance)
        data['design_append_category'] = {
            "id": instance.design_append_category.id, "type_name": instance.design_append_category.type_name}
        return data


class DesignUploadSerializer(serializers.ModelSerializer):
    """Serializer for DesignUpload objects"""

    class Meta:
        model = models.DesignUpload
        fields = ('id', 'image')
        read_only_fields = ('id',)
