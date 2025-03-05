from django.urls import path
from .views import dashboard, get_latest_price, start_cron, stop_cron

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("get_price/", get_latest_price, name="get_price"),
    path("start_cron/", start_cron, name="start_cron"),
    path("stop_cron/", stop_cron, name="stop_cron"),
]
