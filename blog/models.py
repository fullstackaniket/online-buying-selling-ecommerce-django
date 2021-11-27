from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
# Create your models here.
class Category(models.Model):
    c_name=models.CharField(max_length=40)
    
    
    def __str__(self):
        return self.c_name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio= models.TextField(max_length=500,blank=True,)
    location = models.CharField(max_length=35,blank=True)
    dob=models.DateTimeField(null=True, blank=True)
    pic=models.ImageField(upload_to="media/profile", default="awatar.jpg")
   
    
    
    @receiver(post_save,sender=User)
    def save_profile_user(sender, instance,created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()
    
    def __str__(self):
        return self.user.username


class Product(models.Model):
 
    cate=models.ForeignKey(Category, on_delete=models.CASCADE)
    p_img=models.ImageField(upload_to='porduct')
    p_img1=models.ImageField(upload_to='porduct',blank=True)
    p_img2=models.ImageField(upload_to='porduct',blank=True)
    price=models.DecimalField(max_digits=7,decimal_places=0)
    name=models.CharField(max_length=70)
    description=models.TextField()
    date_posted=models.DateField(auto_now=True)
    p_state=models.CharField(max_length=100)
    p_city=models.CharField(max_length=100)
    seller=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    