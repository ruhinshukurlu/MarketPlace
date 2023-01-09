from django.db.models.signals import pre_save, post_init
from django.dispatch import receiver
from django.utils.translation import ugettext as _
from worker.models import *
from django.contrib.auth import get_user_model
from slugify import slugify

User = get_user_model()

@receiver(pre_save,sender=Service)
def send_user_data_when_created_by_admin(sender, instance, **kwargs):
    instance.slug = slugify(sender.title)
