from django.views.generic.edit import FormView , CreateView
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView , ListView
from .forms import ContatoForm , CustomUsuarioCreateForm
from .models import Servico ,CustomUsuario , Pais , Cidade
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.shortcuts import redirect, render , get_object_or_404

class IndexViews(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()  # Salva o contato no banco
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao enviar a mensagem.')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(IndexViews, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()

        return context
    
class UserRegisterView(CreateView):
    model = CustomUsuario
    form_class = CustomUsuarioCreateForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class CustomLogoutView(View):
    def post(self,request):
        logout(request)
        return render(request, 'logout.html')
    
    def get(sekf, request):
        return redirect('index')
    
class ListaPaisView(ListView):
    model = Pais
    template_name = 'paises/listar_paises.html'
    context_object_name = 'paises'



class PaisView(DetailView):
    model = Pais
    template_name = 'paises/pais_detalhe.html' 
    context_object_name = 'pais'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cidade'] = self.object.cidade.all()
        return context

class CidadesView(DetailView):
    model = Cidade
    template_name = 'paises/cidades.html'
    context_object_name = 'cidade'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
