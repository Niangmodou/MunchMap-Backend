import django
import os

# Configuring Django Settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from users.models import AppUser


def main():
    AppUser.objects.all().delete()

    print("App Users:", len(AppUser.objects.all()))


if __name__ == "__main__":
    main()
