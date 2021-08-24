from django.conf.urls import url
from devedor import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^debtor/$',views.debtorAPI),
    url(r'^debtor/$([0-9]+)',views.debtorAPI),
    url(r'^employee/$',views.employeeApi),
    url(r'^employee/([0-9]+)',views.employeeApi),

    url(r'^SaveFile$',views.SaveFile),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)