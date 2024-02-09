"""
Exists to ensure you can always log in with admin/password when running in
'dev' mode - see tests/README.rst
"""

from django.contrib.auth.models import User
from django.contrib.staticfiles.management.commands.runserver import Command as BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    def check_migrations(self):
        call_command('migrate', interactive=True)
        if not User.objects.exists():
            self.stdout.write(
                "Welcome to Nexus test mode\n" "Login with username 'admin', password 'password'",
            )
            user = User(username='admin', is_superuser=True, is_staff=True)
            user.set_password('password')
            user.save()
