from django.conf.urls import url
from devedor import views

urlpatterns=[
    url(r'^debtor/$',views.debtorAPI),
    url(r'^debtor/$([0-9]+)',views.debtorAPI),
    url(r'^employee/$',views.employeeAPI),
    url(r'^employee/$([0-9]+)',views.employeeAPI),
]
