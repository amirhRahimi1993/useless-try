from django.http import HttpResponse , HttpResponseRedirect
from .models import Dr_info , collector , Hash_capcha , specialiy , Iran_city
from django.template import loader
from .add_specialty import adder
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from .Create_million_user import create_Collector , Generator
from .Generate_capch import GeneratorCapcha
from .Generate_city import city_Adder
import random
#####TEST VIEW #######
from django.shortcuts import render
from django.views import View
from .form import Dr_form , FileUploadForm
from django.views.decorators.csrf import csrf_exempt
from .Generate_city import city_Adder


######################



Expire_Time =300 #set Expire time
username = ""
password = ""
previous_scrol_content = 0;

class Basic_Opreatoin:
    def Verify_image(self, FILES):
        Answer = False
        Size_thershold = 1 * 1000 * 1000
        acceptable_format = ["jpg" , "jpeg" , "png" , "gif" , "bmp" , "tiff" ]
        img_size = FILES._size
        img_name = FILES._name.split('.')
        if img_size >= Size_thershold:
            return False
        for s in acceptable_format:
            if s == img_name[len(img_name)-1].lower():
                Answer = True
                break
        return Answer


def By_Adder_Doctor_detail(request , collector_id):
    request.session.set_expiry(Expire_Time)

    filters = ""
    try:
        for i in range(len(Dr_info.objects.filter(adder=collector_id))):
            filters = filters + Dr_info.objects.filter(adder=collector_id)[i].Dr_name + " " + Dr_info.objects.filter(adder=collector_id)[i].Dr_family + "<br/>"
    except:
        return HttpResponse("WOW it seems your data dosent avalable")
    return HttpResponse (filters)

def USer_adder(request , collector_id):
    request.session.set_expiry(Expire_Time)
    try:
        X = collector.objects.get(pk=collector_id)
        return HttpResponse(X.name + " " + X.family)
    except:
        return HttpResponse("Collector does not EXIST")

def index(request):
    if len(collector.objects.all()) == 0 :
        a = create_Collector()
    if len(Dr_info.objects.all()) == 0 :
        generate = Generator(30)
        generate.main()
    if len(Hash_capcha.objects.all()) == 0:
        x = GeneratorCapcha(CREATE_IMAGE=False)
        x.main()
    if len(specialiy.objects.all()) == 0:
        z = adder()
    if len(Iran_city.objects.all()) == 0:
        x = city_Adder()
    return HttpResponse("xxxx")

class Login_user(View):
    def get(self, request):
        # request.session.set_expiry(Expire_Time)
        template = loader.get_template('Super_user/login.html')
        context = {
            'sth': 1,
        }
        return HttpResponse(template.render(context, request))
    def post(self , request):
        password = request.POST.get('txt_password', None)
        username = request.POST.get('txt_username', None)
        request.session.set_expiry(Expire_Time)
        try:
            if collector.objects.get(Email=username).password == password:
                template = loader.get_template('Super_user/Addinfo.html')
                request.session["username"] = username
                request.session["password"] = password
                data = {
                    'is_taken': 'Home',
                    'is_correct': 'True'
                }
            else:
                data = {
                    'is_taken': 'your user name our password is wrong',
                    'is_correct': 'False'
                }

        except:
            data = {
                'is_taken': 'Ur user name our password is wrong',
                'is_correct': 'False'
            }
        return JsonResponse(data)
