from django.db.models import *


# Create your models here.

class cloth(Model):

    price = IntegerField()
    name = CharField(max_length = 100)
    img = ImageField(upload_to = 'pics')
    spo = BooleanField(default = False)