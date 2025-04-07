
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *

# Commission APIs
class CommissionListCreateView(APIView):
    def get(self, request):
        commissions = Commission.objects.all()
        serializer = CommissionSerializer(commissions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CommissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommissionDetailView(APIView):
    def get(self, request, commission_id):
        commission = get_object_or_404(Commission, commission_id=commission_id)
        serializer = CommissionSerializer(commission)
        return Response(serializer.data)

    def put(self, request, commission_id):
        commission = get_object_or_404(Commission, commission_id=commission_id)
        serializer = CommissionSerializer(commission, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, commission_id):
        commission = get_object_or_404(Commission, commission_id=commission_id)
        commission.delete()
        return Response({"message": "Commission deleted successfully"}, status=status.HTTP_204_NO_CONTENT)




class CommissionByPartnerId(APIView):
    def get(self, request, partner_id):
        commissions = Commission.objects.filter(partner_id=partner_id)

        if not commissions.exists():
            return Response({"error": "No commissions found for this partner"}, status=404)
        
        serializer = CommissionSerializer(commissions, many=True)
        return Response(serializer.data)
