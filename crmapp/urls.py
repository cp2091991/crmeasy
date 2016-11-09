"""crmapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
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
admin.autodiscover()

urlpatterns = [
    # Marketing pages
     url(r'^$', HomePage.as_view(), name="home"),
     url(r'^signup/$',views.subscriber_new, name='sub_new'),
     url(r'^admin/', include(admin.site.urls)),
     url(regex=r'^login/$', view=login, kwargs={'template_name': 'login.html'},name='login'),
     url(regex=r'^logout/$', view=logout, kwargs={'next_page': '/'}, name='logout'),
     url(r'^account/list/$',AccountList.as_view(), name='account_list'),
     url(r'^account/(?P<uuid>[\w-]+)/', include(account_urls)),
     url(r'^account/new/$',account_cru, name='account_new'),




       # Login/Logout URLs


    # Account related URLs


    # Contact related URLS


    # Communication related URLs


    #url(r'^admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
