from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router_v1 = DefaultRouter()
router_v1.register(r'follow', FollowViewSet, basename='follow')
router_v1.register(r'posts', PostViewSet, basename='post')
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet, basename='comments'
)
router_v1.register(r'groups', GroupViewSet, basename='group')

urlpatterns = [
    path('', include(router_v1.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]
