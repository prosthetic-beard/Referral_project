from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):

    def create_user(self, email, password=None):

        # if not all([email, company_name]):
        #     raise ValueError('Email and Company name are required.')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.username = user.generate_uniquie_username()
        user.save()

        return user

    def create_superuser(self, email, password):

        user = self.create_user(email=self.normalize_email(email), company_name='')
        user.set_password(password)
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save()

        return user