from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class TransactionListCreateView(APIView):
    def get(self, request):
        try:
            transactions = Transaction.objects.all().order_by("-created_at")
            serializer = TransactionSerializer(transactions, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = TransactionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TransactionDetailView(APIView):
    def get(self, request, transaction_id):
        try:
            transaction = get_object_or_404(Transaction, transaction_id=transaction_id)
            serializer = TransactionSerializer(transaction)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, transaction_id):
        try:
            transaction = get_object_or_404(Transaction, transaction_id=transaction_id)
            serializer = TransactionSerializer(transaction, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, transaction_id):
        try:
            transaction = get_object_or_404(Transaction, transaction_id=transaction_id)
            transaction.delete()
            return Response({"message": "Transaction deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Filter Views

class TransactionByPropertyId(APIView):
    def get(self, request, property_id):
        try:
            transactions = Transaction.objects.filter(property_id=property_id)
            if not transactions.exists():
                return Response({"error": "No transactions found for this property"}, status=status.HTTP_404_NOT_FOUND)
            serializer = TransactionSerializer(transactions, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TransactionByUserId(APIView):
    def get(self, request, user_id):
        try:
            transactions = Transaction.objects.filter(user_id=user_id)
            if not transactions.exists():
                return Response({"error": "No transactions found for this user"}, status=status.HTTP_404_NOT_FOUND)
            serializer = TransactionSerializer(transactions, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TransactionByUserIdAndPropertyId(APIView):
    def get(self, request, user_id, property_id):
        try:
            transactions = Transaction.objects.filter(user_id=user_id, property_id=property_id)
            if not transactions.exists():
                return Response({"error": "No transactions found for the given user and property id"}, status=status.HTTP_404_NOT_FOUND)
            serializer = TransactionSerializer(transactions, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TransactionByUserIdAndPaymentType(APIView):
    def get(self, request, user_id, payment_type):
        try:
            transactions = Transaction.objects.filter(user_id=user_id, payment_type=payment_type)
            if not transactions.exists():
                return Response({"error": "No transactions found for the given user and payment type"}, status=status.HTTP_404_NOT_FOUND)
            serializer = TransactionSerializer(transactions, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TransactionByUserIdPropertyIdAndPaymentType(APIView):
    def get(self, request, user_id, property_id, payment_type):
        try:
            transactions = Transaction.objects.filter(user_id=user_id, property_id=property_id, payment_type=payment_type)
            if not transactions.exists():
                return Response({"error": "No transactions found for the given user, property, and payment type"}, status=status.HTTP_404_NOT_FOUND)
            serializer = TransactionSerializer(transactions, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
