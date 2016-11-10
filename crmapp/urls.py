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
from communications.views import comm_cru
from contacts.views import ContactDelete
from communications.urls import comm_urls
admin.autodiscover()

urlpatterns = [
    # Marketing pages
     url(r'^$', HomePage.as_view(), name="home"),
     url(r'^signup/$',views.subscriber_new, name='sub_new'),
     url(r'^admin/', include(admin.site.urls)),
      # Login/Logout URLs
     url(regex=r'^login/$', view=login, kwargs={'template_name': 'login.html'},name='login'),
     url(regex=r'^logout/$', view=logout, kwargs={'next_page': '/'}, name='logout'),
     # Account related URLs
     url(r'^account/new/$',account_cru, name='account_new'),
     url(r'^account/list/$',AccountList.as_view(), name='account_list'),
     url(r'^account/(?P<uuid>[\w-]+)/', include(account_urls)),
     # Contact related URLS
     url(r'^contact/new/$',contact_cru, name='contact_new'),
     url(r'^contact/(?P<uuid>[\w-]+)/', include(contact_urls)),
     url(r'^contact/(?P<pk>[\w-]+)/delete/$',ContactDelete.as_view(), name='contact_delete'),
     # Communication related URLs
     url(r'^comm/new/$',comm_cru, name='comm_new'),
     url(r'^comm/(?P<uuid>[\w-]+)/', include(comm_urls)),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
