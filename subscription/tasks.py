# import threading
# import time
# from datetime import timedelta
# from django.core.mail import EmailMessage
# from django.utils import timezone
# from datetime import timezone as dt_timezone
# from django.conf import settings
# from .models import *
# from django.db.models import Q
# from django.core.mail import send_mail
# import os 
# import random
# from io import BytesIO
# from django.template.loader import render_to_string
# from datetime import datetime, date
# current_date = date.today()

# def update_subscription_status():

#     while True:
#         subscriptions = Subscription.objects.all()    
#         for i in subscriptions:
            
#             if current_date == i.subscription_end_date:
#                 i.subscription_status="unpaid"
#                 i.save()
#         time.sleep(1)  


# def start_thread():
#     printer_thread = threading.Thread(target=update_subscription_status)
#     printer_thread.daemon = True
#     printer_thread.start()






import threading
import time
from datetime import date
from .models import Subscription

current_date = date.today()

def update_subscription_status():
    while True:
        try:
            subscriptions = Subscription.objects.all()
            for i in subscriptions:
                if current_date == i.subscription_end_date:
                    i.subscription_status = "unpaid"
                    i.save()
        except Exception as e:
            print("Error in update_subscription_status:", e)

        time.sleep(1)

def start_thread():
    printer_thread = threading.Thread(target=update_subscription_status)
    printer_thread.daemon = True
    printer_thread.start()


