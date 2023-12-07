from django.core.management.base import BaseCommand
from app1.models import User

class Command(BaseCommand):
    help = "Create user."
    def handle(self, *args, **kwargs):
        user = User(name='Маша', email='masha@example.com', phone='333333', address='Минск')
        user.save()
        self.stdout.write(f'{user}')