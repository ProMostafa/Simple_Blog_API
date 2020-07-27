from django.urls import path ,include
from posts import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('list-post',views.Posts_ViewSet,basename='list-post-viewset')
router.register('list-comment',views.Comment_ViewSet,basename='list-comment-viewset')

urlpatterns = [
   path('Blog-API/',include(router.urls)),
   path('login/',views.UserLoginAPIView.as_view()),
]

