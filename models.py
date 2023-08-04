from tortoise import fields
from tortoise.models import Model


class Hotels(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    description = fields.TextField()
    stars = fields.IntField()
    minimal_price = fields.FloatField()


class Rooms(Model):
    id = fields.IntField(pk=True)
    hotel = fields.ForeignKeyField(model_name='models.Hotels', related_name='rooms')
    count_of_persons = fields.IntField()
    price = fields.FloatField()


class Clients(Model):
    id = fields.IntField(pk=True)
    room = fields.ForeignKeyField(model_name='models.Rooms', related_name='clients')
    full_name = fields.CharField(max_length=255)
    phone_number = fields.CharField(max_length=20)
    date_start = fields.DateField()
    date_end = fields.DateField()
