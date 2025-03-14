import os
import django
import pytest
from home.models import blog,blog_kategori  # Modeli import etmeden önce Django ortamını başlatmalısın
from tests.pages.blog_page import Anasayfa

@pytest.mark.django_db
class Test_Blog_Ekleme:
    def test_yeni_bir_blog_ekleme_islemi_yapiliyor_mu(self):
        naber=Anasayfa()
        assert naber.blog_olustur()==True,"🟥 Hata meydana geldi"
        print('🟩 Blog ekleme işlemi başarılı.')
    
    def test_eklenen_testi_silme(self):
        naber=Anasayfa()
        naber.blog_olustur()
        assert naber.blog_sil()==True,"🟥 Hata meydana geldi"
        print('🟩 Blog silme işlemi')

    def test_eklenen_testi_guncelleme(self):
        naber=Anasayfa()
        naber.blog_olustur()
        assert naber.blog_guncelle()==True
        print('🟩 Blog Güncelleme İşlemi çalışıyor')
