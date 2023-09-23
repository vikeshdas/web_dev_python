import json
from django.http import JsonResponse
from django.views import View 

class Demo(View):
    def get(self, request):
        print("reached here")
        res="Reached"
        return JsonResponse(res,status=200)