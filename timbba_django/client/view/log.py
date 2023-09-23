from ..models import Consignment,Item
from django.views import View 
import json
from django.http import JsonResponse



class Log(View):
    def put(self, request):
        data = json.loads(request.body)

        try:
            Consignment.objects.get(id=data.get("con_id"))
        except Exception as e:
            return JsonResponse({'error':'Consignment with this id does not exist'}, status=404)
        
        duplicate_log=Item.objects.filter(barcode=data.get('barcode'))
        if duplicate_log is not None:
            return JsonResponse({'error':'Log with this barcode allredy exist'}, status=404)

        try:
            consignmentObj=Consignment.objects.get(id=data.get("con_id"))
            log = Item(consignment=consignmentObj,barcode=data.get('barcode'),length=data.get('length'),volume=data.get('volume'))
            log.save()
            serialized_data = log.log_serializer()
            return JsonResponse({'message': 'log inserted successfully', 'data': serialized_data}, status=201)
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    def get(self, request):
        data = json.loads(request.body)
        log_id = data.get('id')
        try:
            log = Item.objects.get(id=log_id)
            serializer_data = log.log_serializer()
            return JsonResponse(serializer_data,status=201)
        except Item.DoesNotExist:
            return JsonResponse({'error': 'log with this id not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

class Logs(View):
    def get(self, request):
        data = json.loads(request.body)
        consignment_id = data.get('con_id')
        print("consignemnt_id",consignment_id)
        consignment_exist=Consignment.objects.filter(id=consignment_id)
        if not consignment_exist:
            return JsonResponse({'error':'Consignment with this id does not exist'}, status=404)
        try:
            logs = Item.objects.filter(consignment=consignment_id)
            serialized_data = [log.log_serializer() for log in logs]
            return JsonResponse(serialized_data, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
