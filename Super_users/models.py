from django.db import models

# Create your models here.
class collector (models.Model):
    photo_user = models.CharField(max_length=700)
    name = models.CharField(max_length=250)
    family = models.CharField(max_length=250)
    Email = models.CharField(max_length=250 , null=False ,unique=True, default="Unset")
    password = models.CharField(max_length=250)
    telephone = models.CharField(max_length=50)
    def __str__(self):
        return self.name + " " + self.family
class Dr_info (models.Model):
    Dr_name = models.CharField(max_length=250 , null=False)
    Dr_family = models.CharField(max_length=250 , null=False)
    adder = models.ForeignKey(collector, on_delete=models.CASCADE , null=False)
    Dr_telephone = models.CharField(max_length=11 , null=False , default="-1")
    Dr_mobile = models.CharField(max_length=13 , null=False , default="-1")
    Dr_google_map_link = models.CharField(max_length=700 , default="-1")
    Dr_Address = models.CharField(max_length=700 , null=False)
    Dr_photo_link = models.CharField(max_length=1000 , default="/media/People-Doctor-Male-icon.png")
    Dr_specialty = models.CharField(max_length=50 ,null=False ,  default="General")

    # def __str__(self):
    #     return self.Dr_name + " " + self.Dr_family
    #
    # def __iter__(self):
    #     for field_name in self._meta.get_all_field_names():
    #         value = getattr(self, field_name, None)
    #         yield (field_name, value)

class Hash_capcha(models.Model):
    Hash_value = models.CharField(max_length=1000 , unique=True , default="-1")
    Number = models.CharField(max_length=13 , unique=True , default="-1")
    Number_name = models.CharField(max_length=20 , unique=True , default="-1")
class Document(models.Model):
    path = models.CharField(max_length=500)
    document = models.FileField()
class specialiy(models.Model):
    specialiy_name = models.CharField(max_length=50 , unique=True)
class Iran_city(models.Model):
    city_name = models.CharField(max_length=100 , unique=True)
