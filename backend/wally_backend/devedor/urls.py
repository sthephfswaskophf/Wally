from django.conf.urls import url
from devedor import views

urlpatterns=[
    url(r'^debtor/$',views.debtorAPI),
    url(r'^debtor/$([0-9]+)',views.debtorAPI),
]