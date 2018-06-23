from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'Super_users'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('<int:collector_id>/', views.USer_adder, name='USer_adder'),
    path('<int:collector_id>/current_activity', views.By_Adder_Doctor_detail, name='By_Adder_Doctor_detail'),
    path('Login/', views.Login_user.as_view(), name='Login'),
    path('Logout/', views.Logout, name='Logout'),
    path ('Login/Home/' , views.Super_Usr_Home.as_view(), name='Super_Usr_Home' ),
    path ('Login/Home/Dashboard/<int:id>/' , views.Report_activity.as_view(), name='Report_activity'),
    url(r'^Login/Home/ajax/insert_Dr_By_adder/$', views.insert_Dr_By_adder, name='insert_Dr_By_adder'),
    url(r'^ajax/Update_dr/$', views.Update_dr, name='Update_dr'),
    url('Login/Home/AdvanceSearch' , views.AdvanceSearch, name='AdvanceSearch'),
    url('Login/Home/result' , views.result, name='result'),
    ######BOTH TEST ######
    url(r'^basic-upload/$', views.BasicUploadView.as_view(), name='basic_upload'),
    #url(r'ajax/basic_upload/$', views.BasicUploadView_ajax, name='BasicUploadView_ajax')
    # url(r'^login_user/$', views.login_user, name='login_user'),
    # url(r'^add_new_Doctor/$', views.add_new_Doctor, name='add_new_Doctor'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)