class Super_Usr_Home(View):
    @csrf_exempt
    def get(self , request):
        request.session.set_expiry(Expire_Time)
        Email = request.session["username"]
        Password = request.session["password"]
        rand = random.randint(9001,9998)
        Hash_value = Hash_capcha.objects.get(Number=rand).Hash_value
        Num_path = Hash_capcha.objects.get(Number=rand).Number_name
        try:
            collectors = collector.objects.get(Email=Email , password=Password)
        except:
            return HttpResponse("WRONG")
        template = loader.get_template('Super_user/Addinfo.html')
        speciality_list = []
        for x in specialiy.objects.all():
            speciality_list.append(x.specialiy_name)
        city_list = []
        for city in Iran_city.objects.all():
            city_list.append(city.city_name)
        context ={
            'Email': Email,
            'name': collectors.name,
            'family': collector.family,
            'HASH_VALUE' : Hash_value,
            'img_path' : Num_path,
            'spec': sorted(speciality_list),
            'city_list' : city_list,
            'id' : 1,
        }
        return HttpResponse(template.render(context, request))
    #@csrf_exempt
    def post(self , request):
        request.session.set_expiry(Expire_Time)
        List = list(request.POST.keys())
        image_verfication = Basic_Opreatoin()
        ids = []

        if len(request.FILES) == 0:
            data={
                'is_taken': 'تصویر بارگذاری نشد لطفا دوباره تلاش کنید',
                'is_correct': 'False'
            }
            return JsonResponse(data)
        if len(request.FILES) > 1:
            data = {
                'is_taken': 'بیش از یک تصویر نمی تواند بارگذاری شود، لطفا دوباره تلاش کنید',
                'is_correct': 'False'
            }
            return JsonResponse(data)
        verify = image_verfication.Verify_image(request.FILES[list(request.FILES.keys())[0]])
        if verify == False:
            data = {
                'is_taken': 'سایز تصویر شما بایستی کمتر از ۱ مگابایت باشد همچنین پسوند تصویر قابل قبول jpg bmp jpeg tiff png gif میباشد',
                'is_correct': 'False'
            }
        else:
            Hash_capch = request.POST.get('HASH', None)
            number = request.POST.get('capcha_number', None)
            if Hash_capcha.objects.get(Hash_value=Hash_capch).Number != number:
                data = {
                    'is_taken': 'کد امنیتی اشتباه می باشد لطفا دوباره تلاش کنید',
                    'is_correct': 'False'
                }
                return JsonResponse(data)

            name = request.POST.get('txt_name', None)
            family = request.POST.get('txt_family', None)
            location = request.POST.get('txt_gmap', None)
            address = request.POST.get('txt_Address', None)
            ph_link = ''
            tel = request.POST.get('txt_tel', None)
            mbl = request.POST.get('txt_mobile', None)
            spl = request.POST.get('txt_specialty', None)
            adder_email = request.POST.get('adder_email', None)
            if len(mbl) != 11:
                data = {
                    'is_taken': 'شماره موبایل بایستی ۱۱ رقم باشد',
                    'is_correct': 'False'
                }
                return JsonResponse(data)
            try:
                tel_phone = int(tel)
                mobile = int(mbl)
            except:
                data = {
                    'is_taken': 'شماره بایستی شامل شامل عدد باشد',
                    'is_correct': 'False'
                }
                return JsonResponse(data)
            try:
                myfile = request.FILES['Dr_Pic_Upload']
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                uploaded_file_url = fs.url(filename)
                col = collector.objects.get(Email=adder_email)
                Answer = Dr_info(Dr_name=name, Dr_family=family, Dr_google_map_link=location, Dr_Address=address,Dr_photo_link=uploaded_file_url, Dr_telephone=tel, Dr_mobile=mbl, Dr_specialty=spl, adder=col)
                Answer.save()
                data = {
                    'is_taken': 'ثبت اطلاعات با موفقیت انجام شد',
                    'is_correct': 'True'
                }
            except:
                data = {
                    'is_taken': 'خطایی رخ داده',
                    'is_correct': 'False'
                }
        return JsonResponse(data)
