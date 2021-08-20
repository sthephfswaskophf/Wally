from django.db.models import fields
from rest_framework import serializers

from devedor.models import Debtor, Employees

class DebtorSerializer(serializers.ModelSerializer):
   class Meta:
       model = Debtor
       fields = (
                'ID',
                'name',
                'id_tax',
                'id_espaider',
                'contabil',
                'risco',
                'wallet_type',
                'phone_1',
                'phone_2',
                'phone_hot',
                'phone_whatsapp',
                'status_negociacao',
                'user_agent',
                'cpc_status',
                'data_registro',
                'data_alteracao',
                'observacoes_status',
                'cpc_status',
                'observacoes_status'
       )

class EmployeesSerializer(serializers.ModelSerializer):
   class Meta:
       model = Employees
       fields = (
                'EmployeeId',
                'name_employee',
                'departament',
                'PhotoFilename'
        )




