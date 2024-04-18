from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, user, departamento, email, password=None, **extra_fields):
        if not user:
            raise ValueError('El usuario debe tener un nombre de usuario')
        
        user = self.model(
            username=user,
            departamento=departamento,
            password=password,
            email=self.normalize_email(email),
            **extra_fields
        )
        
        extra_fields['email'] = self.normalize_email(email)  
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_superuser(self, user, departamento, email, telefono, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        user = self.create_user(
            user=user,
            departamento=departamento,
            email=email,
            telefono=telefono,
            password=password,
            **extra_fields
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user