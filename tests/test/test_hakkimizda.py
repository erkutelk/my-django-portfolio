import pytest
from tests.pages.hakkimizda_page import HakkimizdaPage

@pytest.mark.django_db
class TestHakkimizda:
    def test_hakkimizda_sayfasi_ekleme(self):
        deger = HakkimizdaPage()
        assert deger.hakkimizda_sayfasi_ekleme() == True,'🟥 Değer bulunamadı'
        print('🟩 Hakkimizda Ekleme işlemi yapıldı')

    def test_hakkimizda_sayfasi_guncelleme(self):
        deger=HakkimizdaPage()
        deger.hakkimizda_sayfasi_ekleme()
        assert deger.hakkimizda_sayfasi_guncelle()==True,'🟥 Değer bulunamadı.'
        print('🟩 Hakkimizda güncelleme işlemi yapıldı')

