
from django.urls import path
# from .views import UserAPIView
# from .views import UsersApiView
# from .views import CreateConsignment
# from .views import Log
# from .views import Logs
from .view import consignment, log,user,client,role
from django.views.decorators.csrf import csrf_exempt

# URLConf
urlpatterns = [
    path('demo/',csrf_exempt(user.Demo.as_view())),
    path('user/',csrf_exempt(user.User_.as_view())),
    path('users/',csrf_exempt(user.Users.as_view())),
    path('consignment/',csrf_exempt(consignment.Consignment_.as_view())),
    path('consignments/',csrf_exempt(consignment.Consignments.as_view())),
    path('log/',csrf_exempt(log.Log.as_view())),
    path('logs/',csrf_exempt(log.Logs.as_view())),
    path('client/',csrf_exempt(client.Client_.as_view())),
    path('role/',csrf_exempt(role.Role_.as_view()))
]
