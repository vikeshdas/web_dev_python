from ..models import User,Client,Consignment,Item
from django.views import View 
import json
from django.http import JsonResponse
from django.db.utils import IntegrityError
import datetime
import time
from django.http import HttpResponse




class User_(View):
    def patch(self, request):
        try:
            data = json.loads(request.body)
            user_id = data.get('id')
            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                return JsonResponse({'error': 'User not found'}, status=404)
            user.name = data.get('name',user.name)
            user.username = data.get('username', user.username)
            user.role_id = data.get('role', user.role_id)
            user.contact = data.get('contact', user.contact)
            user.client_id = data.get('client_id', user.client_id)
            user.save()
            return JsonResponse({'message': 'User updated successfully'}, status=200)
        
        except IntegrityError as e:
            if "Duplicate entry" in str(e) and "for key 'client_user.username'" in str(e):
                return JsonResponse({'error': "This username already exists"}, status=409)
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


    def put(self, request):
        data = json.loads(request.body)

        try:
            duplicate_username = User.objects.filter(username=data.get('username'))
            contact_duplicate= User.objects.filter(contact=data.get('contact'))
            if duplicate_username.exists():
                return JsonResponse({"error": "User with this username already exists"}, status=409, safe=False)
            if contact_duplicate:
                return JsonResponse({"error": "User with this contact number already exists"}, status=409, safe=False)

            user = User(name=data.get('name'),username=data.get('username'),role_id=data.get('role'),contact=data.get('contact'),client_id=data.get('client_id'))
            user.save()
            serialized_data = user.user_serializer()
            return JsonResponse({'message': 'User created successfully', 'data': serialized_data}, status=201, safe=False)

        except IntegrityError as e:
            if "Duplicate entry" in str(e):
                return JsonResponse({'error': "User already exists"}, status=409)
            else:
                return JsonResponse({'error': str(e)}, status=500)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    def get(self, request):
        data = json.loads(request.body)
        user_id = data.get('id')
        # check for client_id as wll for user.
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        
        serialized_data = user.user_serializer() 
        return JsonResponse(serialized_data,status=200)
    

    def delete(self, request):
        data = json.loads(request.body)
        user_id = data.get('id')
        
        try:
            user = User.objects.get(id=user_id)
            user.delete()
            return JsonResponse({'message': 'User deleted successfully'},status=204)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


class Users(View):
    def get(self, request):
        data = json.loads(request.body)
        client_id = data.get('client_id')
        if not Client.objects.filter(id=client_id):
            return JsonResponse({"error": "There is no such client"}, status=409, safe=False)
        try:
            users = User.objects.filter(client_id=client_id)
            serialized_data = [user.user_serializer() for user in users]
            return JsonResponse(serialized_data, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
class Demo(View):
    def get(self, request):
        x = request.GET.get('x')
        print("REQUEST ",x,"START")
        # time.sleep(5)
        for i in range(1000000):
            print("",end="")
        print("REQUEST ",x,"END")
        return HttpResponse("Response after delay")