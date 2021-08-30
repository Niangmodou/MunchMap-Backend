from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(
        self, username=None, full_name=None, email=None, password=None, zipcode=None
    ):
        user = self.model(
            username=username, full_name=full_name, email=email, zipcode=zipcode
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password, **extra_fields):
        print("Hi")
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))

        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        user = self.model(username=username, email=email, zipcode=10003)
        user.set_password(password)
        user.save()

        return user
