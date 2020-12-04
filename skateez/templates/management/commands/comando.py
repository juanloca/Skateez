#from django.core.management.base import BaseCommand, CommandError
#from polls.models import Question as Poll

#class Command(BaseCommand):
#    help = 'Closes the specified poll for voting'
#
#    def add_arguments(self, parser):
#        parser.add_argument('skateez_ids', nargs='+', type=int)
#
#    def handle(self, *args, **options):
#        for skateez_id in options['skateez_ids']:
#            try:
#                skateez = skateez.objects.get(pk=skateez_id)
#            except skateez.DoesNotExist:
#                raise CommandError('skateez "%s" does not exist' % skateez_id)
#
#            skateez.opened = False
#            skateez.save()
#
#            self.stdout.write(self.style.SUCCESS('Successfully closed skateez "%s"' % skateez_id))

from django.core.management.base import BaseCommand, CommandError
from skateez.models import Tabla

class Command(BaseCommand):

    help = ''