from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

# Create your models here.

flag_choises={
    ('Englang','Englang'),
    ('France','France'),
}

class Jewellery(models.Model):
    name=models.CharField(_ ('name') ,max_length=20)
    price=models.FloatField()
    images=models.ImageField(upload_to='shoping/' , null=True,blank=True)
    flag=models.CharField(_ ('flag'), max_length=20 ,choices=flag_choises)
    description=models.TextField(_ ('description'), max_length=200)
    slug=models.SlugField(null=True,blank=True)


    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
       self.slug=slugify(self.name)
       super(Jewellery, self).save(*args, **kwargs) # Call the real save() method




class Fashion(models.Model):
    name=models.CharField(_ ('name') ,max_length=20)
    price=models.FloatField()
    images=models.ImageField(upload_to='fashion/' , null=True,blank=True)
    flag=models.CharField(_ ('flag'), max_length=20 ,choices=flag_choises)
    description=models.TextField(_ ('description'), max_length=200)
    slug=models.SlugField(null=True,blank=True)


    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
       self.slug=slugify(self.name)
       super(Fashion, self).save(*args, **kwargs) # Call the real save() method






class Electronic(models.Model):
    name=models.CharField(_ ('name') ,max_length=20)
    price=models.FloatField()
    images=models.ImageField(upload_to='electronic/' , null=True,blank=True)
    flag=models.CharField(_ ('flag'), max_length=20 ,choices=flag_choises)
    description=models.TextField(_ ('description'), max_length=200)
    slug=models.SlugField(null=True,blank=True)


    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
       self.slug=slugify(self.name)
       super(Electronic, self).save(*args, **kwargs) # Call the real save() method
