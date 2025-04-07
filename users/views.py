
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *




class LoginAPIView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        try:
            user = User.objects.get(email=email)
            print(user)
            if check_password(password, user.password):
                # Fetch the user's roles
                roles = user.roles.values_list('role_name', flat=True)  # Get role names as a list
                
                return Response(
                    {
                        "message": "Login successful",
                        "user_id": user.user_id,
                        "roles": list(roles),  # Convert QuerySet to list
                    },
                    status=status.HTTP_200_OK
                )
            else:
                return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)




# Logout API 
class LogoutAPIView(APIView):
    def post(self, request):
        return Response({"message": "Logged out successfully!"}, status=status.HTTP_200_OK)

class RoleListCreateView(APIView):
    def get(self, request):
        roles = Role.objects.all()
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoleDetailView(APIView):
    def get(self, request, role_id):
        role = get_object_or_404(Role, role_id=role_id)
        serializer = RoleSerializer(role)
        return Response(serializer.data)

    def put(self, request, role_id):
        role = get_object_or_404(Role, role_id=role_id)
        serializer = RoleSerializer(role, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, role_id):
        role = get_object_or_404(Role, role_id=role_id)
        role.delete()
        return Response({"message": "Role deleted successfully"},status=status.HTTP_204_NO_CONTENT)


class UserListCreateView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data.copy()
        if "password" in data and not data["password"].startswith("pbkdf2_sha256$"):
            data["password"] = make_password(data["password"])
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class UserDetailView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User, user_id=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, user_id):
        user = get_object_or_404(User, user_id=user_id)
        data = request.data.copy()
        if 'password' in data:
            data['password'] = make_password(data['password'])  # Hash new password
        serializer = UserSerializer(user, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id):
        user = get_object_or_404(User, user_id=user_id)
        user.delete()
        return Response({"message": "User deleted successfully"},status=status.HTTP_204_NO_CONTENT)



class UsersByRoleAPIView(APIView):
    def get(self, request, role_name):
        try:
            role = Role.objects.get(role_name=role_name)
            users = User.objects.filter(roles=role).distinct()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data, status=200)
        except Role.DoesNotExist:
            return Response({"error": f"Role '{role_name}' not found"}, status=404)
