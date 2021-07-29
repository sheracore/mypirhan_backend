from billing import serializers
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, AllowAny

from billing import serializers   
from billing import permissions
from core import models


class ShipperViewSet(viewsets.GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin):
    """Manage Shipper in the database"""
    permission_classes = (IsAuthenticated,)
    queryset = models.Shipper.objects.all()
    serializer_class = serializers.ShipperSerializer

    def get_queryset(self):
        return self.queryset.filter(
            user=self.request.user
        ).order_by('-company_name')

    def perform_create(self, serializer):
        """Create a new Shipper"""
        # Set the user to the authenticated user
        serializer.save(user=self.request.user)


class DesignAppendCategoryViewSet(viewsets.GenericViewSet,
                                  mixins.ListModelMixin,
                                  mixins.CreateModelMixin):
    """Manage OrderItemAppendCategory in the database"""
    permission_classes = (permissions.DesignAppendCategoryPermissions,)
    queryset = models.DesignAppendCategory.objects.all()
    serializer_class = serializers.DesignAppendCategorySerializer


class DesignAppendViewSet(viewsets.GenericViewSet,
                          mixins.CreateModelMixin,
                          mixins.ListModelMixin):
    """Manage OrderItemAppend in the database"""
    permission_classes = (permissions.DesignAppendPermissions,)
    queryset = models.DesignAppend.objects.all()
    serializer_class = serializers.DesignAppendSerializer


class DesignUploadViewSet(viewsets.GenericViewSet,
                          mixins.CreateModelMixin,
                          mixins.ListModelMixin):
    """Manage DesignUpload in the database"""
    permission_classes = (permissions.DesignUploadPermissions,)
    queryset = models.DesignUpload.objects.all()
    serializer_class = serializers.DesignUploadSerializer