"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from firstapp import views

from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^izotoprk/$', views.izotoprk, name='izotoprk'),
    url(r'^$', views.home, name='home'),
    url(r'^izotoprk/company/(?P<company_id>\d+)/$', views.izotoprk_companys_detail, name='izotoprk-companys-detail'),
    url(r'^izotoprk/company/(?P<company_id>\d+)/delete/$', views.izotoprk_companys_delete, name='izotoprk-companys-delete'),
    url(r'^izotoprk/company/(?P<company_id>\d+)/edit/$', views.izotoprk_companys_edit, name='izotoprk-companys-edit'),

    url(r'^izotoprk/company_contact/(?P<contact_id>\d+)/edit/$', views.izotoprk_contact_edit, name='izotoprk-contact-edit'),
    url(r'^izotoprk/company_contact_work/(?P<contact_work_id>\d+)/edit/$', views.izotoprk_contact_work_edit, name='izotoprk-contact-work-edit'),

    url(r'^izotoprk/company/object/(?P<object_id>\d+)/$', views.izotoprk_object_detail, name='izotoprk-object-detail'),
    url(r'^izotoprk/company/object/(?P<object_id>\d+)/edit/$', views.izotoprk_object_edit, name='izotoprk-object-edit'),
   
    url(r'^izotoprk/company/object/work/(?P<work_id>\d+)/$', views.izotoprk_work, name='izotoprk-work'),
    url(r'^izotoprk/company/object/work/(?P<work_id>\d+)/edit/$', views.izotoprk_work_edit, name='izotoprk-work-edit'),
    url(r'^izotoprk/company/object/work/(?P<work_id>\d+)/status/$', views.izotoprk_work_status, name='izotoprk-work-status'),
    
    url(r'^izotoprk/sign_in/$', auth_views.login,
        {'template_name': 'izotoprk/sign_in.html'},
        name='izotoprk-sign-in'),

    url(r'^izotoprk/sign_out/$', auth_views.logout,
        {'next_page': '/'},
        name='izotoprk-sign-out'),

    url(r'^izotoprk/account/$', views.izotoprk_account, name='izotoprk-account'),
    url(r'^izotoprk/companys/$', views.izotoprk_companys, name='izotoprk-companys'),
    url(r'^izotoprk/companys_objects/$', views.izotoprk_companys_objects, name='izotoprk-companys-objects'),
    url(r'^izotoprk/in_work/$', views.izotoprk_in_work, name='izotoprk-in-work'),
    url(r'^izotoprk/on_payment/$', views.izotoprk_on_payment, name='izotoprk-on-payment'),
    url(r'^izotoprk/co_workers/$', views.izotoprk_co_workers, name='izotoprk-co-workers'),
    url(r'^izotoprk/documents/$', views.izotoprk_documents, name='izotoprk-documents'),
    url(r'^izotoprk/documents/(?P<doc_id>\d+)/delete/$', views.izotoprk_document_delete, name='izotoprk-document-delete'),
    url(r'^izotoprk/co_workers/worker/(?P<worker_id>\d+)/$', views.izotoprk_worker, name='izotoprk-worker'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
