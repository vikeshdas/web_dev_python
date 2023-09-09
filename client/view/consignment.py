from ..models import User,Client,Consignment,Item
from django.views import View 
import json
from django.http import JsonResponse
from django.db.utils import IntegrityError
from django.db.models import Q


class Consignment_(View):
    def put(self, request):
        data = json.loads(request.body)

        try:
            try:
                client = Client.objects.get(id=data.get('client_id'))
            except Client.DoesNotExist:
                return JsonResponse({"error": "client_id does not exist"}, status=404)
            try:
                user = User.objects.get(id=data.get('user_id'))
            except User.DoesNotExist:
                return JsonResponse({"error": "user_id does not exist"}, status=404)
            duplicate_consignment=Consignment.objects.filter(client_id=client).filter(created_by=user).filter(name=data.get('name'))
            if not duplicate_consignment.exists():
                consignment = Consignment(name=data.get('name'),type=data.get('type'),client_id=client,created_by=user,updated_by=user)
                consignment.save()
                serialize_data=consignment.con_serializer()
                return JsonResponse({'message': 'Consignment created successfully', 'data': serialize_data}, status=201)
            else:
                return JsonResponse({'message': 'Consignment allredy exist'}, status=409)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def get(self, request):
        data = json.loads(request.body)
        cons_id = data.get('con_id')
        try:
            consignment = Consignment.objects.get(id=cons_id)
        except Consignment.DoesNotExist:
            return JsonResponse({'error': 'Consignment with this id not found'}, status=404)
        
        serialized_data = consignment.con_serializer() 
        return JsonResponse(serialized_data,status=201)
    
class Consignments(View):
    def get(self, request):
        data = json.loads(request.body)
        client_id = data.get('client_id')
        try:
            client_exist=Client.objects.get(id=client_id)
        except Exception as e:
            return JsonResponse({'error': 'Client not found with this id'}, status=404)
    
        consignments = Consignment.objects.filter(client_id=client_id)
        serialized_data = [cons.con_serializer() for cons in consignments]
        return JsonResponse({"consignments":serialized_data}, status=200)