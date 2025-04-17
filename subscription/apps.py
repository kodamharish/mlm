# from django.apps import AppConfig


# class SubscriptionConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'subscription'

#     def ready(self):
#         from . import tasks
#         tasks.start_thread()

# subscription/apps.py

from django.apps import AppConfig
import sys

class SubscriptionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'subscription'

    def ready(self):
        if 'runserver' in sys.argv:
            from .tasks import start_thread
            start_thread()




    