from django.db import models
from django.contrib.auth.models import User


class Debtor (models.Model):

    IdDebtor = models.AutoField(auto_created = True,
                          primary_key = True,
                          serialize = False, 
                          verbose_name ='ID')
    name = models.CharField('Nome/Razão Social', max_length=80, blank=True, null=True)
    id_tax = models.CharField('CNPJ/CPF', max_length=20)
    id_espaider = models.CharField('ID Espaider', max_length=10)
    contabil = models.DecimalField('Contábil', max_digits=15, blank=False, decimal_places=2, default='0')
    risco = models.DecimalField('Risco', max_digits=15, blank=False, decimal_places=2, default='0')
    wallet_type = models.CharField(max_length=20, blank=False, default='MASSIFICADO PF',
                                   choices=(('MASSIFICADO PF', 'MASSIFICADO PF'),
                                    ('MASSIFICADO PJ', 'MASSIFICADO PJ'),
                                    ('AUTOS', 'AUTOS'),
                                    ('ALTO TICKET', 'ALTO TICKET'),
                                    ))
    phone_1 = models.CharField('Telefone', max_length=11)
    phone_2 = models.CharField('Telefone', max_length=11)
    phone_hot = models.CharField('Telefone Hot', max_length=11)
    phone_whatsapp = models.CharField('Whatsapp', max_length=11)
    status_negociacao = models.CharField(max_length=20, blank=False, default='NEGOCIAR',
                                         choices=(('NEGOCIAR', 'NEGOCIAR'),
                                             ('POTENCIAL', 'POTENCIAL'),
                                             ('PROPOSTA EM ANÁLISE', 'PROPOSTA EM ANÁLISE'),
                                             ('PROPOSTA APROVADA', 'PROPOSTA APROVADA'),
                                             ('PROPOSTA NEGADA', 'PROPOSTA NEGADA'),
                                             ('PROPOSTA EXPURGADA', 'PROPOSTA EXPURGADA'),
                                             ('PROPOSTA EXPURGA', 'PROPOSTA EXPURGADA'),
                                             ('ACORDO SEM ENTRADA', 'ACORDO SEM ENTRADA'),
                                             ('ACORDO PAGO', 'ACORDO PAGO'),
                                             ('FORMALIZADO', 'FORMALIZADO'),
                                             ('ACORDO EM DIA', 'ACORDO EM DIA'),
                                             ('ACORDO EXTERNO', 'ACORDO EXTERNO'),
                                             ('ACORDO QUITADO', 'ACORDO QUITADO'),
                                             ('DESINDICADO', 'DESINDICADO'),
                                             ('ACORDO ATIVO', 'ACORDO ATIVO'),
                                             ('NÃO ATUAR', 'NÃO ATUAR'),
                                             ))
    user_agent = models.ForeignKey(User, on_delete=models.CASCADE)
    cpc_status = models.CharField(max_length=20, blank=False, default='SIM',
                                   choices=(('SIM', 'SIM'),
                                    ('NÃO', 'NÃO')
                                    ))
    data_registro = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)
    observacoes_status = models.TextField('Observações', max_length=500, blank=True)

    cpc_status = models.CharField(max_length=20, blank=False, default='SIM',
                                   choices=(('SIM', 'SIM'),
                                    ('NÃO', 'NÃO')
                                    ))
    observacoes_status = models.TextField('Observações', max_length=500, blank=True)


    class Employees(models.Model):
        name_employee = models.ForeignKey(User, on_delete=models.CASCADE)
        departament =  models.CharField(max_length=20, blank=False, default='Varejo',
                                   choices=(('Varejo', 'Varejo'),
                                    ('BackOffice', 'BackOffice'),
                                    ('Imobiliário', 'Imobiliário'),
                                    ('Especializado', 'Especializado'),
                                    ('Judicial', 'Judicial'),
                                    ))
        PhotoFilename = models.CharField(max_length=100, blank = False)