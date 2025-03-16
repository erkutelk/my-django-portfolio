from home.models import portfoy_project,portfoy_kategori
class test_portfoy:
    @staticmethod
    def portfoy_ekle():
        try:
            portfoy_kategori_objects = portfoy_kategori.objects.create(
                kategori='isim-naber',
                isActive=True
            )

            portfoy_objects = portfoy_project.objects.create(
                title='erkut',
                description='isim',
                images='isim',
                isActive=True,
                date='2025-03-14',
                slug='yiopo',
                categories=portfoy_kategori_objects
            )
            return True 
        except:
            return False

    @staticmethod
    def portfoy_sil():
        try:
            deger=portfoy_project.objects.get(pk=1)
            deger.delete()
            return True
        except:
            return False
        
    @staticmethod
    def portfoy_guncelle():
        deger=portfoy_project.objects.filter(pk=1)
        if deger.exists():
            deger.update(title='NABER')
            return True
        else:return False 





