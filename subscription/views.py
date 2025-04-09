from django.shortcuts import render

# Create your views here.


# subscriptions/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import SubscriptionPlan, Subscription
from .serializers import SubscriptionPlanSerializer, SubscriptionSerializer

# Subscription Plan APIs
# class SubscriptionPlanListCreateView(APIView):
#     def get(self, request):
#         plans = SubscriptionPlan.objects.all()
#         serializer = SubscriptionPlanSerializer(plans, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = SubscriptionPlanSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class SubscriptionPlanDetailView(APIView):
#     def get(self, request, plan_id):
#         plan = get_object_or_404(SubscriptionPlan, plan_id=plan_id)
#         serializer = SubscriptionPlanSerializer(plan)
#         return Response(serializer.data)

#     def put(self, request, plan_id):
#         plan = get_object_or_404(SubscriptionPlan, plan_id=plan_id)
#         serializer = SubscriptionPlanSerializer(plan, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, plan_id):
#         plan = get_object_or_404(SubscriptionPlan, plan_id=plan_id)
#         plan.delete()
#         return Response({"message": "Subscription plan deleted successfully"}, status=status.HTTP_204_NO_CONTENT)





# subscriptions/views.py (continued)

# Subscription APIs
# class SubscriptionListCreateView(APIView):
#     def get(self, request):
#         subscriptions = Subscription.objects.all()
#         serializer = SubscriptionSerializer(subscriptions, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = SubscriptionSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class SubscriptionDetailView(APIView):
#     def get(self, request, subscription_id):
#         subscription = get_object_or_404(Subscription, subscription_id=subscription_id)
#         serializer = SubscriptionSerializer(subscription)
#         return Response(serializer.data)

#     def put(self, request, subscription_id):
#         subscription = get_object_or_404(Subscription, subscription_id=subscription_id)
#         serializer = SubscriptionSerializer(subscription, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, subscription_id):
#         subscription = get_object_or_404(Subscription, subscription_id=subscription_id)
#         subscription.delete()
#         return Response({"message": "Subscription deleted successfully"}, status=status.HTTP_204_NO_CONTENT)



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


# List and Create Subscription Plans (e.g., Connect, Connect+, Relax)
class SubscriptionPlanListCreateView(APIView):
    def get(self, request):
        plans = SubscriptionPlan.objects.all()
        serializer = SubscriptionPlanSerializer(plans, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SubscriptionPlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# List and Create Plan Variants (e.g., Connect+ 45 days, Connect+ 90 days)
class SubscriptionPlanVariantListCreateView(APIView):
    def get(self, request):
        variants = SubscriptionPlanVariant.objects.select_related("plan").all()
        serializer = SubscriptionPlanVariantSerializer(variants, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SubscriptionPlanVariantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create Subscription for User
class SubscribeUserView(APIView):
    def post(self, request):
        serializer = SubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Subscription created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Get Subscriptions of a User
class UserSubscriptionsView(APIView):
    def get(self, request, user_id):
        subscriptions = Subscription.objects.filter(user_id=user_id).select_related('subscription_variant__plan')
        serializer = SubscriptionSerializer(subscriptions, many=True)
        return Response(serializer.data)



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import SubscriptionPlan, SubscriptionPlanVariant, Subscription
from .serializers import (
    SubscriptionPlanSerializer,
    SubscriptionPlanVariantSerializer,
    SubscriptionSerializer
)


# ------------------ Subscription Plan ------------------

class SubscriptionPlanDetailView(APIView):
    def get(self, request, pk):
        plan = get_object_or_404(SubscriptionPlan, pk=pk)
        serializer = SubscriptionPlanSerializer(plan)
        return Response(serializer.data)

    def put(self, request, pk):
        plan = get_object_or_404(SubscriptionPlan, pk=pk)
        serializer = SubscriptionPlanSerializer(plan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        plan = get_object_or_404(SubscriptionPlan, pk=pk)
        plan.delete()
        return Response({"message": "Subscription Plan deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


# ------------------ Subscription Plan Variant ------------------

class SubscriptionPlanVariantDetailView(APIView):
    def get(self, request, pk):
        variant = get_object_or_404(SubscriptionPlanVariant, pk=pk)
        serializer = SubscriptionPlanVariantSerializer(variant)
        return Response(serializer.data)

    def put(self, request, pk):
        variant = get_object_or_404(SubscriptionPlanVariant, pk=pk)
        serializer = SubscriptionPlanVariantSerializer(variant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        variant = get_object_or_404(SubscriptionPlanVariant, pk=pk)
        variant.delete()
        return Response({"message": "Subscription Plan Variant deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


# ------------------ Subscription ------------------

class SubscriptionDetailView(APIView):
    def get(self, request, pk):
        subscription = get_object_or_404(Subscription, pk=pk)
        serializer = SubscriptionSerializer(subscription)
        return Response(serializer.data)

    def put(self, request, pk):
        subscription = get_object_or_404(Subscription, pk=pk)
        serializer = SubscriptionSerializer(subscription, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        subscription = get_object_or_404(Subscription, pk=pk)
        subscription.delete()
        return Response({"message": "Subscription deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
