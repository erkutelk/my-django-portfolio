from django.db import models # type: ignore
from ckeditor.fields import RichTextField # type: ignore
from django.utils.text import slugify # type: ignore

class title(models.Model):
    title=models.CharField(max_length=20)
    description=models.CharField(max_length=20)
    linkedin=models.CharField(max_length=20)
    instagram=models.CharField(max_length=20)
    git=models.CharField(max_length=20)
    images=models.ImageField()

class about(models.Model):
    about_title=models.TextField()
    about_description=models.CharField(max_length=50)
    about_image=models.ImageField()

class servic(models.Model):
    title=models.CharField(max_length=25)
    description=models.CharField(max_length=25)
    isActive=models.BooleanField()

class menu(models.Model):
    title=models.CharField(max_length=15)
    link=models.SlugField(default='', blank=True, null=False, unique=True, db_index=True)
    isActive=models.BooleanField()

    def save(self, *args, **kwargs):
        if not self.link:  # Eğer slug mevcut değilse
            self.link = slugify(self.title)  # title'dan slug oluştur
        super().save(*args, **kwargs)  # Üst sınıfın save metodunu çağır


class portfoy_kategori(models.Model):
    kategori=models.CharField(max_length=12)
    isActive=models.BooleanField()
    def __str__(self) -> str:
        return self.kategori

class portfoy_project(models.Model):
    title = models.CharField(max_length=12)
    description = RichTextField()
    images = models.ImageField(upload_to='images/')
    isActive = models.BooleanField()
    date = models.DateField(auto_now=True)
    slug = models.SlugField(default='', blank=True, null=False, unique=True, db_index=True)
    categories = models.ForeignKey(portfoy_kategori, on_delete=models.CASCADE)

    
class blog_kategori(models.Model):
    kategori=models.CharField(max_length=20)
    slug = models.SlugField(unique=True, blank=True, null=False, db_index=True)
    isActive=models.BooleanField()
    def __str__(self) -> str:
        return self.kategori
    
    def save(self, *args, **kwargs):
        if not self.slug:  # Eğer slug mevcut değilse
            self.slug = slugify(self.kategori)  # title'dan slug oluştur
        super().save(*args, **kwargs)  # Üst sınıfın save metodunu çağır


class blog(models.Model):
    image = models.ImageField(upload_to='images', default="")
    title_blog=models.CharField(max_length=50)
    description_blog=models.TextField()
    isBlog_blog=models.BooleanField()
    blog_kategori = models.ForeignKey(blog_kategori, on_delete=models.CASCADE)
    slug=models.SlugField(default='',unique=True,db_index=True,blank=True, null=False)
    date = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:  # Eğer slug mevcut değilse
            self.slug = slugify(self.title_blog)  # title'dan slug oluştur
        super().save(*args, **kwargs)  # Üst sınıfın save metodunu çağır
    
class contact(models.Model):
    title=models.CharField(max_length=50)
    konum=models.CharField(max_length=50)
    konum2=models.CharField(max_length=50)
    telefon=models.CharField(max_length=11)
    mail=models.CharField(max_length=20)



class UploadModel(models.Model):
    image=models.ImageField(upload_to='images')