from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    user =models.OneToOneField(User, on_delete = models.CASCADE,related_name ='profile')
    image =models.ImageField(upload_to='profile', blank=True, null=True)
    gender =models.CharField(max_length = 1,null="True", blank=True ,choices=(("M","Male"), ("F","Female")))
    phone_number = PhoneNumberField(blank=True, null=True)
    bio = models.TextField()
    github_url=models.URLField(null="True", blank=True,max_length=255)
    linkedin_url=models.URLField(null="True", blank=True,max_length=255)
    twitter_url=models.URLField(null="True", blank=True,max_length=255)
    instagram_url=models.URLField(null="True", blank=True,max_length=255)


    def __str__(self):
        return self.user.username

@receiver(post_save, sender =User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

