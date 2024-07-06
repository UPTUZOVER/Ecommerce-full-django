from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Account.views import (
                        RegisterView,
                        LoginView,
                        LogoutView
                        )
from cart.views import (
                        CartItemListCreateAPIView,
                        CartListCreateAPIView,
                        CartItemRetrieveUpdateDestroyAPIView,
                        CartRetrieveUpdateDestroyAPIView,
                        CartItemViewSet

                        )
from cart_variant_2.views import (
                        ProductListCreateAPIView,
                        ProductRetrieveUpdateDestroyAPIView,
                        ProductImageListCreateAPIView,
                        ProductImageRetrieveUpdateDestroyAPIView
                        )
from cart_variant_2.views import (
                        CartItemListCreateAPIView_,
                        CartItemRetrieveUpdateDestroyAPIView_,
                        CartListCreateAPIView_,
                        CartRetrieveUpdateDestroyAPIView_
                        )
from products.views import (
                        ProductViewSet,
                        ProductDetailViewSet,
                        CategoryViewSet,
                        CategoryDetailViewSet
                        )


from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



from rest_framework_swagger.views import get_swagger_view

schema_view = get_schema_view(
    openapi.Info(
        title="INCOME EXPENSES API",
        default_version='v1',
        description="Your API description",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@expenses.com"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path("admin/", admin.site.urls),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),



    #path('api/', include('products.urls')),

    # path('api/register/', RegisterView.as_view(), name='register'),
    # path('api/userlist/', UserListView.as_view(), name='register'),

    # path('api/products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    # path('api/products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-retrieve-update-destroy'),

    #products uchun
    path('api/products/', ProductViewSet.as_view()),
    path('api/products/<str:pk>/', ProductDetailViewSet.as_view(), name='product-detail'),
    path('api/categories/', CategoryViewSet.as_view()),
    path('api/categories/<int:pk>/', CategoryDetailViewSet.as_view(), name='category-detail'),

    #cart lar uchun
    path('api/cart-items/', CartItemListCreateAPIView.as_view(), name='cart-item-list-create'),
    path('api/cart-items/<int:pk>/', CartItemRetrieveUpdateDestroyAPIView.as_view(), name='cart-item-list-create'),
    path('api/carts/', CartListCreateAPIView.as_view(), name='cart-list-create'),
    path('api/carts/<str:pk>/cart', CartRetrieveUpdateDestroyAPIView.as_view(), name='cart-retrieve-update-destroy'),
   # path('api/add-cart/', CartItemViewSet.as_view(), name='add-cart-item-view-set'),

    #cart variant 2 uchun
    path('api/variant/cart-items/', CartItemListCreateAPIView_.as_view(), name='cart-item-list-create'),
    path('api/variant/cart-items/<int:pk>/', CartItemRetrieveUpdateDestroyAPIView_.as_view(), name='cart-item-retrieve-update-destroy'),
    path('api/variant/carts/', CartListCreateAPIView_.as_view(), name='cart-list-create'),
    path('api/variant/carts/<str:pk>/',CartRetrieveUpdateDestroyAPIView_.as_view(), name='cart-retrieve-update-destroy'),


    #product variant 2 uchun
    path('api/variant/products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('api/variant/products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-retrieve-update-destroy'),
    path('api/variant/product-images/', ProductImageListCreateAPIView.as_view(), name='product-image-list-create'),
    path('api/variant/product-images/<str:pk>/', ProductImageRetrieveUpdateDestroyAPIView.as_view(), name='product-image-retrieve-update-destroy'),

    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]






if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'cart-items', CartItemViewSet, basename='cart-item')

urlpatterns += router.urls