class Report_activity(View):
    @csrf_exempt
    def get(self , request , id):
        request.session.set_expiry(Expire_Time)
        filters = []
        Empty_image = []
        ########itreate 30
        iterated =10
        ###################
        template = loader.get_template("Super_user/Doctor_Template.html")
        collector_id = collector.objects.get(Email=request.session["username"]).id
        scrol_number = request.GET.get('scroll')
        DB_user = Dr_info.objects.filter(adder=collector_id)
        counter = []
        href = []
        for i in range(id , iterated + id):
            if i >= DB_user.count():
                break;
            filters.append(DB_user[i])
            if '/media/' not in DB_user[i].Dr_photo_link:
                Empty_image.append(True)
            else:
                Empty_image.append(False)
        page = int((DB_user.count()/30) + 2)
        for i in range(1,page):
            href.append("~/Login/Home/Dashboard/" + str(i))
        context = {
            'filters': filters,
            'Empty_image': Empty_image,
            'page_numbers' : range(page),
            'id' : id,
            'Size' : range(len(filters))
        }
        return HttpResponse(template.render(context , request))

    @csrf_exempt
    def post(self , request , id):
        request.session.set_expiry(Expire_Time)
        name = request.POST.get('txt_name', None)
        family = request.POST.get('txt_family', None)
        location = request.POST.get('txt_gmap', None)
        address = request.POST.get('txt_address', None)
        # ph_link = request.GET.get('dr', None)
        tel = request.POST.get('txt_tel', None)
        mbl = request.POST.get('txt_mbl', None)
        spl = request.POST.get('txt_special', None)
        adder_email = request.session['username']
        id = request.POST.get('txt_id', None)
        obj = Dr_info.objects.get(id=id)
        try:
            if not obj.adder.Email == request.session["username"]:
                data = {
                    'is_taken': 'خطایی رخ داده',
                    'is_correct': 'False'
                }
            else:
                obj.Dr_name = name
                obj.Dr_family = family
                obj.Dr_google_map_link = location
                obj.Dr_Address = address
                obj.Dr_telephone = tel
                obj.Dr_mobile = mbl
                obj.Dr_specialty = spl
                number = int(mbl)
                x = int(tel)
                if len(mbl) == 11:
                    data = {
                        'is_taken': 'عملیات به روزرسانی با موفقیت انجام شد',
                        'is_correct': 'True'
                    }
                    obj.save()
                else:
                    data = {
                        'is_taken': 'طول شماره تلفن بایستی شامل ۱۱ رقم باشد',
                        'is_correct': 'False'
                    }
        except:
            data = {
                'is_taken': 'خطا رخ داده',
                'is_correct': 'False'
            }
        return JsonResponse(data)


def AdvanceSearch(request):
    request.session.set_expiry(Expire_Time)
    filters = []
    template = loader.get_template("Super_user/AdvanceSearch.html")
    collector_id = collector.objects.get(Email=request.session["username"]).id
    filters = Dr_info.objects.filter(adder=collector_id)
    context = {
        'filters': filters
    }
    return HttpResponse(template.render(context , request))
def result(request):
    request.session.set_expiry(Expire_Time)
    template = loader.get_template("Super_user/result.html")
    search_items = []
    item = []
    if request.method == "POST":

        adder_email = request.session["username"]
        Emails =[]

        item.extend(["Dr_name", request.POST["txt_name"]]) if request.POST["txt_name"] != "" else item
        item.extend(["Dr_family", request.POST["txt_family"]]) if request.POST["txt_family"] != "" else item

        item.extend(["Dr_specialty", request.POST["txt_specialty"]]) if request.POST["txt_specialty"] != "" else item
        item.extend(["Dr_telephone", request.POST["txt_tel"]]) if request.POST["txt_tel"] != "" else item

        item.extend(["Dr_mobile", request.POST["txt_mobile"]]) if request.POST["txt_mobile"] != "" else item

        item.extend(["Dr_google_map_link", request.POST["txt_gmap"]]) if request.POST["txt_gmap"] != "" else item
        item.extend(["Dr_Address", request.POST["txt_Address"]]) if request.POST["txt_Address"] != "" else item
        dr=[]
        Search_Query = {}
        for i in range(0,len(item)-1,2):
            if not item[i+1] == "":
                Search_Query[item[i]] = item[i+1]
                i= i+1
        for i in range(30):
            try:
                dr.append(Dr_info.objects.filter(**Search_Query)[i])
            except:
                break
        if len(dr) != 0 :
            context = {
                'filters' : dr,
                'empty' : 'False',
                'viewer_email' : adder_email,
            }
        else:
            context = {
                'filters': 'متاسفانه درخواست شما نتیجه ای در بر نداشت',
                'empty' : 'True'
            }
    return  HttpResponse(template.render(context,request))
def Logout(request):
    request.session.flush()
    template = loader.get_template("Super_user/Logout.html")
    context = {}
    return HttpResponse(template.render(context,request))

