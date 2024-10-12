from django.db import models
from django.utils import timezone
from accounts.models import User
from django.urls import reverse
from extensions.utils import jalali_converter
# Create your models here.
class ServicesCategory(models.Model):
    parent=models.ForeignKey('self',null=True,blank=True,related_name="child",on_delete=models.SET_NULL)
    title=models.CharField(null=True,max_length=30)
    slug=models.SlugField(null=True)
    is_visible=models.BooleanField(default=True)
    position=models.IntegerField(null=True)
    class Meta:
        ordering = ('position',)
        verbose_name = 'دسته بندی خدمات'
        verbose_name_plural = 'دسته بندی های خدمات '

    def __str__(self):
        return self.title
    #def get_absolute_url(self):
        #return reverse("blog:category_list" , kwargs={"category_slug":self.slug})

class Services(models.Model):
    USERSTATUS_CHOICES=(('تقاضا کننده','تقاضا کننده'),('عرضه کننده','عرضه کننده'))
    
    userstatus=models.CharField(choices=USERSTATUS_CHOICES,default='تقاضا کننده',max_length=50)
    
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_services',null=True,verbose_name='نام کاربری')
    
    category=models.ManyToManyField('ServicesCategory',blank=True,verbose_name='گروه تخصص')
    title=models.CharField(null=True,max_length=30,verbose_name='نام خدمات')
    slug=models.SlugField(null=True,allow_unicode=True)
    description=models.TextField(null=True,verbose_name='شرح خدمات')
    capacity=models.CharField(null=True,verbose_name='ظرفیت',blank=True,max_length=50,)
    created=models.DateTimeField(auto_now_add=timezone.now,null=True)
    updated=models.DateTimeField(auto_now=timezone.now,)
    price=models.DecimalField(max_digits=6, decimal_places=2,verbose_name='قیمت',null=True)
    
    class Meta:
      verbose_name = 'سرویس'
      verbose_name_plural = 'سرویس ها'
      #ordering=('-publish',)
    def __str__(self):
       return self.title
    
    def get_category(self):
        return ', '.join([cat.title for cat in self.category.all()])
    def get_categoryslug(self):
        return ', '.join([cat.slug for cat in self.category.all()])
     # def get_absolute_url(self):
      #  return reverse("blog:post_detail" , kwargs={"year":self.publish.year,"month":self.publish.month,"day":self.publish.day,"slug":self.slug})
    #def save(self, *args, **kwargs):
        slug = ""
        for char in self.title:
            if char.isalpha():
                slug += char
            elif char == " ":
                slug += "-"
        self.slug = slug
        super().save(*args, **kwargs)
#def save error dare bARAYE POST_DETAIL

