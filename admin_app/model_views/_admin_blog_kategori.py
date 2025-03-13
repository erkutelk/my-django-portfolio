from django.http import HttpResponse # type: ignore
from django.shortcuts import render,get_object_or_404,redirect # type: ignore
from home.models import menu,blog,portfoy_kategori,blog_kategori,portfoy_project,title,servic,about,contact
from ..forms import blog_kategori_form
from django.template.defaultfilters import slugify # type: ignore
from django.shortcuts import render, get_object_or_404, redirect
from home.models import title
from django.contrib import messages

class Admin_Blog_Kategori:
    @staticmethod
    def ekle(request):
        manu = blog_kategori.objects.all()

        if request.method == 'POST':
            blog_kategori_objects = blog_kategori_form(request.POST)
            if blog_kategori_objects.is_valid():
                blog_kategori_objects.save()
                return redirect('Admin_kategori_ekle') 
        else:
            blog_kategori_objects = blog_kategori_form()

        return render(request, 'admin_app/pages/_blog_kategori/blog_kategori.html', {'form': blog_kategori_objects,'menü':manu})

    @staticmethod
    def guncelle(request, id):
        kategori_edit = get_object_or_404(blog_kategori, pk=id)
        if request.method == 'POST':
            form = blog_kategori_form(request.POST, instance=kategori_edit)
            if form.is_valid():
                form.instance.slug = slugify(form.cleaned_data['kategori'])
                form.save()
                return redirect('Admin_kategori_ekle')
        else:
            form = blog_kategori_form(instance=kategori_edit)
        return render(request, 'admin_app/pages/_blog_kategori/blog_kategori_guncelle.html', {'form': form})
    
    @staticmethod
    def sil(request,id):
        blogKategori=get_object_or_404(blog_kategori,pk=id)
        if request.method=='POST':
            blogKategori.delete()
            return redirect('Admin_kategori_ekle')
        return render(request, 'admin_app/pages/_blog_kategori/blog_kategori_sil.html', {'menu_objects': blogKategori})