######TEST########
class BasicUploadView(View):
    def get(self, request):
        photos_list = Dr_info.objects.all()
        template = loader.get_template("Super_user/Test.html")
        context = {}
        return HttpResponse(template.render(context , request))

    def post(self, request):
        if request.method == 'POST':
            form = FileUploadForm(data=request.POST, files=request.FILES)
            myfile = request.FILES['FILE']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            if form.is_valid():
                print('valid form')
            else:
                print('invalid form')
                print(form.errors)
        return HttpResponseRedirect('/ingest/')

###########Ajax#################################
@csrf_exempt
def insert_Dr_By_adder( request):
    request.session.set_expiry(Expire_Time)
    Hash_capch = request.GET.get('Hash_Value' , None)
    number =  request.GET.get('cap_number' , None)
    if Hash_capcha.objects.get(Hash_value=Hash_capcha).Number != number:
        data = {
            'is_taken': 'کد امنیتی اشتباه می باشد لطفا دوباره تلاش کنید',
            'is_correct': 'False'
        }
        return JsonResponse(data)

    name = request.GET.get('name' , None)
    family = request.GET.get('family' , None)
    location = request.GET.get('location' , None)
    address = request.GET.get('address' , None)
    ph_link = ''
    tel = request.GET.get('tel' , None)
    mbl = request.GET.get('mbl' , None)
    spl = request.GET.get('spl' , None)
    adder_email = request.GET.get('adder_email' , None)
    if len(mbl) != 11:
        data = {
            'is_taken': 'شماره موبایل بایستی ۱۱ رقم باشد',
            'is_correct': 'False'
        }
        return JsonResponse(data)
    try:
        tel_phone = int(mbl)
        mobile = int(spl)
    except:
        data = {
            'is_taken': 'شماره بایستی شامل شامل عدد باشد',
            'is_correct': 'False'
        }
        return JsonResponse(data)
    try:
        col = collector.objects.get(Email=adder_email)
        Answer = Dr_info(Dr_name=name , Dr_family=family , Dr_google_map_link= location , Dr_Address=address , Dr_photo_link=ph_link , Dr_telephone=tel , Dr_mobile=mbl, Dr_specialty=spl , adder=col)
        Answer.save()
        data = {
            'is_taken': 'ثبت اطلاعات با موفقیت انجام شد',
            'is_correct': 'True'
        }
    except:
        data = {
            'is_taken': 'خطایی رخ داده',
            'is_correct': 'False'
        }
    return JsonResponse(data)
@csrf_exempt
def Update_dr(request):
    request.session.set_expiry(Expire_Time)
    name = request.GET.get('txt_name', None)
    family = request.GET.get('txt_family', None)
    location = request.GET.get('txt_gmap', None)
    address = request.GET.get('txt_address', None)
    #ph_link = request.GET.get('dr', None)
    tel = request.GET.get('txt_tel', None)
    mbl = request.GET.get('txt_mbl', None)
    spl = request.GET.get('txt_special', None)
    adder_email = request.session['username']
    id = request.GET.get('txt_id', None)
    obj = Dr_info.objects.get(id=id)
    try:
        if not obj.adder.Email == request.session["username"]:
            data = {
                'is_taken': 'خطایی رخ داده',
                'is_correct': 'False'
            }
        else :
            obj.Dr_name = name
            obj.Dr_family = family
            obj.Dr_google_map_link = location
            obj.Dr_Address = address
            obj.Dr_telephone = tel
            obj.Dr_mobile = mbl
            obj.Dr_specialty = spl
            number = int(mbl)
            x = int(tel)
            if len(mbl) == 11:
                data = {
                    'is_taken': 'عملیات به روزرسانی با موفقیت انجام شد',
                    'is_correct': 'True'
                }
                obj.save()
            else :
                data = {
                    'is_taken': 'طول شماره تلفن بایستی شامل ۱۱ رقم باشد',
                    'is_correct': 'False'
                }
    except:
        data = {
            'is_taken': 'خطا رخ داده',
            'is_correct': 'False'
        }
    return JsonResponse(data)
##############################################################