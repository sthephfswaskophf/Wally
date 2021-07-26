from django.contrib import admin
from devedor.models import Devedor

class DevedorAdmin(admin.ModelAdmin):
    list_display =('name', 'id_tax', 'id_espaider', 'contabil', 'risco', 'wallet_type', 'status_negociacao', 'user_agent', 'cpc_status' )


admin.site.register(Devedor, DevedorAdmin)