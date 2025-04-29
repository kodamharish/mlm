from rest_framework import serializers
from .models import *

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'




# class UserSerializer(serializers.ModelSerializer):
#     roles = RoleSerializer(many=True, read_only=True)  # For response
#     role_ids = serializers.PrimaryKeyRelatedField(     # For creating/updating
#         queryset=Role.objects.all(), write_only=True, many=True, source="roles"
#     )

#     class Meta:
#         model = User
#         fields = '__all__'



class UserSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(many=True, read_only=True)  # For response
    role_ids = serializers.PrimaryKeyRelatedField(     # For creating/updating
        queryset=Role.objects.all(), write_only=True, many=True, source="roles"
    )
    referral_id = serializers.CharField(read_only=True)  # Include in response, not required from input
    #referred_by = serializers.CharField(read_only=True)  # Include in response, not required from input
    level_no = serializers.CharField(read_only=True)  # Include in response, not required from input


    class Meta:
        model = User
        fields = '__all__'


# class UserSerializer(serializers.ModelSerializer):
#     roles = RoleSerializer(many=True, read_only=True)
#     role_ids = serializers.PrimaryKeyRelatedField(
#         queryset=Role.objects.all(), write_only=True, many=True, source="roles"
#     )

#     class Meta:
#         model = User
#         # exclude = ['password']
#         fields = '__all__'


#     def create(self, validated_data):
#         roles = validated_data.pop("roles", [])
#         user = User.objects.create(**validated_data)
#         user.roles.set(roles)
#         return user

#     def update(self, instance, validated_data):
#         roles = validated_data.pop("roles", None)
#         if roles is not None:
#             instance.roles.set(roles)
#         return super().update(instance, validated_data)

