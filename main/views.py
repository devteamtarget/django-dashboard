from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render
import requests

# ✅ FastAPI API ka Base URL
FASTAPI_URL = "http://127.0.0.1:8000"

def dashboard(request):
    """Dashboard Page Render karega"""
    return render(request, "dashboard.html")

def get_latest_price(request):
    """FastAPI se latest price fetch karega"""
    response = requests.get(f"{FASTAPI_URL}/latest_price")
    return JsonResponse(response.json())

def start_cron(request):
    """FastAPI se cron job start karega"""
    response = requests.get(f"{FASTAPI_URL}/start")
    return JsonResponse(response.json())

def stop_cron(request):
    """FastAPI se cron job stop karega"""
    response = requests.get(f"{FASTAPI_URL}/stop")
    return JsonResponse(response.json())
