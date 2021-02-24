from django.db import models

# Create your models here.

class Idc(models.Model):
    name = models.CharField("RoomName", max_length=32)
    address = models.CharField("RoomAddr", max_length=256)
    phone = models.CharField("Connector", max_length=15)
    email = models.EmailField("EmailAddr", default="null")


    def __str__(self):
        return self.name


    class Meta:
        db_table = "resources_idc"
