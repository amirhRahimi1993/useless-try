import cv2
import hashlib
from .models import Hash_capcha
import random
class GeneratorCapcha:
    def __init__(self, CREATE_IMAGE=False):
        self.CREATE_IMAGE = CREATE_IMAGE
    def main(self):
        ####Create Capcha
        A = "1234567890"
        Algo = "ALGODRILL@)!*"
        capcha_value = ""
        for i in range(9000,10000):
            capcha_value = ""
            capcha_value = str(i)
            capcha_name = ""
            JPG_name = ""
            name = ""
            while True:
                name = random.randint(1000000 , 100000000000)
                try :
                    JPG_name = Hash_capcha.objects.get(Number_name= str(name))
                except:
                    break
            m = hashlib.md5()
            m.update((capcha_value + Algo).encode('utf-8'))
            digest_capcha = m.digest()
            if self.CREATE_IMAGE:
                I = cv2.imread("/Users/amirhosseinrahimi/Documents/Django_projects/DR_info/static/Super_users/Picture/capcha/capcha_background.jpg")
                font = cv2.FONT_HERSHEY_SIMPLEX
                I = cv2.putText(I, capcha_value, (100, 100), font, 2, (190, 50, 50), 2, cv2.LINE_AA)
            cv2.imwrite("/Users/amirhosseinrahimi/Documents/Django_projects/DR_info/static/Super_users/Picture/capcha_create/"+str(name)+".jpg", I)
            try:
                x= Hash_capcha(Hash_value=digest_capcha, Number=capcha_value , Number_name=str(name) + ".jpg")
                x.save()
            except:
                continue
    if __name__ == '__main__':
        main()
        ##############