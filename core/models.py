from django.db import models
import uuid
from django.utils.text import slugify
from django.conf import settings
from stdimage.models import StdImageField
from django.contrib.auth import get_user_model 
from django.contrib.auth.models import AbstractUser , BaseUserManager

class UsuarioManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('O e-mail é obrigatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields) 
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email,password=None , **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('super usuario precisa ter is_superuser=True')
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('super usuario precisa ter is_staff=True')

        return self._create_user(email,password, **extra_fields)


class CustomUsuario(AbstractUser):
    email = models.EmailField('E-mail', unique=True)
    fone = models.CharField('fone', max_length=15) 
    is_staff = models.BooleanField('Membro da equipe', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'fone']



    def __str__(self):
        return self.email
    
    objects = UsuarioManager()




def get_file_path(instance, filename):
    """Generate a unique file path for uploaded files."""
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return filename

class Base(models.Model):
    criado = models.DateField('Criado', auto_now_add=True)
    modificado = models.DateField('Modificado', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True 


class Servico(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Grafico'),
        ('lni-users', 'Usuarios'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )

    servico = models.CharField('Serviço', max_length=100)
    descricao = models.TextField('Descrição', max_length=300)
    icone = models.CharField('Icon', max_length=12, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.servico


class Contato(Base):
    nome = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-mail', max_length=150)
    assunto = models.CharField('Assunto', max_length=100)
    mensagem = models.TextField('Mensagem', max_length=500)

  

    def __str__(self):
        return f'{self.nome}'




class Pais(Base):
    nome = models.CharField(max_length=60)
    slug = models.SlugField(unique=True,blank=True)
    descricao = models.TextField()
    imagem = StdImageField(
        upload_to='paises',
        variations={
            'thumb': (200,100),
            'normal': (600,600)
        },
        blank=True,
        null=True
    )


    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args,**kwargs)

    
    def __str__(self):
        return self.nome
    

class Cidade(models.Model):
    pais = models.ForeignKey(Pais, related_name='cidade', on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    imagemCdd = StdImageField(
        upload_to='paises',
         variations={
            'normal': (150,100),
        },
        blank=True,
        null=True
    )
    populacao = models.CharField(max_length=19)
    idh = models.DecimalField(max_digits=5 , decimal_places=3)
    descricao = models.TextField()
    slug = models.SlugField(unique=True, blank=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome

    
 