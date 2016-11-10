from django.conf.urls import  url

comm_urls = [

    url(r'^$',
        'crmapp.communications.views.comm_detail', name="comm_detail"


]
