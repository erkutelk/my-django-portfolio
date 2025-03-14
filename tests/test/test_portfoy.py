import pytest
from tests.pages.portfoy_page import test_portfoy

@pytest.mark.django_db
class Test_portfoy:
    def test_yeni_bir_portfoy_olusuruyor_mu(self):
        portfoy_project=test_portfoy()
        assert portfoy_project.portfoy_ekle() == True
        print('🟩 Portfoy ekleme işlemi yapıldı.')

    def test_yeni_eklenen_degeri_silme(self):
        portfoy_project=test_portfoy()
        portfoy_project.portfoy_ekle()
        assert portfoy_project.portfoy_sil()==True
        print('🟩 Portfoy silme işlemi yapıldı')

    def test_guncelleme_islemi_yapildi(self):
        portfoy_project=test_portfoy()
        portfoy_project.portfoy_ekle()
        portfoy_project.portfoy_guncelle()