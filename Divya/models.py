from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS = (
    (0,"not_featured"),
    (1,"Featured")
)

class My_profile_nav(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True)
    short_intro = models.CharField(max_length=200,blank=True, null=True)
    side_profile_pic = models.ImageField(blank=True, null=True) 
    linkedin_link = models.URLField(("linkedin_link"), 
            max_length=128, 
            db_index=True, 
            unique=False, 
            blank=True
        )
    my_email = models.EmailField(("my_email"), max_length=128, 
        db_index=True, 
        unique=False, 
        blank=True
    )
    github_link = models.URLField(("github_link"), 
            max_length=128, 
            db_index=True, 
            unique=False, 
            blank=True
        )
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    Featured = models.IntegerField(choices=STATUS, default=1)
    def __str__(self):
        return self.name
class My_profile_home(models.Model):
    full_name = models.CharField(max_length=100,blank=True, null=True)
    my_job_status = models.CharField(max_length=100,blank=True, null=True)
    mid_intro = models.TextField(max_length=600,blank=True, null=True)
    side_profile_pic = models.ImageField(blank=True, null=True) 
    what_i_do = models.TextField(max_length=600,blank=True, null=True)

    def __str__(self):
        return self.full_name  
class My_portfolio(models.Model):

    portfolio_title = models.CharField(max_length=300,blank=True, null=True)
    portfolio_short_dis = models.TextField(max_length=600,blank=True, null=True)
    portfolio_image = models.ImageField(blank=True, null=True)
    portfolio_readtime = models.CharField(max_length=100,blank=True, null=True)
    portfolio_publish_time = models.CharField(max_length=100,blank=True, null=True)
    
    portfolio_git_link = models.URLField(("portfolio_git_link"), max_length=128, 
        db_index=True, 
        unique=False, 
        blank=True
    )

    

    Featured = models.IntegerField(choices=STATUS, default=1)
    

    def __str__(self):
        return self.portfolio_title
class My_blog(models.Model):

    blog_title = models.CharField(max_length=300,blank=True, null=True)
    blog_short_dis = models.TextField(max_length=600,blank=True, null=True)
    blog_image = models.ImageField(blank=True, null=True)
    blog_readtime = models.CharField(max_length=100,blank=True, null=True)
    blog_publish_time = models.CharField(max_length=100,blank=True, null=True)
    blog_link = models.URLField(("blog_link"), max_length=128, 
        db_index=True, 
        unique=False, 
        blank=True
    )


    Featured = models.IntegerField(choices=STATUS, default=1)
    

    def __str__(self):
        return self.blog_title




class Contact(models.Model):
    con_name = models.CharField(max_length=100,blank=True, null=True)
    con_email = models.EmailField(("my_email"), max_length=128, 
        db_index=True, 
        unique=False, 
        blank=True
    )
    con_message = models.TextField(max_length=600,blank=True, null=True)

    def __str__(self):
        return self.con_name

class Certification(models.Model):
   
    title = models.CharField(max_length=255)
    issuer = models.CharField(max_length=255)
    pic = models.ImageField(blank=True, null=True) 
    verification_link = models.URLField(("verification link"), 
            max_length=128, 
            db_index=True, 
            unique=False, 
            blank=True
        )
    
    
    Featured = models.IntegerField(choices=STATUS, default=1)
    def __str__(self):
        return self.title     
class Video(models.Model):
    caption=models.CharField(max_length=100)
    video=models.FileField(upload_to='videos/%y')
    def __str__(self):
        return self.caption