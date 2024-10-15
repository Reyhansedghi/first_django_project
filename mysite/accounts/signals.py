from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile
from blog.models import Post
from services.models import Services
from products.models import Product
@receiver(post_save, sender=[Product, Services])
def create_post(sender, instance, created, **kwargs):
    if created:
        if isinstance(instance, Product):
            Post.objects.create(product=instance, title=instance.name, content='')
        elif isinstance(instance, Services):
            Post.objects.create(service=instance, title=instance.name, content='')



            
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.userprofile.save()
