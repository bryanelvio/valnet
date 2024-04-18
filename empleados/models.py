from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin, User
from .manager import UserManager

class Empleados(AbstractUser):
    departamento = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True, unique=True)
    telefono = models.IntegerField(null=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    groups = models.ManyToManyField('auth.Group', related_name='empleados_grupos', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='empleados_permisos', blank=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['departamento', 'email', 'telefono']
    

    objects = UserManager()
    
    def __str__(self):
        return self.username
    