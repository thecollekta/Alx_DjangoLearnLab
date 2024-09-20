# social_media_api/accounts/views.py

from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import RegisterSerializer, CustomUserSerializer, LoginSerializer
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from rest_framework import permissions

# Registration View to Return a Token
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                'status': 'User created successfully',
                'token': token.key,
                'user': {
                    'username': user.username,
                    'bio': user.bio
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Login View to Return a Token
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({
                    'token': token.key
                }, status=status.HTTP_200_OK)
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Profile View for Profile Management    
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = CustomUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request):
        user = request.user
        serializer = CustomUserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Follow a user
class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()

    def post(self, request, user_id):
        try:
            user_to_follow = self.get_queryset().get(id=user_id)
            if user_to_follow == request.user:
                return Response({"error": "You cannot follow yourself"}, 
                                status=status.HTTP_400_BAD_REQUEST)
            request.user.following.add(user_to_follow)
            return Response({"message": "User followed successfully"}, 
                            status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found"}, 
                            status=status.HTTP_404_NOT_FOUND)


# Unfollow a user
class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()

    def post(self, request, user_id):
        try:
            user_to_unfollow = self.get_queryset().get(id=user_id)
            request.user.following.remove(user_to_unfollow)
            return Response({"message": "User unfollowed successfully"}, 
                            status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found"}, 
                            status=status.HTTP_404_NOT_FOUND)
