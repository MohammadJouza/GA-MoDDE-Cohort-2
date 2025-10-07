from django.apps import AppConfig
from django.contrib.auth import get_user_model


class MainAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main_app'

# !- Extra (dont do it on production)
    # /create superadmin
    def ready(self):
        user_name = "superadmin"
        pass_word = "0000"
        User = get_user_model()
        if not User.objects.filter(username=user_name).exists():
            User.objects.create_superuser(
                username=user_name, email="superadmin@example.com", password=pass_word
            )

