from rest_framework.routers import DefaultRouter
from django.urls import re_path, path
from django.urls import include
from rest_framework.authtoken import views

from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet


router_v1 = DefaultRouter()
router_v1.register('posts', PostViewSet)
router_v1.register('groups', GroupViewSet)
router_v1.register('follow', FollowViewSet, basename='follow')
router_v1.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewSet,
                   basename='comments')


urlpatterns = [
    re_path('^v1/', include(router_v1.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),

]
