import pytest
from tests.pages.info_page import site_baslangic
class Test_info():
    def test_info_basariyla_ekleniyor_mu(self):
        isim=site_baslangic()
        assert isim.ekle()==True
        print('🟩 Info başarıyla eklendi')

    def test_info_basariyla_güncelleniyor_mu(self):
        isim=site_baslangic()
        isim.ekle()
        assert isim.guncelle()
        print('🟩 İnfo Başarıyla güncelleniyor')