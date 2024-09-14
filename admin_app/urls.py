from django.urls import path # type: ignore
from .views import Admin_Menu,Admin_Blog,Admin_Blog_Kategori,admin_portfoy,Admin_info,admin_servic,admin_about,admin_contact

urlpatterns = [
    #* menu
    path('yonetim', Admin_Menu.admin_page_funcation),
    path('yonetim/navbar_ekle', Admin_Menu.navbar_ekle_funcation, name='navbar_ekle'),
    path('yonetim/navbar_sil/<int:id>', Admin_Menu.navbar_sil, name='navbar_sil'),
    path('yonetim/navbar_düzenle/<int:id>', Admin_Menu.navbar_düzenle, name='navbar_düzenle'),

    #? Blog
    # path('', info_guncelle, name='infoGuncelle'),
    path('yonetim/blog_ekle', Admin_Blog.blog_ekle, name='blog_ekle'),
    path('yonetim/blog_all', Admin_Blog.blog_all, name='blog_all'),
    path('yonetim/<int:id>', Admin_Blog.blog_edit, name='guncelleBlog'),
    path('yonetim/sil/<int:id>', Admin_Blog.blog_sil, name='sil_blog'),
    
    #!Blog_Kategori
    path('yonetim/blog_ketegori/', Admin_Blog_Kategori.ekle, name='Admin_kategori_ekle'),
    path('yonetim/blog_ketegori/guncelle/<int:id>', Admin_Blog_Kategori.guncelle, name='Admin_kateogri_guncelle'),
    path('yonetim/blog_ketegori/sil/<int:id>', Admin_Blog_Kategori.sil, name='Admin_kateogri_sil'),

    #*Portfoy
    path('yonetim/protfoy/portfoy-ekle',admin_portfoy.ekle,name='portfoy'),
    path('yonetim/protfoy_all',admin_portfoy.tablo,name='protfoy_all'),
    path('yonetim/protfoy_sil/<int:id>',admin_portfoy.sil,name='portfoy_sil'),
    path('yonetim/portfoy_guncelle/<int:id>',admin_portfoy.guncelle,name='portfoy_guncelle'),

    #?Admin İnfo
    path('yonetim/admin_info/page', Admin_info.guncelle, name='info_guncelle'),

    #! Servis İşlemleri
    path('yonetim/servis_ekle',admin_servic.ekle,name='servis_ekle'),
    path('yonetim/servis_guncelle/<int:id>',admin_servic.guncelle,name='servis_guncelle'),
    path('yonetim/servis_sil/<int:id>',admin_servic.sil,name='servis_sil'),

    #*
    path('yonetim/about_page',admin_about.guncelle,name='about_update'),

    #?Contact
    path('yonetim/contact',admin_contact.guncelle,name='contactGuncelle')



]
