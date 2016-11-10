from django.conf.urls import include, url
from django.contrib import admin
from marketing.views import HomePage
from subscribers import views
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from accounts.views import AccountList,account_cru
from accounts.urls import account_urls
from django.conf import settings
from django.conf.urls.static import static
from accounts.urls import account_urls
from contacts.urls import contact_urls
from contacts.views import contact_cru
from contacts.views import ContactDelete
from communications.urls import comm_urls
admin.autodiscover()

urlpatterns = [
    # Marketing pages
     url(r'^$', HomePage.as_view(), name="home"),
     url(r'^signup/$',views.subscriber_new, name='sub_new'),
     url(r'^admin/', include(admin.site.urls)),
     url(regex=r'^login/$', view=login, kwargs={'template_name': 'login.html'},name='login'),
     url(regex=r'^logout/$', view=logout, kwargs={'next_page': '/'}, name='logout'),

     url(r'^account/new/$',account_cru, name='account_new'),
     url(r'^account/list/$',AccountList.as_view(), name='account_list'),
     url(r'^account/(?P<uuid>[\w-]+)/', include(account_urls)),
     url(r'^contact/new/$',contact_cru, name='contact_new'),
     url(r'^comm/(?P<uuid>[\w-]+)/', include(comm_urls)),


     url(r'^contact/(?P<uuid>[\w-]+)/', include(contact_urls)),
     url(r'^contact/(?P<pk>[\w-]+)/delete/$',ContactDelete.as_view(), name='contact_delete'),







       # Login/Logout URLs


    # Account related URLs


    # Contact related URLS


    # Communication related URLs


    #url(r'^admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
