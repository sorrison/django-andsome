from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext as _
from django.utils.encoding import force_unicode
from django_common.middleware.threadlocals import get_current_user


def log_and_message(obj, flag):

    user = get_current_user()
    opts = obj.__class__._meta

    if flag == ADDITION:
        LogEntry.objects.log_action(
            user.id,
            ContentType.objects.get_for_model(obj.__class__).id,
            obj._get_pk_val(),
            force_unicode(obj),
            ADDITION
        )
        message = _('The %(name)s "%(obj)s" was added successfully.') % {'name': force_unicode(opts.verbose_name), 'obj': force_unicode(obj)}
    elif flag == CHANGE:
        LogEntry.objects.log_action(
            user.id,
            ContentType.objects.get_for_model(obj.__class__).id,
            obj._get_pk_val(),
            force_unicode(obj),
            CHANGE
        )
        message = _('The %(name)s "%(obj)s" was changed successfully.') % {'name': force_unicode(opts.verbose_name), 'obj': force_unicode(obj)}
    elif flag == DELETION:
        LogEntry.objects.log_action(
            user.id,
            ContentType.objects.get_for_model(obj.__class__).id,
            obj._get_pk_val(),
            force_unicode(obj),
            DELETION
        )
        message=_('The %(name)s "%(obj)s" was deleted successfully.') % {'name': force_unicode(opts.verbose_name), 'obj': force_unicode(obj)}

    user.message_set.create(message=message)


def unique(seq):
    """Makes a list unique"""
    # Not order preserving
    keys = {}
    for e in seq:
        keys[e] = 1
    return keys.keys()
