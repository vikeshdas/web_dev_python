from ..models import Roles
from django.views import View 
import json
from django.http import JsonResponse
from django.db.utils import IntegrityError
 


class RoleView(View):
    """
        View class to handle Role related operation like create role.Role can be like mobile,web .mobile means user can 
        access information using only mobile,or web or boath.

        Mthods:
            put(self,request): Create a new role.

    """
    def put(self, request):
        """
            Create new role.

            Args:
                request (HttpRequest): rquest object contains information of a role to save in databse.
            
            Reponse(jsonResponse):return jsonresponse either role creaated succesfully or error.
        """
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