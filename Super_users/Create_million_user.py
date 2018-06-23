from Super_users.models import Dr_info , collector
import string
import random
class create_Collector:
    # photo_user = models.CharField(max_length=700)
    # name = models.CharField(max_length=250)
    # family = models.CharField(max_length=250)
    # Email = models.CharField(max_length=250, null=False, unique=True, default="Unset")
    # password = models.CharField(max_length=250)
    # telephone = models.CharField(max_length=50)
    def __init__(self):
        fake_email = ["a.h.rahimi1993@gmail.com" , "YnsRezaie@gmail.com" , "Ehsan_Ghafari@gmail.com" , "test_adder@gmail.com"]
        name = ["Amirhosein" , "Yoones" , "Ehsan" , "test"]
        family = ["Rahimi" , "Rzn" , "Ghafari" , "adder"]
        for f in range(len(fake_email)):
            a = collector(photo_user="" , name=name[f] , family=family[f] , Email=fake_email[f], password="12345", telephone="23444444")
            a.save()
class Generator:

    def __init__(self,size):
        self.size = size
    def main(self):
        # Dr_name = models.CharField(max_length=250, null=False)
        # Dr_family = models.CharField(max_length=250, null=False)
        # adder = models.ForeignKey(collector, on_delete=models.CASCADE, null=False)
        # Dr_telephone = models.CharField(max_length=11, null=False, default="-1")
        # Dr_mobile = models.CharField(max_length=13, null=False, default="-1")
        # Dr_google_map_link = models.CharField(max_length=700, default="-1")
        # Dr_Address = models.CharField(max_length=700, null=False)
        # Dr_photo_link = models.FileField()
        # Dr_specialty = models.CharField(max_length=50, null=False, default="General")
        speciality = ['آسیب شناسی','آلرژی','آندرولژی','ارتوپدی','اورژانس','اورولوژی','ایمنی شناسی','بهداشت در سکس','بهداشت عمومی','بیماری شناسی','گوارش','عفونی','بیهوشی','جراحی عمومی','زنان','پلاستیک','چشم','گوش حلق بینی','پرتوشناسی',' مغز و اعصاب','جراح مغز و اعصاب','اطفال', 'قلب داخلی','جراح قلب']
        pishvand = ['0933' , '0915' , '0912' , '0914' , '0914', '0916' , '0917' , '0918' , '0935' , '0901', '0936' , '0937']
        city_pishvand = ['021' , '051' ,'041' , '044' ,'045' ,'31','26']
        fake_email = ["a.h.rahimi1993@gmail.com", "YnsRezaie@gmail.com", "Ehsan_Ghafari@gmail.com","test_adder@gmail.com"]
        for i in range(self.size):
            A = Dr_info(Dr_name=''.join(random.choice(string.ascii_lowercase) for _ in range(10)) , Dr_family=''.join(random.choice(string.ascii_lowercase) for _ in range(10)), adder=collector.objects.get(Email=fake_email[random.randint(0,len(fake_email)-1)]) , Dr_specialty=speciality[random.randint(0,len(speciality)-1)] , Dr_mobile= pishvand[random.randint(0,len(pishvand)-1)] + str(random.randint(1000000 , 9999999)) , Dr_Address=''.join(random.choice(string.ascii_lowercase) for _ in range(20)), Dr_telephone= city_pishvand[random.randint(0 , len(city_pishvand)-1)] + str(random.randint(1000000 , 9999999)), Dr_google_map_link= ''.join(random.choice(string.ascii_lowercase) for _ in range(30)))
            A.save()
