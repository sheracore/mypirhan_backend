from rest_framework.routers import DefaultRouter
from django.urls import path, include
from billing import views


router = DefaultRouter()

router.register('shippers', views.ShipperViewSet)
router.register('designappendcategory',
                views.DesignAppendCategoryViewSet)
router.register('designappend', views.DesignAppendViewSet)
router.register('designupload', views.DesignUploadViewSet)

app_name = 'billing'

urlpatterns = [
    path('', include(router.urls))
]
