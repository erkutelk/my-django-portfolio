import os
import django
import pytest
from home.models import blog,blog_kategori
class Anasayfa:
    @staticmethod
    def blog_olustur():
        try:
            kategori = blog_kategori.objects.create(kategori="Test Kategorisi",slug="test-kategorisi",isActive=True)
            project = blog.objects.create(image='Test',title_blog='Test',description_blog='test',isBlog_blog=True,blog_kategori=kategori,)
            return True
        except Exception as e:
            print(f'Hata meydana geldi: {e}')
            return False
        
    @staticmethod
    def blog_sil():
        try:
            blog_id=blog.objects.filter(pk=1).first()
            blog_id.delete()
            return True
        except:
            return False
        
    @staticmethod
    def blog_guncelle():
        try:
            blog_id = blog.objects.filter(pk=1)
            if blog_id.exists():  # Eğer kayıt varsa güncelle
                blog_id.update(title_blog='NABERRR')
                return True
        except:
            return False



        