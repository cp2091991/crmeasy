from django.conf.urls import url
from . import views
contact_urls = [

    url(r'^$', views.contact_detail, name="contact_detail"),
    url(r'^edit/$',views.contact_cru, name='contact_update'),


]
