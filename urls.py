from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
    TokenVerifyView,  # Optional
)
from .views import (
    RegisterView,
    BlogAPIView,
    SingleBlogAPIView,
    SingleSideBlogAPIView,
    UserView,
    BlogCreateView,
    SideBlogCreateView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # JWT Endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),  # Optional

    # App Endpoints
    path('blogs/', BlogAPIView.as_view(), name='blog-list'),
    path('blogs/<int:id>/', SingleBlogAPIView.as_view(), name='blog-detail'),
    path('sideblogs/<int:id>/', SingleSideBlogAPIView.as_view(), name='sideblog-detail'),
    path('users/', UserView.as_view(), name='user-list'),
    path('register/', RegisterView.as_view(), name='register'),
    path('blog_create/', BlogCreateView.as_view(), name='blog-create'),
    path('sideblog_create/', SideBlogCreateView.as_view(), name='sideblog-create'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)