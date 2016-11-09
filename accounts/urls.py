from django.conf.urls import  url
from . import views
account_urls = [

    url(r'^$',views.account_detail, name='account_detail'),
    url(r'^edit/$',views.account_cru, name='account_update'    ),

    

]
