from django.shortcuts import render
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *

from .serializers import SubscriptionPlanSerializer, SubscriptionSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SubscriptionPlan, SubscriptionPlanVariant, Subscription
from .serializers import (
    SubscriptionPlanSerializer,
    SubscriptionPlanVariantSerializer,
    SubscriptionSerializer
)
from django.shortcuts import get_object_or_404
from users.models import User  # Import your custom user model if needed

# ------------------ Subscription Plan ------------------


# List and Create Subscription Plans (e.g., Connect, Connect+, Relax)
class SubscriptionPlanListCreateView(APIView):
    def get(self, request):
        try:
            plans = SubscriptionPlan.objects.all()
            serializer = SubscriptionPlanSerializer(plans, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = SubscriptionPlanSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)





# ------------------ Subscription Plan ------------------

class SubscriptionPlanDetailView(APIView):
    def get(self, request, pk):
        try:
            plan = get_object_or_404(SubscriptionPlan, pk=pk)
            serializer = SubscriptionPlanSerializer(plan)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            plan = get_object_or_404(SubscriptionPlan, pk=pk)
            serializer = SubscriptionPlanSerializer(plan, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            plan = get_object_or_404(SubscriptionPlan, pk=pk)
            plan.delete()
            return Response({"message": "Subscription Plan deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# ------------------ Subscription Plan Variant ------------------


# List and Create Plan Variants (e.g., Connect+ 45 days, Connect+ 90 days)
class SubscriptionPlanVariantListCreateView(APIView):
    def get(self, request):
        try:
            variants = SubscriptionPlanVariant.objects.select_related("plan_id").all()
            serializer = SubscriptionPlanVariantSerializer(variants, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = SubscriptionPlanVariantSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class SubscriptionPlanVariantDetailView(APIView):
    def get(self, request, pk):
        try:
            variant = get_object_or_404(SubscriptionPlanVariant, pk=pk)
            serializer = SubscriptionPlanVariantSerializer(variant)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            variant = get_object_or_404(SubscriptionPlanVariant, pk=pk)
            serializer = SubscriptionPlanVariantSerializer(variant, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            variant = get_object_or_404(SubscriptionPlanVariant, pk=pk)
            variant.delete()
            return Response({"message": "Subscription Plan Variant deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        





# ------------------ Subscription ------------------


# Create Subscription for User
class SubscriptionListCreateView(APIView):
    def get(self, request):
        try:
            subcriptions = Subscription.objects.all()
            serializer = SubscriptionSerializer(subcriptions, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = SubscriptionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message": "Subscription created successfully", "data": serializer.data},
                    status=status.HTTP_201_CREATED
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SubscriptionDetailView(APIView):
    def get(self, request, pk):
        try:
            subscription = get_object_or_404(Subscription, pk=pk)
            serializer = SubscriptionSerializer(subscription)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            subscription = get_object_or_404(Subscription, pk=pk)
            serializer = SubscriptionSerializer(subscription, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            subscription = get_object_or_404(Subscription, pk=pk)
            subscription.delete()
            return Response({"message": "Subscription deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


# Get Subscriptions of a User
class UserSubscriptionsView(APIView):
    def get(self, request, user_id):
        try:
            subscription = Subscription.objects.get(user_id=user_id)
            serializer = SubscriptionSerializer(subscription)  # no many=True
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Subscription.DoesNotExist:
            return Response({'error': 'Subscription not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




# Get Subscription Plans based on user_type
class SubscriptionPlanByUserTypeView(APIView):
    def get(self, request, user_type):
        try:
            plans = SubscriptionPlan.objects.filter(user_type=user_type)
            serializer = SubscriptionPlanSerializer(plans, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Get Subscription Plan Variants based on user_type
class SubscriptionPlanVariantByUserTypeView(APIView):
    def get(self, request, user_type):
        try:
            variants = SubscriptionPlanVariant.objects.select_related("plan_id").filter(plan_id__user_type=user_type)
            serializer = SubscriptionPlanVariantSerializer(variants, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
