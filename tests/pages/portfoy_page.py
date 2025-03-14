from home.models import portfoy_project,portfoy_kategori
class Portfoy:
    @staticmethod
    def portfoy_ekle():
        portfoy_kategori_objects=portfoy_kategori.objects.create(kategori='isim',slug='isim',isActive=True)
        portfoy_objects=portfoy_project.objects.create(title='erkut',description='isim',images='isim',isActive=True,date='isim',slug='isim',categories=1)