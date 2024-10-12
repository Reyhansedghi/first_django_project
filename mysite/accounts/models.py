from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import PermissionsMixin
from . managers import UserManager
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save  
from django.dispatch import receiver  # new
# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(
        _("phone_number"),
        max_length=11,
        unique=True,
        help_text=_(
            "Required. 11 numbers"
        ),
        error_messages={
            "unique": _("A user with that phone_number already exists."),
        },
    )

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = UserManager()

    
    USERNAME_FIELD = "phone_number"
    
    def get_full_name(self):
        
        full_name = "%s %s" % (self.userprofile.first_name , self.userprofile.last_name)
        return full_name.strip()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
       # abstract = True
  

class UserProfile(models.Model):
    USERTYPE_CHOICES=(('حقیقی','حقیقی'),('حقوقی','حقوقی'))
    COMPANYTYPE_CHOICES=(('سهامی عام','سهامی عام'),('سهامی خاص','سهامی خاص'),
                         ('با مسءولیت محدود','با مسءولیت محدود'),('تعاونی','تعاونی'),)
    CITY_CHOICES={
        'te':'tehran',
        'es':'esfahan',
        'bb':'babol',
        'ka':'karaj',
        'gi':'gilan',
    }
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='userprofile')
    status=models.CharField(_("status"),choices=USERTYPE_CHOICES,default='حقیقی',max_length=50)
    companytype=models.CharField(choices=COMPANYTYPE_CHOICES,default='سهامی عام',max_length=150)
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    company_name=models.CharField(_("company"), max_length=150, blank=True)
    
    city=models.CharField(_("city"),choices=[(key, value) for key, value in CITY_CHOICES.items()],default='te', max_length=2, null=True)
    social_media=models.TextField(verbose_name="صفحات مجازی", null=True)
    
    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

class OtpCode(models.Model):
    phone_number = models.CharField(max_length=11)
    code = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.phone_number} --- {self.code}"