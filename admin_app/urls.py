from django.urls import path # type: ignore
from admin_app.model_views import (
_admin_about, 
_admin_blog, 
_admin_blog_kategori, 
_admin_contact, 
_admin_info,
_admin_menu, 
_admin_portfoy, 
_admin_servic
)

urlpatterns = [
    #* menu
    path('yonetim', _admin_menu.Admin_Menu.admin_page_funcation, name='admin_page'),
    path('yonetim/navbar_ekle', _admin_menu.Admin_Menu.navbar_ekle_funcation, name='navbar_ekle'),
    path('yonetim/navbar_sil/<int:id>', _admin_menu.Admin_Menu.navbar_sil, name='navbar_sil'),
    path('yonetim/navbar_düzenle/<int:id>', _admin_menu.Admin_Menu.navbar_düzenle, name='navbar_düzenle'),

    #? Blog
    path('yonetim/blog_ekle', _admin_blog.Admin_Blog.blog_ekle, name='blog_ekle'),
    path('yonetim/blog_all', _admin_blog.Admin_Blog.blog_all, name='blog_all'),
    path('yonetim/<int:id>', _admin_blog.Admin_Blog.blog_edit, name='guncelleBlog'),
    path('yonetim/sil/<int:id>', _admin_blog.Admin_Blog.blog_sil, name='sil_blog'),
    
    #!Blog_Kategori
    path('yonetim/blog_kategori/', _admin_blog_kategori.Admin_Blog_Kategori.ekle, name='Admin_kategori_ekle'),
    path('yonetim/blog_kategori/guncelle/<int:id>', _admin_blog_kategori.Admin_Blog_Kategori.guncelle, name='Admin_kategori_guncelle'),
    path('yonetim/blog_kategori/sil/<int:id>', _admin_blog_kategori.Admin_Blog_Kategori.sil, name='Admin_kategori_sil'),

    #*Portfoy
    path('yonetim/protfoy/portfoy-ekle', _admin_portfoy.admin_portfoy.ekle, name='portfoy'),
    path('yonetim/protfoy_all', _admin_portfoy.admin_portfoy.tablo, name='protfoy_all'),
    path('yonetim/protfoy_sil/<int:id>', _admin_portfoy.admin_portfoy.sil, name='portfoy_sil'),
    path('yonetim/portfoy_guncelle/<int:id>', _admin_portfoy.admin_portfoy.guncelle, name='portfoy_guncelle'),

    #?Admin İnfo
    path('yonetim/admin_info/page', _admin_info.Admin_info.guncelle, name='info_guncelle'),

    #! Servis İşlemleri
    path('yonetim/servis_ekle', _admin_servic.admin_servic.ekle, name='servis_ekle'),
    path('yonetim/servis_guncelle/<int:id>', _admin_servic.admin_servic.guncelle, name='servis_guncelle'),
    path('yonetim/servis_sil/<int:id>', _admin_servic.admin_servic.sil, name='servis_sil'),

    #* About
    path('yonetim/about_page', _admin_about.admin_about.guncelle, name='about_update'),

    #? Contact
    path('yonetim/contact', _admin_contact.admin_contact.guncelle, name='contactGuncelle')
]
