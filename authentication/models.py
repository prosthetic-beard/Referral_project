from django.db import models
from base.models import TimestampedModel
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
import uuid
import random


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin, TimestampedModel):
    id = models.UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True, verbose_name='ID', editable=False)
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.CharField(max_length=255, unique=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    activation_token = models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, unique=True)
    referral_code = models.CharField(null=True, blank=True, max_length=255)
    is_active = models.BooleanField(default=True)
    is_vip = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    first_app = models.BooleanField(default=False)
    second_app = models.BooleanField(default=False)
    third_app = models.BooleanField(default=False)
    fourth_app = models.BooleanField(default=False)
    

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
    @property
    def fullname(self):
        return f'{self.lastname} {self.firstname}'
    

    def generate(self):
        ten_digits = str(random.randint(1000000000, 9999999999))
        return ten_digits
        
    def generate_uniquie_username(self):
        # Generates a unique username id
        unique_username = self.generate()
        
        # Filter user by the generated unique username id
        user = User.objects.filter(username=unique_username)
        if not user:
            username = unique_username
            return username
        
    def save(self, *args, **kwargs):
      self.username = self.generate_uniquie_username()
      super(User, self).save(*args, **kwargs) 