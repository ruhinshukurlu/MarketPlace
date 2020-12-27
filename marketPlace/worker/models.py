from django.db import models
from django.utils.translation import ugettext_lazy as _
from slugify import slugify
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from notifications.signals import notify
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Service(models.Model):

    title = models.CharField(_("Title"), max_length=50)
    description = models.TextField(_("Description"), blank=True, null=True)
    image = models.ImageField(_("Image"), upload_to='service-photos/', blank=True, null = True)
    created_at = models.DateField(_("Created At"), auto_now=False, auto_now_add=True)
    slug = models.SlugField(_("Slug"), blank=True, null=True)

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Service")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Service, self).save(*args, **kwargs)



class Skill(models.Model):

    user = models.ForeignKey("account.User", verbose_name=_("User"), on_delete=models.CASCADE, related_name='skill')
    service = models.ForeignKey("Service", verbose_name=_("Service"), on_delete=models.CASCADE, related_name='skill')
    price = models.IntegerField(_("Price"))
    vehicles = models.ManyToManyField('Vehicle', verbose_name=_("Vehicle"), related_name='skill')
    tools = models.ManyToManyField('Tool', verbose_name=_("Tool"), related_name='skill')
    experience = models.TextField(_("Experience"))
    task_count = models.IntegerField(_("Task Count"), blank=True, null=True)

    class Meta:
        verbose_name = _("Skill")
        verbose_name_plural = _("Skills")

    def __str__(self):
        return self.service.title


class Task(models.Model):

    user = models.ForeignKey("account.User", verbose_name=_("User"), on_delete=models.CASCADE, related_name='user_task')
    worker = models.ForeignKey("account.User", verbose_name=_("Worker"), on_delete=models.CASCADE, related_name='worker_task', blank=True, null=True)
    skill = models.ForeignKey("Skill", verbose_name=_("Skill"), on_delete=models.CASCADE, related_name='task')

    accept = models.BooleanField(_("Accept"), default=False)
    denied = models.BooleanField(_("Denied"), default=False)
    text = models.TextField(_("Text"))
    created_at = models.DateField(_("Created At"), auto_now=False, auto_now_add=True)

    date = models.DateField(_("Date"), blank=True, null=True)
    time = models.TimeField(_("Time"), blank=True, null=True)

    class Meta:
        verbose_name = _("Task")
        verbose_name_plural = _("Tasks")

    def __str__(self):
        return f"{self.user.first_name}"

@receiver(post_save,sender=Task)
def send_user_data_when_created_by_admin(sender, instance, **kwargs):
    
    if instance.accept:
        print('ok accept')
        recipient = User.objects.get(email=instance.user.email)
        notify.send(sender, recipient = recipient , verb=f'Your {instance.skill.service.title} task accepted by {instance.worker.first_name} {instance.worker.last_name} <a class="btn btn-outline-primary" href="/payment">Go to Payment</a>')

    elif instance.denied:
        print('ok deny')
        recipient = User.objects.get(email=instance.user.email)
        notify.send(sender, recipient = recipient , verb=f'Your {instance.skill.service.title} task denied by {instance.worker.first_name} {instance.worker.last_name}')
    
    else:
        recipient = User.objects.get(email=instance.worker.email)
        notify.send(sender, recipient = recipient , verb=f'You have new {instance.skill.service.title} task from {instance.user.first_name} {instance.user.last_name}')



class Vehicle(models.Model):

    title = models.CharField(_("Title"), max_length=50)

    class Meta:
        verbose_name = _("Vehicle")
        verbose_name_plural = _("Vehicles")

    def __str__(self):
        return self.title


class Tool(models.Model):

    title = models.CharField(_("Title"), max_length=50)

    class Meta:
        verbose_name = _("Tool")
        verbose_name_plural = _("Tools")

    def __str__(self):
        return self.title


class SkillPhoto(models.Model):

    skill = models.ForeignKey("Skill", verbose_name=_("Skill"), on_delete=models.CASCADE, related_name='skillphoto')
    image = models.ImageField(_("Image"), upload_to='skill-photos/')

    class Meta:
        verbose_name = _("Photo")
        verbose_name_plural = _("Photos")

    def __str__(self):
        return self.skill.user.email


class Review(models.Model):

    user = models.ForeignKey("account.User", verbose_name=_("User"), on_delete=models.CASCADE, related_name='review')
    skill = models.ForeignKey("Skill", verbose_name=_("Skill"), on_delete=models.CASCADE, related_name='review')
    text = models.TextField(_("Text"))
    rating = models.IntegerField(_("Rating"), blank=True, null=True)
    commented_at = models.DateField(_("Commented At"), auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = _("Review")
        verbose_name_plural = _("Reviews")

    def __str__(self):
        return self.user.email

   