from rest_framework import serializers
from core.models import ProductColors, Supplier, Product, Category, Customer


class SupplierSerializer(serializers.ModelSerializer):
    """Serializer for Supplier objects"""

    class Meta:
        model = Supplier
        fields = ('id', 'company_name', 'type_good', 'discount_type', 'url')
        read_only_fields = ('id',)


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for products objects"""

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('id',)

    def to_representation(self, instance):
        data = super(ProductSerializer, self).to_representation(instance)
        data["category"] = {"id": instance.category.id,
                            "category_type": instance.category.category_type}
        return data


class ProductColorSerializer(serializers.ModelSerializer):
    """Serializer for productColors objects"""
    class Meta:
        model = ProductColors
        fields = "__all__"
        read_only_fields = ('id',)


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for Categorys objects"""

    class Meta:
        model = Category
        fields = ("id", "category_type")
        read_only_fields = ('id',)


class CustomerSerializer(serializers.ModelSerializer):
    """Serializer for Customer objects"""

    class Meta:
        model = Customer
        fields = (
            "first_name",
            "last_name",
            "address1",
            "address2",
            "age",
            "city",
            "province",
            "phone",
            "postal_code",
            "country",
            "gender")
        read_only_fields = ("id",)
