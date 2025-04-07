from django.urls import path
from .views import *

urlpatterns = [
    
    # Commission URLs
    path('commissions/', CommissionListCreateView.as_view(), name='commission-list-create'),
    path('commissions/<int:commission_id>/', CommissionDetailView.as_view(), name='commission-detail'),
    path('commissions/partner-id/<int:partner_id>/', CommissionByPartnerId.as_view(), name='commissions-partner-id'),
]