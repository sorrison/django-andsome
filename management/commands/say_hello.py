from django.core.management.base import NoArgsCommand

class Command(NoArgsCommand):
    help = "Runs a shell output that writes out Hello person to the console."

    requires_model_validation = False
    can_import_settings = True

    def handle_noargs(self, **options):
        print "Hello person"