from ..models import User,Client,Roles,Item
from django.views import View 
import json
from django.http import JsonResponse
from django.db.utils import IntegrityError
from datetime import datetime
import time
from django.http import HttpResponse    

class Client_(View):
    def put(self, request):
        data = json.loads(request.body)

        try:
            client = Client(name=data.get('name'),address=data.get('address'),contact=data.get('contact'),updated_at=datetime.now(),created_at=datetime.now(),email=data.get('email'))
            client.save()
            serialized_data = client.client_serializer()
            return JsonResponse({'message': 'User created successfully', 'data': serialized_data}, status=201, safe=False)

        except IntegrityError as e:
            if "Duplicate entry" in str(e):
                return JsonResponse({'error': "Client already exists"}, status=409)
            else:
                return JsonResponse({'error': str(e)}, status=500)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
