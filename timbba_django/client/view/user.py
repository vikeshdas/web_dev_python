from ..models import User,Client
from django.views import View 
import json
from django.http import JsonResponse
from django.db.utils import IntegrityError




class UserView(View):
    """
        A View class to handle user related operations like create new user,fetch information of a user , 
        update a user and delete a user.

        Methods:
            patch(self,request):Update user information in a databse.
            put(self,request): create new user 
            get(self,request): fetch information of a user from database based on user_id.
            delete(self,request): delete a perticuar user from database based on user_id.
    """
    def patch(self, request):
        """
            update infromation of a user based on user id.

            Args:
                request:HttpRequest's object contains user id.
            
            Returns(jsonResponse): return a message in json form either successfully updated or error.
        """
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
        """
            Create a new user with unique username and contact number,means save information of user in databse.

            Args:
                request:HttpRequest's object contains information of a user to save in databasea.
            
            Returns:
                JsonResponse : Returns message in josnform either data saved successfully or fail.
        """
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
        """
            Fetch informatins of a user from database, based on user_id.

            Args:
                request: Httprequest's object containse id of a user.
            
            Returns: JsonResponse: returns information of a user in the jsonform.
        """
        data = json.loads(request.body)
        user_id = data.get('id')
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        
        serialized_data = user.user_serializer() 
        return JsonResponse(serialized_data,status=200)
    

    def delete(self, request):

        """
            Delete a user from databse based on user_id.

            Args:
                HttpRequest's object contains user id, whose information need to delete.
            
            Returns: returns message in jsonform either user deleted successfully or error.
        """
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
    """
      A view class handles operation related more then user.like get information of all users related to a client.

      Methods:
        get(self,request): get information of all users of a client

    """
    def get(self, request):
        """
            Fetch all user of a client based on client_id .if client exist in database

            Args:
                request: HttpRequest's object contains client_id whose all user need to fetch from database.
            
            Return: Return information of all user of a client in the jsonform or error if client is invalid.
                
        """
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
        