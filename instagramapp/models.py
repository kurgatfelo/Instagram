from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = CloudinaryField('image')
    bio = models.TextField(max_length=300, default="Bio", blank=True)

    def __str__(self):
        return self.user.username

class Image(models.Model):
    img_name = models.CharField(max_length=80,blank=True)
    caption = models.CharField(max_length=500)
    profile = models.ForeignKey(Profile,on_delete = models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    comments = models.CharField(max_length=100,blank=True)
    image = CloudinaryField('images')

    def __str__(self):
        return self.img_name

class Comment(models.Model):
    comment = models.TextField()
    post= models.ForeignKey(Image, on_delete=models.CASCADE)
    user= models.ForeignKey(Profile, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return f'{self.user.user} Image'