from ..models import User,Client,Roles,Item
from django.views import View 
import json
from django.http import JsonResponse
from django.db.utils import IntegrityError
from datetime import datetime
import time
from django.http import HttpResponse    


class Role_(View):
    def put(self, request):
        data = json.loads(request.body)

        try:
            role = Roles(name=data.get('name'))
            role.save()
            serialized_data = role.role_serializer()
            return JsonResponse({'message': 'Role created successfully', 'data': serialized_data}, status=201, safe=False)

        except IntegrityError as e:
            if "Duplicate entry" in str(e):
                return JsonResponse({'error': "Role already exists"}, status=409)
            else:
                return JsonResponse({'error': str(e)}, status=500)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)