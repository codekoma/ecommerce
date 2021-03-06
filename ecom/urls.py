from django.urls import path, include
from rest_framework import routers
from api import api

router = routers.DefaultRouter()
router.register('api/categories', api.CategoryViewSet, 'category')
router.register('api/subcategories', api.SubCategoryViewSet, 'subcategory'),
router.register('api/products', api.ProductViewSet, 'product')

urlpatterns = [
    path('', include(router.urls)),
]