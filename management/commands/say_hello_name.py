from django.core.management.base import LabelCommand
from optparse import make_option

class Command(LabelCommand):
    help = "Runs a shell output that writes out Hello and the specified name to the console."
    args = "[name]"
    label = 'person\'s name'
    
    option_list = LabelCommand.option_list + (
        make_option('--capitalize', '-c', action='store_true', dest='capitalize',
            help='Tells Django to capitalize the name.'),
    )

    requires_model_validation = False
    can_import_settings = True

    def handle_label(self, name, **options):        
        if options.get('capitalize', False):
            name = name.capitalize()
        
        print "Hello %s" % name