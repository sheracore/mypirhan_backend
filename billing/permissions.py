from rest_framework.permissions import BasePermission


class DesignAppendCategoryPermissions(BasePermission):
    """Create permissions for OrderItemAppendCategory"""

    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        if view.action in ['create', 'destroy', 'partial_update', 'update']:
            return request.user and request.user.is_authenticated and request.user.is_staff

        elif view.action in ['retrieve', 'list']:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return True


class DesignAppendPermissions(BasePermission):
    """Creare permissions for OrderItemAppend"""

    def has_permission(self, request, view):
        if view.action in ['create', 'destroy', 'partial_update', 'update']:
            # print("*********",request,request.user, request.user.is_authenticated, request.user.is_staff)
            return request.user and request.user.is_authenticated and request.user.is_staff

        elif view.action in ['retrieve', 'list']:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return True


class DesignUploadPermissions(BasePermission):
    """Creare permissions for OrderItemAppend"""

    def has_permission(self, request, view):
        if view.action in ['create', 'destroy', 'partial_update', 'update']:
            # return request.user and request.user.is_authenticated 
            return True

        elif view.action in ['retrieve', 'list']:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return True