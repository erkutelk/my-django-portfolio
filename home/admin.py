from django.contrib import admin # type: ignore
from .models import about,blog,contact,menu,portfoy_kategori,servic,title,portfoy_project,blog_kategori
@admin.register(about)
class about_admin(admin.ModelAdmin):
    list_display=("about_title","about_description","about_image")

@admin.register(servic)
class servic_admin(admin.ModelAdmin):
    list_display=("title","description","isActive")

@admin.register(menu)
class menu_admin(admin.ModelAdmin):
    list_display=("title","link","isActive")

@admin.register(blog)
class admin_blog(admin.ModelAdmin):
    list_display = ("title_blog", "description_blog", "isBlog_blog","blog_kategori","image")

@admin.register(blog_kategori)
class blog_kategori_admin(admin.ModelAdmin):
    list_display = ("slug", "isActive", 'kategori')


@admin.register(portfoy_project)
class admin_portfoy_kategori(admin.ModelAdmin):
    list_display=("title","description","images","isActive","date","slug")

@admin.register(title)
class admin_title(admin.ModelAdmin):
    list_display=("title","description","linkedin","instagram","git","images")

@admin.register(portfoy_kategori)
class admin_portfoy_kategori(admin.ModelAdmin):
    list_display=("kategori","isActive")

@admin.register(contact)
class admin_contact(admin.ModelAdmin):
    list_display=("title","konum","konum2",'telefon','mail')

