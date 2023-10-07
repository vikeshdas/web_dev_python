from ..models import User,Client,Consignment
from django.views import View 
import json
from django.http import JsonResponse


class ConsignmentView(View):
    """
        View for handling client related operations 

        Methods:
            put(self,request): Creates new consignment
            get(self,request): Fetch details of a consignmetn
    """
    def put(self, request):
        """
            Create a new consignment

            Args: 
                request: Https request object contains information of a consignment
            
            Return:
                JsonResponse: return a josn about an error or success.
        """
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
        """
            Fetch details of a consignment from databasea by Id.

            Args: 
                request : Http request object ,contains consignment Id.
            
            Retruns:
                JsonResponse: Details of a consignment.if Id not find in Database return a error message.
        """
        data = json.loads(request.body)
        cons_id = data.get('con_id')
        try:
            consignment = Consignment.objects.get(id=cons_id)
        except Consignment.DoesNotExist:
            return JsonResponse({'error': 'Consignment with this id not found'}, status=404)
        
        serialized_data = consignment.con_serializer() 
        return JsonResponse(serialized_data,status=201)
    
class Consignments(View):
    """
        Handles operation releted to more then one consignments

        Method:
            get(self,request): Fetch all consignments of a perticular client.
    """
    def get(self, request):
        """
            Retrive information of all consignments of a perticular client.

            Args:
               request (HttpRequest): Http request object contais client Id.

            Returns:
                JsonResponse: A json response with list of consignmens of a perticular client. 
        """
        data = json.loads(request.body)
        client_id = data.get('client_id')
        try:
            client_exist=Client.objects.get(id=client_id)
        except Exception as e:
            return JsonResponse({'error': 'Client not found with this id'}, status=404)
    
        consignments = Consignment.objects.filter(client_id=client_id)
        serialized_data = [cons.con_serializer() for cons in consignments]
        return JsonResponse({"consignments":serialized_data}, status=200)