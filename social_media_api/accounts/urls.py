from django.urls import path
from .views import RegisterView, LoginView, ProfileView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("profile/", ProfileView.as_view(), name="profile"),
]
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = router.urls

from django.urls import path
from . import views

urlpatterns = [
    path('follow/<int:user_id>/', views.FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', views.UnfollowUserView.as_view(), name='unfollow-user'),
]
