from django.db.models.signals import post_save
from django.dispatch import receiver
from WMS.models import Manager
from users.models import User


@receiver(post_save, sender=Manager)
def user_created(sender, instance, created, **kwargs):
    if created:
        user = User.objects.get(pk=instance.user.pk)
        user.isManager = True
        user.save()
