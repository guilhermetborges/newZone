from django import forms
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from .models import Contato , CustomUsuario

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUsuario


class CustomUsuarioCreateForm(UserCreationForm):
    class Meta:
        model = CustomUsuario
        fields = ['email', 'first_name', 'last_name', 'fone', 'password1', 'password2']
        widgets = {
            'username': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Primeiro nome'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sobrenome'}),
            'fone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefone'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data["email"]  # Usa email como username
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class CustomUsuarioChangeForm(UserChangeForm):
    class Meta:
        model = CustomUsuario
        fields = ['first_name', 'last_name' , 'fone']
        

class ContatoForm(forms.ModelForm):

    class Meta:
        model = Contato
        fields = ['nome', 'email', 'assunto', 'mensagem']

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome', 'autocomplete': 'off'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'autocomplete': 'off'}),
            'assunto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Assunto', 'autocomplete': 'off'}),
            'mensagem': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Mensagem', 'rows': '7', 'autocomplete': 'off'}),
        }

    