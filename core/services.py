# import os
# import json
# import requests
# from django.http import JsonResponse
# from django.conf import settings

# def assign_dedicated_account(email, firstName, lastName, phone):
#     secret_key = settings.PAYSTACK_SECRET_KEY
#     base_url = settings.PAYSTACK_BASE_URL
#     # secret_key = os.environ.get("PAYSTACK_SECRET_KEY")
#     # base_url = os.environ.get("PAYSTACK_BASE_URL")
#     print(secret_key, base_url)
 
#     endpoint = f"{base_url}/dedicated_account/assign"

#     data = {
#         "email": email,
#         "first_name": firstName,
#         "middle_name": " ",
#         "last_name": lastName,
#         "phone": phone,
#         "preferred_bank": "test-bank",
#         "country": "NG"
#     }

#     # Define headers with the Authorization header containing the secret key
#     headers = {
#         "Authorization": f"Bearer {secret_key}",
#         "Content-Type": "application/json"
#     }

#     # Make the POST request to the Paystack API
#     response = requests.post(endpoint, headers=headers, json=data)
#     print(response)
#     if response.status_code == 200:
#         return JsonResponse(response.json())
#     else:
#         return JsonResponse({"error": "API request failed." }, status=500)from rave_python import Rave


from rave_python import Rave
from django.conf import settings

def assign_dedicated_account(email, firstName, lastName, middleName, BVN, phone):
    print(email, firstName, lastName, middleName, BVN, phone)
    secret_key = settings.FLW_SECRET_KEY
    public_key = settings.FLW_PUBLIC_KEY
   
    rave = Rave(public_key,secret_key, usingEnv=False )

    res = rave.VirtualAccount.create({
        "email": email,
        "narration": firstName +" "+ lastName +" "+ middleName,
        "is_permanent": True,
        "bvn": BVN,
        "tx_ref": "VA12",
        "phonenumber": phone,
        "firstname": firstName,
        "lastname": lastName,
    })
    
    response_code = res['data']['response_code']
    data =  res['data']
    if response_code == '02':
        return data
    else:
        return data