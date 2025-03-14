import pytest
from django.urls import reverse

url_dict = {
    'admin_page': {},
    'navbar_ekle': {},
    'blog_ekle': {},
    'blog_all': {},
    'Admin_kategori_ekle': {},
    'portfoy': {},
    'protfoy_all': {},
    'servis_ekle': {},
    'contactGuncelle': {}
}

@pytest.mark.django_db
@pytest.mark.parametrize("deger, params", url_dict.items())
def test_index_view(client, deger, params):  
    url = reverse(deger, kwargs=params) if params else reverse(deger)
    response = client.get(url)
    
    if response.status_code == 404:
        print(f"URL {url} bulunamadı.")
    
    assert response.status_code == 200
    print(f'🟩 URL= {url} Sayfa Açıldı')
