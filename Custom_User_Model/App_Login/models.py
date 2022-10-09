from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
from django.utils.translation import gettext_lazy

class MyUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):

        if not email:

            raise ValueError('Email is required!')

        if not password:

            raise ValueError('Password is required!')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:

            raise ValueError('superuser must have is_staff=True')

        if extra_fields.get('is_superuser') is not True:

            raise ValueError('superuser must have is_superuser=True')

        return self.create_user(email, password, **extra_fields)



class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=264, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    date_of_birth = models.DateField(null=True)
    address = models.TextField()
    country = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=20)

    is_staff = models.BooleanField(

        gettext_lazy('is_staff'),
        default=False,
        help_text=gettext_lazy('Designates whether the user can log in this site.')

    )

    is_active = models.BooleanField(

        gettext_lazy('is_active'),
        default=True,
        help_text=gettext_lazy('Designates whether the user should be treated as active.Unselect this instead of deleting account.')

    )

    USERNAME_FIELD = 'email'

    objects = MyUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email


