from flask_sqlalchemy import SQLAlchemy

from app import db
class Roles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def role_serializer(self):
        return {
            'id': self.id,
            'name': self.name,
        }

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    address = db.Column(db.Text)
    contact = db.Column(db.String(20))
    updated_at = db.Column(db.DateTime, onupdate=db.func.current_timestamp())
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    email = db.Column(db.String(120))

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

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    username = db.Column(db.String(50), unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    contact = db.Column(db.String(20))
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, onupdate=db.func.current_timestamp())

    role = db.relationship('Roles', backref='users')
    client = db.relationship('Client', backref='users')

    def user_serializer(self):
        role_data = self.role.id if self.role else None
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

class UserRole(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

class DataEntity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

class Consignment(db.Model):
    TYPE_CHOICES = [
        ('Type1', 'Type 1'),
        ('Type2', 'Type 2'),
    ]

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    type = db.Column(db.String(20), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    created_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    updated_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, onupdate=db.func.current_timestamp())

    client = db.relationship('Client', backref='consignments')
    created_by = db.relationship('User', foreign_keys=[created_by_id], backref='created_consignments')
    updated_by = db.relationship('User', foreign_keys=[updated_by_id], backref='updated_consignments')

    def con_serializer(self):
        client_id = self.client_id if self.client_id else None
        created_by_id = self.created_by_id if self.created_by_id else None

        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'client_id': client_id,
            'created_by': created_by_id,
            'updated_by': self.updated_by_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    consignment_id = db.Column(db.Integer, db.ForeignKey('consignment.id'))
    barcode = db.Column(db.String(50))
    length = db.Column(db.Float(precision=2))
    volume = db.Column(db.Float(precision=2))

    def log_serializer(self):
        consignment_id = self.consignment_id if self.consignment_id else None
        return {
            'consignment_id': consignment_id,
            'barcode': self.barcode,
            'length': self.length,
            'volume': self.volume
        }

class Logs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    consignment_id = db.Column(db.Integer, db.ForeignKey('consignment.id'))
    barcode = db.Column(db.String(50))
    length = db.Column(db.Float(precision=2))
    volume = db.Column(db.Float(precision=2))


