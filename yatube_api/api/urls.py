from django.urls import path, include
from rest_framework.routers import SimpleRouter
from api.views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet

router = SimpleRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups',)
router.register('follow', FollowViewSet, basename='follow',)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet, basename='comments',)

app_name = 'api'
urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
