import pytest
from django.urls import reverse, resolve
from admin_app.model_views import (
    _admin_about, _admin_blog, _admin_blog_kategori, _admin_contact, _admin_info,
    _admin_menu, _admin_portfoy, _admin_servic
)
from tests.pages.blog_page import Anasayfa
from tests.pages.portfoy_page import test_portfoy
from tests.pages.hakkimizda_page import HakkimizdaPage
from tests.pages.iletisim_page import IletisimPage
from home.views import home_
from home.views import detay

import pytest
from django.urls import reverse, resolve

@pytest.mark.django_db  
@pytest.mark.parametrize("url_name, kwargs", [
    ('admin_page', {}),
    ('navbar_ekle', {}),
    ('navbar_sil', {"id": 1}),
    ('navbar_düzenle', {"id": 1}),
    ('blog_ekle', {}),
    ('blog_all', {}),
    ('guncelleBlog', {"id": 1}),
    ('sil_blog', {"id": 1}),
    ('Admin_kategori_ekle', {}),
    ('Admin_kategori_guncelle', {"id": 1}),
    ('Admin_kategori_sil', {"id": 1}),
    ('portfoy', {}),
    ('protfoy_all', {}),
    ('portfoy_sil', {"id": 1}),
    ('portfoy_guncelle', {"id": 1}),
    ('info_guncelle', {"id": 1}),
    ('servis_ekle', {}),
    ('servis_guncelle', {"id": 1}),
    ('servis_sil', {"id": 1}),
    ('about_update', {}),
    ('contactGuncelle', {}),
    ('anasayfa', {}),
    ('detay',{"slug":"Test"})
])
def test_url_resolves_correctly(url_name, kwargs):
    path = reverse(url_name, kwargs=kwargs)
    resolved_func = resolve(path).func

    expected_funcs = {
        'anasayfa':home_,
        'detay':detay,
        'admin_page': _admin_menu.Admin_Menu.admin_page_funcation,
        'navbar_ekle': _admin_menu.Admin_Menu.navbar_ekle_funcation,
        'navbar_sil': _admin_menu.Admin_Menu.navbar_sil,
        'navbar_düzenle': _admin_menu.Admin_Menu.navbar_düzenle,
        'blog_ekle': _admin_blog.Admin_Blog.blog_ekle,
        'blog_all': _admin_blog.Admin_Blog.blog_all,
        'guncelleBlog': _admin_blog.Admin_Blog.blog_edit,
        'sil_blog': _admin_blog.Admin_Blog.blog_sil,
        'Admin_kategori_ekle': _admin_blog_kategori.Admin_Blog_Kategori.ekle,
        'Admin_kategori_guncelle': _admin_blog_kategori.Admin_Blog_Kategori.guncelle,
        'Admin_kategori_sil': _admin_blog_kategori.Admin_Blog_Kategori.sil,
        'portfoy': _admin_portfoy.admin_portfoy.ekle,
        'protfoy_all': _admin_portfoy.admin_portfoy.tablo,
        'portfoy_sil': _admin_portfoy.admin_portfoy.sil,
        'portfoy_guncelle': _admin_portfoy.admin_portfoy.guncelle,
        'info_guncelle': _admin_info.Admin_info.guncelle,
        'servis_ekle': _admin_servic.admin_servic.ekle,
        'servis_guncelle': _admin_servic.admin_servic.guncelle,
        'servis_sil': _admin_servic.admin_servic.sil, 
        'about_update': _admin_about.admin_about.guncelle,
        'contactGuncelle': _admin_contact.admin_contact.guncelle,}

    assert url_name in expected_funcs, f"{url_name} için beklenen fonksiyon bulunamadı"
    
    expected_func = expected_funcs[url_name]
    
    assert resolved_func == expected_func, f"{url_name} yanlış view fonksiyonuna yönleniyor"


