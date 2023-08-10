from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, phone_number, password, **extra_fields):
        """
        Create and save a user with the given phone_number and password.
        """
        if not phone_number:
            raise ValueError(_("The Phone number must be set"))
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_number, password, **extra_fields):
        """
        Create and save a SuperUser with the given phone_number and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(phone_number, password, **extra_fields)


class RoleChoices(models.TextChoices):
    ADMIN = 'admin', _('admin')
    OWNER = 'owner', _('owner')
    CUSTOMER = 'customer', _('customer')


class User(AbstractUser):
    username = None
    first_name = None
    last_name = None
    phone_number = PhoneNumberField(unique=True)
    full_name = models.CharField(max_length=100)
    role = models.CharField(choices=RoleChoices.choices, max_length=50, default=RoleChoices.CUSTOMER)
    image = models.ImageField(upload_to='image/', blank=True)
    is_phone_confirmed = models.BooleanField(default=False)
    email = models.EmailField(blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    
    
    def __str__(self):
        return f'{self.phone_number}'