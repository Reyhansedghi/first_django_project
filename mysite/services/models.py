from django.db import models
from django.utils import timezone
from accounts.models import User
from django.urls import reverse
from extensions.utils import jalali_converter
# Create your models here.
class ServicesCategory(models.Model):
    
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

class ServicesSubCategory(models.Model):
    parent=models.ForeignKey(ServicesCategory,blank=True,null=True,on_delete=models.CASCADE)
    title=models.CharField(null=True,max_length=30)
    slug=models.SlugField(null=True)
    is_visible=models.BooleanField(default=True)
    position=models.IntegerField(null=True)
    class Meta:
        ordering = ('position',)
        verbose_name = 'دسته بندی 2 خدمات'
        verbose_name_plural = 'دسته بندی های 2 خدمات '

    def __str__(self):
        return self.title
    
class ServicesSubSubCategory(models.Model):
    parent=models.ForeignKey(ServicesSubCategory,blank=True,null=True,on_delete=models.CASCADE)
    title=models.CharField(null=True,max_length=30)
    slug=models.SlugField(null=True)
    is_visible=models.BooleanField(default=True)
    position=models.IntegerField(null=True)
    class Meta:
        ordering = ('position',)
        verbose_name = 'دسته بندی 3 خدمات'
        verbose_name_plural = 'دسته بندی های 3 خدمات '

    def __str__(self):
        return self.title

class Services(models.Model):
    
    GRADE_CHOICES=((1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'))

    is_seller=models.BooleanField(verbose_name='عرضه کننده / تقاضا کننده',default=True)
    is_legal=models.BooleanField(verbose_name='حقوقی / حقیقی',default=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_services',null=True,verbose_name='نام کاربری')
    category=models.ManyToManyField('ServicesCategory',blank=True,verbose_name='گروه تخصص')
    subcategory=models.ManyToManyField('ServicesSubCategory',blank=True,verbose_name='گروه ')
    subsubcategory=models.ManyToManyField('ServicesSubSubCategory',blank=True,verbose_name='2گروه ')
    title=models.CharField(null=True,max_length=30,verbose_name='دانش فنی')
    description=models.TextField(null=True,verbose_name='توضیحات اضافه')
    slug=models.SlugField(null=True,allow_unicode=True)
    
    created=models.DateTimeField(auto_now_add=timezone.now,null=True)
    updated=models.DateTimeField(auto_now=timezone.now,)
    grade=models.IntegerField(choices=GRADE_CHOICES,default=1)
    certificate=models.ImageField(upload_to='image',null=True,blank=True,verbose_name='گواهینامه')
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
    def get_subcategory(self):
        return ', '.join([cat.title for cat in self.subcategory.all()])
    def get_subcategoryslug(self):
        return ', '.join([cat.slug for cat in self.subcategory.all()])
    def get_subsubcategory(self):
        return ', '.join([cat.title for cat in self.subsubcategory.all()])
    def get_subsubcategoryslug(self):
        return ', '.join([cat.slug for cat in self.subsubcategory.all()])
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

