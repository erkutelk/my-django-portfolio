import pytest
from django.urls import reverse

Deger = [
    ('admin_page', 'Yönetim Paneli', 'Çıkış'),
    ('navbar_ekle', 'Navigasyon Ekle', 'Başlık'),
    ('blog_ekle', 'Blog Yazısı Ekle', 'Başlık'),
    ('Admin_kategori_ekle', 'Kategori Ekle', 'Kategori'),
    ('portfoy', 'Portföy Listesi', 'Açıklama'),
    ('servis_ekle', 'Servis Ekle', 'Açıklama Giriniz'),
    ('contactGuncelle', 'İletişim Güncelle', 'Telefon'),
]

@pytest.mark.django_db
@pytest.mark.parametrize("url_adi, sayfa_basligi, arama_kelimesi", Deger)
def test_page_template(client, url_adi, sayfa_basligi, arama_kelimesi):
    url = reverse(url_adi)
    response = client.get(url)
    assert response.status_code == 200, f"{url_adi} sayfası açılmadı! (Hata Kodu: {response.status_code})"
    print(f'🟩 URL {url} açıldı')
    assert "text/html" in response.headers.get("Content-Type", ""), f"{url_adi} sayfası HTML değil!"
    assert arama_kelimesi in response.content.decode("utf-8"), f"{url_adi} sayfasında '{arama_kelimesi}' bulunamadı!"
