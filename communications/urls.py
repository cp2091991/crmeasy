from django.conf.urls import  url
from . import views
comm_urls = [

    url(r'^$',views.comm_detail, name="comm_detail"),
    url(r'^edit/$',views.comm_cru, name='comm_update'),




]
