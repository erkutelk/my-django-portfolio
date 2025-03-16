import pytest
from home.models import title

class site_baslangic:
    @staticmethod
    def ekle():
        try:
            title_object=title.objects.create(
            title='deger',
            description='deger',
            linkedin='deger',
            instagram='deger',
            git='deger',
            images='deger')
            return True
        except:
            return False

    
    @staticmethod
    def guncelle():
        try:
            isim = title.objects.filter(pk=1).first()
            if isim:
                isim.title = 'test1'
                isim.description = 'isim'
                isim.linkedin = 'test'
                isim.instagram = 'test1'
                isim.git = 'test1'
                isim.images = 'test1'
                isim.save()
                return True
            else:
                print("⚠️ Güncellenecek kayıt bulunamadı!")  # Debug mesajı
                return False
        except Exception as e:
            print(f"❌ Hata oluştu: {e}")  # Hata mesajını yazdır
            return False


