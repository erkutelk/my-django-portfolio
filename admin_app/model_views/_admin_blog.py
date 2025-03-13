from django.http import HttpResponse # type: ignore
from django.shortcuts import render,get_object_or_404,redirect # type: ignore
from home.models import menu,blog,portfoy_kategori,blog_kategori,portfoy_project,title,servic,about,contact
from ..forms import blog_ekle_forms
from django.template.defaultfilters import slugify # type: ignore
from django.shortcuts import render, get_object_or_404, redirect
from home.models import title
from django.contrib import messages
class Admin_Blog:
    @staticmethod
    def blog_ekle(request):
        if request.method == 'POST':
            blog_form = blog_ekle_forms(request.POST, request.FILES)
            if blog_form.is_valid():
                blog_form.save()
                messages.success(request, "Blog Başarıyla Eklendi")

        else:
            blog_form = blog_ekle_forms()

        return render(request, 'admin_app/pages/_blog/blog-ekle.html', {'form': blog_form})
    
    @staticmethod
    def blog_edit(request,id):
        blog_Edit=get_object_or_404(blog,pk=id)
        if request.method=='POST':
            form=blog_ekle_forms(request.POST,request.FILES,instance=blog_Edit)
            if form.is_valid():
                form.instance.slug = slugify(form.cleaned_data['title_blog'])

                form.save()
                return redirect('blog_all')
        else:
            form=blog_ekle_forms(instance=blog_Edit)

        return render(request,'admin_app/pages/_blog/blog-düzenle-sayfası.html',{'form':form})
    
    @staticmethod
    def blog_sil(request, id):
        blog_edit = get_object_or_404(blog, pk=id)
        if request.method == 'POST':
            blog_edit.delete()
            print('silme işlemi yapıldı')
            return redirect('blog_all')
        
        return render(request, 'admin_app/pages/_blog/blog-sil.html', {'blog': blog_edit})
    
    @staticmethod
    def blog_all(request):
        blog_all_fucation=blog.objects.all()
        return render(request,'admin_app/pages/_blog/kurs-listesi.html',{'blog_all':blog_all_fucation})
