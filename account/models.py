from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.utils.translation import ugettext_lazy as _
from account.managers import UserManager

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_worker = models.BooleanField(default=False)
    
    email = models.EmailField(_("Email"), max_length=254, unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    profile_img = models.ImageField(_("Profile image"),upload_to='profile-pictures/', null=True, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'    
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email



class Customer(models.Model):

    user = models.OneToOneField("account.User", verbose_name=_("customer"), on_delete=models.CASCADE, primary_key=True, related_name='customer')
    
    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return self.user.email
    

class Worker(models.Model):

    LANGUAGES = (
        ('Azerbaijan', 'Azerbaijan'),
        ('English', 'English'),
        ('Russian', 'Russian'),
        ('Turkish', 'Turkish'),
    )

    EXPERIENCE = (
        ('1 year', '1 year'),
        ('2 years', '2 years'),
        ('3 years', '3 years'),
        ('4 years', '4 years'),
        ('5+ years', '5+ years'),
    )

    user = models.OneToOneField("account.User", verbose_name=_("Worker"), on_delete=models.CASCADE, primary_key=True, related_name='worker')
    work_place = models.CharField(_("Work Place"), max_length=50)

    elite_tasker = models.BooleanField(_("Elite Tasker"), default=False)
    about = models.TextField(_("About"))
    languages = models.CharField(_("Languages"), choices=LANGUAGES, max_length=50)
    rating = models.IntegerField(_("Rating"), blank=True, null=True)
    experience = models.CharField(_("Experience"), choices=EXPERIENCE, max_length=50)
    birth_date = models.CharField(_("Birth Date"), max_length=50)

    class Meta:
        verbose_name = _("Worker")
        verbose_name_plural = _("Workers")

    def __str__(self):
        return self.user.first_name


class WorkPlace(models.Model):

    title = models.CharField(_("Title"), max_length=50)

    class Meta:
        verbose_name = _("WorkPlace")
        verbose_name_plural = _("WorkPlaces")

    def __str__(self):
        return self.title

    