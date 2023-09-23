
from django.conf import settings
from django.db import models

class Roles(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def role_serializer(self):
        return {
            'id': self.id,
            'name': self.name,
        }

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.TextField()
    contact = models.CharField(max_length=20) 
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()

    def client_serializer(self, include_fields=None):
            return {
                'id': self.id,
                'name': self.name,
                'address': self.address,
                'contact': self.contact,
                'updated_at': self.updated_at,
                'created_at': self.created_at,
                'email': self.email,
            }

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)
    contact = models.CharField(max_length=20)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def user_serializer(self):
        role_data = self.role.id  if self.role else None
        client_id = self.client.id if self.client else None

        return {
            'id': self.id,
            'name': self.name,
            'username': self.username,
            'role_id': role_data,
            'contact': self.contact,
            'client_id': client_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }


class UserRole(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)



class DataEntity(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Consignment(models.Model):
    TYPE_CHOICES = (
        ('Type1', 'Type 1'),
        ('Type2', 'Type 2'),
    )
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_consignments')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='updated_consignments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def con_serializer(self):
        client_id = self.client_id.id if self.client_id else None
        user_id = self.created_by.id if self.created_by else None

        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'client_id': client_id,
            'created_by':user_id,
            'updated_by': user_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }

class Item(models.Model):
    consignment = models.ForeignKey(Consignment, on_delete=models.CASCADE)
    barcode = models.CharField(max_length=50)
    length = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.DecimalField(max_digits=10, decimal_places=2)
    def log_serializer(self):
        con_id = self.consignment.id if self.consignment else None
        return {
            'consignment_id': con_id,
            'barcode': self.barcode,
            'length': self.length,
            'volume': self.volume
        }
    
class Logs(models.Model):
    consignment = models.ForeignKey(Consignment, on_delete=models.CASCADE)
    barcode = models.CharField(max_length=50)
    length = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.DecimalField(max_digits=10, decimal_places=2)
