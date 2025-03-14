import pytest
from home.models import contact
from tests.pages.iletisim_page import IletisimPage
from django.urls import reverse


class TestIletisim:
    def test_iletisim_sayfasi_ekleme_ve_guncelleme(self):
        iletisim_page_object = IletisimPage()
        assert iletisim_page_object.iletisim_page_deger_girme() == True, 'Hata veriyor'
        print('🟩 İletişim verisi eklendi')

    def test_iletisim_sayfasi_guncelleme(self):
        iletisim_page_object = IletisimPage()
        iletisim_page_object.iletisim_page_deger_girme()
        assert iletisim_page_object.iletisim_page_guncelleme() == True, 'Hata veriyor'
        print('🟩 İletişim değeri güncellendi')



