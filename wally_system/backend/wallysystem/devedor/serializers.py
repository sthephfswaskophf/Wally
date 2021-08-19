from backend.wallysystem.devedor import models
from rest_framework import serializers
from devedor.models import Debtors, Employees


class DebtorsSerializer(serializers.ModelSerializer):
    class Meta:
        models = Debtors
        fields = (
            'DebtorsID',
            'name',
            'id_tax',
            'id_espaider',
            'contabil',
            'risco',
            'phone_1',
            'risco',
            'phone_2',
            'phone_hot',
            'phone_whatsapp',
            'status_negociacao',
            'user_agent',
            'cpc_status',
            'data_registro',
            'data_alteracao',
            'observacoes_status',
       )

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = (
            'name',
            'departament_type',
            'rating',
            'PhotoFileNAme',

        )