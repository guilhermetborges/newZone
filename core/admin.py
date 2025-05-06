from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Servico
from .models import Contato , CustomUsuario , Pais , Cidade
from .forms import CustomUsuarioCreateForm , CustomUsuarioChangeForm

 


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'descricao', 'icone', 'criado', 'modificado', 'ativo')


@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'assunto', 'mensagem', 'criado', 'modificado', 'ativo')


@admin.register(CustomUsuario)
class CustomUsuarioAdmin(UserAdmin):
    add_form = CustomUsuarioCreateForm
    form = CustomUsuarioChangeForm
    model = CustomUsuario
    list_display = ['first_name','last_name','email','fone','is_staff']
    fieldsets =  (
        (None, { 'fields': ('email', 'password')}),
        ('informações pessoais' , {'fields': ('is_active','is_staff', 'is_superuser', 'groups','user_permissions')}),
        ('datas importantes' , {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'fone', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )


@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("nome",)}
    list_display = ('nome', 'descricao', 'criado', 'modificado', 'ativo')

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ('nome' , 'populacao' , 'idh' ,'pais', 'descricao')