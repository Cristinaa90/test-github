from django.urls import path
from rest_framework import routers

from post import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path("api/posts/", views.PostList.as_view()),
    path("api/posts/<int:pk>/", views.PostDetail.as_view()),
]

# router = routers.SimpleRouter()
# router.register(r'api/posts', views.PostViewSet)
# urlpatterns += router.urls


