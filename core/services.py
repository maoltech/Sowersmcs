import os
import json
import requests
from django.http import JsonResponse

def assign_dedicated_account(request):
    secret_key = os.environ.get("PAYSTACK_SECRET_KEY")
    base_url = os.environ.get("PAYSTACK_BASE_URL")
    print(secret_key, base_url)
 
    endpoint = f"{base_url}/dedicated_account/assign"

    data = {
        "email": request.email,
        "first_name": request.first_name,
        "middle_name": " ",
        "last_name": request.last_name,
        "phone": request.phone,
        "preferred_bank": "test-bank",
        "country": "NG"
    }

    # Define headers with the Authorization header containing the secret key
    headers = {
        "Authorization": f"Bearer {secret_key}",
        "Content-Type": "application/json"
    }

    # Make the POST request to the Paystack API
    response = requests.post(endpoint, headers=headers, json=data)
    print(response)
    if response.status_code == 200:
        return JsonResponse(response.json())
    else:
        return JsonResponse({"error": "API request failed." }, status=500)