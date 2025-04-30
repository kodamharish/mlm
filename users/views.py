
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
                        "referral_id":user.referral_id,
                        "referred_by": user.referred_by,
                        "first_name":user.first_name,
                        "last_name": user.last_name,
                        "email": user.email,
                        "phone_number": user.phone_number,
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
        try:
            roles = Role.objects.all()
            serializer = RoleSerializer(roles, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = RoleSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RoleDetailView(APIView):
    def get(self, request, role_id):
        try:
            role = get_object_or_404(Role, role_id=role_id)
            serializer = RoleSerializer(role)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, role_id):
        try:
            role = get_object_or_404(Role, role_id=role_id)
            serializer = RoleSerializer(role, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, role_id):
        try:
            role = get_object_or_404(Role, role_id=role_id)
            role.delete()
            return Response({"message": "Role deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



# class UserListCreateView(APIView):
#     def get(self, request):
#         try:
#             users = User.objects.all()
#             serializer = UserSerializer(users, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#     def post(self, request):
#         try:
#             data = request.data.copy()
#             if "password" in data and not data["password"].startswith("pbkdf2_sha256$"):
#                 data["password"] = make_password(data["password"])
#             serializer = UserSerializer(data=data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class UserListCreateView(APIView):
    def get(self, request):
        try:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            data = request.data.copy()

            if "password" in data and not data["password"].startswith("pbkdf2_sha256$"):
                data["password"] = make_password(data["password"])

            role_ids = data.get("role_ids", [])
            agent_role = Role.objects.filter(role_name="Agent").first()

            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                user = serializer.save()


                if agent_role and agent_role in user.roles.all():
                    agent_count = User.objects.filter(roles=agent_role).exclude(referral_id__isnull=True).exclude(user_id=user.user_id).count()
                    referral_id = f"SRP{str(agent_count + 1).zfill(6)}"
                    user.referral_id = referral_id
                    user.save(update_fields=['referral_id'])


                return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class UserDetailView(APIView):
    def get(self, request, user_id):
        try:
            user = get_object_or_404(User, user_id=user_id)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, user_id):
        try:
            user = get_object_or_404(User, user_id=user_id)
            data = request.data.copy()
            if 'password' in data:
                data['password'] = make_password(data['password'])  # Hash new password
            serializer = UserSerializer(user, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, user_id):
        try:
            user = get_object_or_404(User, user_id=user_id)
            user.delete()
            return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class UsersByRoleAPIView(APIView):
    def get(self, request, role_name):
        try:
            role = Role.objects.get(role_name=role_name)
            users = User.objects.filter(roles=role).distinct()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data, status=200)
        except Role.DoesNotExist:
            return Response({"error": f"Role '{role_name}' not found"}, status=404)

# class UsersByReferralIdAPIView(APIView):
#     def get(self, request, referral_id):
#         try:
#             users = User.objects.filter(referred_by=referral_id).order_by('created_at')
#             serializer = UserSerializer(users, many=True)
#             return Response(serializer.data, status=200)
#         except User.DoesNotExist:
#             return Response({"error": f"Users with '{referral_id}' not found"}, status=404)
        







class UsersByReferralIdAPIView(APIView):
    def get(self, request, referral_id):
        try:
            users = User.objects.filter(referred_by=referral_id).order_by('created_at')
            user_count = users.count()  # Count the number of users with that referral_id
            serializer = UserSerializer(users, many=True)
            return Response({
                "users": serializer.data,
                "total_agents": user_count  # Include the count of users
            }, status=200)
        except User.DoesNotExist:
            return Response({"error": f"Users with '{referral_id}' not found"}, status=404)

       

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count, Q
from django.utils import timezone
from datetime import timedelta

from property.models import  Property

class CountAPIView(APIView):
    def get(self, request):
        # Calculate the date one month ago from today
        one_month_ago = timezone.now() - timedelta(days=30)

        # Aggregate counts for users
        user_counts = User.objects.aggregate(
            # Role based counts
            total_admins=Count('user_id', filter=Q(roles__role_name__iexact='Admin'), distinct=True),
            total_clients=Count('user_id', filter=Q(roles__role_name__iexact='Client'), distinct=True),
            total_agents=Count('user_id', filter=Q(roles__role_name__iexact='Agent'), distinct=True),
            
            # Active/Inactive counts (charfield comparison)
            total_active_users=Count('user_id', filter=Q(status__iexact="Active"), distinct=True),
            total_inactive_users=Count('user_id', filter=Q(status__iexact="Inactive"), distinct=True),
        )

        # Aggregate counts for properties
        property_counts = Property.objects.aggregate(
            total_properties=Count('property_id', distinct=True),
            total_latest_properties=Count('property_id', distinct=True, filter=Q(created_at__gte=one_month_ago)),
        )

        # Combine the counts
        counts = {**user_counts, **property_counts}

        return Response(counts, status=status.HTTP_200_OK)
