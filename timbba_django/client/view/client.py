from ..models import Client
from django.views import View 
import json
from django.http import JsonResponse
from django.db.utils import IntegrityError
from datetime import datetime
   

class ClientView(View):
    """
        A view for handling client related operation like create a new client.
        A client is a admin who buy subscription for our application or we can 
        say that client is a owner of a factory who makes logs to plyboard.
    """
    def put(self, request):
        """
            Create a new client.This function will require when client will buy subscription.
            When client signup then this function will be executing.

            Args:
                HttpRequest :Contains client data in request body.

            Returns:
                JsonResponse:return json, that client is created successfully. 
        """
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
        
