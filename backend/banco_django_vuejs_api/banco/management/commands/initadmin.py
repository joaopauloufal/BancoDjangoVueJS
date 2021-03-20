from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Cria um superusuário se o mesmo não existe'

    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
              username='admin',
              email='admin@example.com',
              password='12345678'
            )
            print(u'Super usuario criado!')
        else:
            print(u'O Super usuario ja existe no banco de dados...')
