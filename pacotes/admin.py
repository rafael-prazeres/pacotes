# -*- coding: utf-8 -*-
from django.contrib import admin
#from datetime import timedelta, datetime
#from django import forms


# Register your models here.

from .models import Pessoa, TipoDePacote, Pacote, RemadorAutorizado, RequiredInlineFormSet, ConsumoDePacote

#admin.site.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
	fieldsets = [
		(
			'Informações Pessoais',
			{'fields': ['nome',
				'telefone',
				'email','sexo','data_nascimento','tipo_sanguineo']}),
	]
	#fields = ['nome','telefone','email','sexo','data_nascimento','tipo_sanguineo']
	list_display = ('id','nome','telefone','email','sexo','data_nascimento','tipo_sanguineo')
	search_fields = ['nome']

admin.site.register(Pessoa, PessoaAdmin)

class TipoDePacoteAdmin(admin.ModelAdmin):
	fieldsets = [
		(
			'Informações do Tipo de Pacote',
			{'fields':['nome',
				'duracao_min','prazo_de_validade','venda_autorizada']}),
	]
	list_display = ('id','nome','duracao_min','prazo_de_validade','venda_autorizada')
	search_fields = ['nome']

admin.site.register(TipoDePacote, TipoDePacoteAdmin)

class RemadorAutorizadoInline(admin.TabularInline):
	model = RemadorAutorizado
	#extra = 1
	formset = RequiredInlineFormSet
	verbose_name = "Remador Autorizado"
	verbose_name_plural = "Remadores Autorizados"

class ConsumoDePacoteInline(admin.StackedInline):
        model = ConsumoDePacote
        extra = 0
        #formset = RequiredInlineFormSet


class PacoteAdmin(admin.ModelAdmin):
	fieldsets = [
		('Informações do Pacote',{'fields': ['tipo_de_pacote','responsavel_financeiro','observacoes']}),
	]
        #inlines = [RemadorAutorizadoInline,ConsumoDePacoteInline]
        inlines = [RemadorAutorizadoInline]
	list_display = ('id','responsavel_financeiro','data_de_venda','tipo_de_pacote','remadores','consultar_saldo')
	#list_display = ('id','data_de_compra','tipo_de_pacote','remadores')
	#search_fields = ['remadores_autorizados']
        search_fields = ['responsavel_financeiro__nome']
	#exclude = ('consumo_permitido',)

admin.site.register(Pacote, PacoteAdmin)


#class ConsumoDePacoteAdminForm(forms.ModelForm):
#    def __init__(self, *args, **kwargs):
#        super(ConsumoDePacoteAdminForm, self).__init__(*args, **kwargs)
#        # access object through self.instance...
#        self.fields['pacote_consumido'].queryset = Pacote.objects.filter(self.instance.pacote_consumido.data_de_venda >= (datetime.date.today() - timedelta(months=12)))



class ConsumoDePacoteAdmin(admin.ModelAdmin):
#	form = ConsumoDePacoteAdminForm
        fieldsets = [
                (
			'Informações do Consumo',
			{'fields': ['pacote_consumido',
				'remador_autorizado',
				'data_e_hora_da_remada',
				'tempo_de_duracao_da_remada',
				'numero_de_pranchas_utilizadas','nota_sobre_consumo']}),
        ]
        #inlines = [RemadorAutorizadoInline,ConsumoDePacoteInline]
        list_display = 	(
		'id','pacote_consumido',
		'remador_autorizado',
		#'validar_consumo',
		'data_e_hora_da_remada',
		'total_consumido',
		'tempo_de_duracao_da_remada',
		#'numero_de_pranchas_utilizadas'
	)
        #list_display = ('id','data_de_compra','tipo_de_pacote','remadores')
        #search_fields = ['remadores_autorizados']
        #search_fields = ['remador_autorizado__pessoa__nome']
	search_fields = ['pacote_consumido__responsavel_financeiro__nome']

#	def get_form(self, request, obj=None, **kwargs):
#		form = super(ConsumoDePacote, self).get_form(request, obj, **kwargs)
#		form.base_fields['pacote_consumido'].queryset = Pacote.objects.filter()
#		return form


admin.site.register(ConsumoDePacote, ConsumoDePacoteAdmin)
