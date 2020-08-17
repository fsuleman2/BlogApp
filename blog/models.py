from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    CATEGORY_CHOICES = (
        ('Technology','Technology'),
        ('Food','Food'),
        ('Travel','Travel'),
        ('Health','Health'),
        ('Lifestyle','Lifestyle'),
    )

   




    cover = models.FileField(default='') #photo
    cover2 = models.FileField(default='')
    title = models.CharField(max_length=2000,default='')
    slug = models.SlugField(default='')
    author = models.CharField(max_length=2000,default='')
    text = models.TextField(default='')
    text_2 = models.TextField(default='')
    quote = models.CharField(max_length=2000,default='')
    quote_name = models.CharField(max_length=2000,default='')
    l_heading = models.CharField(max_length=2000,default='')
    l_heading_text = models.CharField(max_length=2000,default='')
    s_heading = models.CharField(max_length=2000,default='')
    s_heading_text = models.CharField(max_length=2000,default='')
    category = models.CharField(max_length=2000,choices=CATEGORY_CHOICES)
    created_date = models.DateTimeField(default='')
    tag_1 = models.CharField(max_length=2000,default='')
    tag_2 = models.CharField(max_length=2000,default='')
    tag_3 = models.CharField(max_length=2000,default='')
    
    class Meta:
        ordering =['-created_date']
    def __str__(self):
        return self.title