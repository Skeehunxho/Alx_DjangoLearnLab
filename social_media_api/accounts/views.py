from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import CustomUser
from .serializers import UserSerializer


# ✅ List all users
class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()  # required for the check
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


# ✅ Follow a user using GenericAPIView
class FollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target_user = get_object_or_404(CustomUser, id=user_id)

        if target_user == request.user:
            return Response(
                {"detail": "You cannot follow yourself."},
                status=status.HTTP_400_BAD_REQUEST
            )

        request.user.following.add(target_user)
        return Response(
            {"detail": f"You are now following {target_user.username}"},
            status=status.HTTP_200_OK
        )


# ✅ Unfollow a user using GenericAPIView
class UnfollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target_user = get_object_or_404(CustomUser, id=user_id)

        if target_user == request.user:
            return Response(
                {"detail": "You cannot unfollow yourself."},
                status=status.HTTP_400_BAD_REQUEST
            )

        request.user.following.remove(target_user)
        return Response(
            {"detail": f"You have unfollowed {target_user.username}"},
            status=status.HTTP_200_OK
        )
