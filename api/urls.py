from django.urls import path, include
from .views import *
from rest_framework.authtoken.views import obtain_auth_token as token


urlpatterns = [
    #path('', views.apiOverview, name="api-overview"),
    path('auth-token/', token),
    path('auth/', include('rest_framework.urls')),
    path('posts/', PostView.as_view()),
    path('posts/delete/<int:id>', PostDeleteView.as_view()),
    path('likes/<int:id>', LikedView.as_view()),
    path('dislikes/<int:id>', DislikedView.as_view()),
]
