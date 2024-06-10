import os

from django.db import transaction

from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from core.models import Supplier, Product, Category, Customer, ProductColors

from product.serializers import (SupplierSerializer,
                                 ProductSerializer,
                                 CategorySerializer,
                                 CustomerSerializer,
                                 ProductColorSerializer)

from product.permissions import ProductPermission, CategoryPermission


class SupplierViewSet(viewsets.GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.DestroyModelMixin):
    """Manage Supplier in the database"""
    permission_classes = (IsAuthenticated,)
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

    def perform_create(self, serializer):
        """Create a new supplier"""
        # Set the user to the authenticated user
        serializer.save(user=self.request.user)


class ProductViewSet(viewsets.GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):
    """Manage Product in the database"""
    permission_classes = (ProductPermission,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductColorViewSet(viewsets.GenericViewSet,
                          mixins.ListModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.DestroyModelMixin,
                          mixins.CreateModelMixin):
    """Manage ProductColor in the database"""
    permission_classes = (ProductPermission,)
    queryset = ProductColors.objects.all()
    serializer_class = ProductColorSerializer


class CategoryViewSet(viewsets.GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.DestroyModelMixin):
    """Manage Category in the database"""
    permission_classes = (CategoryPermission,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CustomerViewSet(viewsets.GenericViewSet,
                      mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.DestroyModelMixin):
    """Manage customer in the database"""
    permission_classes = (IsAuthenticated,)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get_queryset(self):
        return self.queryset.filter(
            user=self.request.user
        ).order_by('-first_name')

    def perform_create(self, serializer):
        """Create a new customer"""
        # If you don't do this, user dosnt create for cusomer
        serializer.save(user=self.request.user)
