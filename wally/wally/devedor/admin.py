from django.contrib import admin
from devedor.models import Devedor

class DevedorAdmin(admin.ModelAdmin):
    list_display =('name', 'id_tax', 'id_espaider', 'contabil', 'risco', 'wallet_type', 'status_negociacao', 'user_agent',)
    list_filter =('user_agent', 'status_negociacao')

admin.site.register(Devedor, DevedorAdmin)