from home.models import about
class HakkimizdaPage:
    @staticmethod
    def hakkimizda_sayfasi_ekleme():
        try:
            portfoy_kategori_objects = about.objects.create(
                about_title='dfad',
                about_description='adfasdda',
                about_image='Hakkimizda')
            return True
        except:
            return False
    @staticmethod
    def hakkimizda_sayfasi_guncelle():
        try:
            deger=about.objects.filter(pk=1)
            if deger.exists():
                deger.update(about_title='NABER')
                return True
            else:return False 
        except:
            return 'Değer bulunamadı.'