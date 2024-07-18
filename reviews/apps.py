# from django.apps import AppConfig


# class ReviewsConfig(AppConfig):
#     name = 'reviews'
# reviews/apps.py

# from django.apps import AppConfig

# class ReviewsConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'kashish'

# app1/apps.py
from django.apps import AppConfig

class App1Config(AppConfig):
    name = 'kashish'
    label = 'kashish_label'

# kashish/apps.py
from django.apps import AppConfig

class KashishConfig(AppConfig):
    name = 'kashish'
    label = 'kashish_label'  # Ensure this is unique

