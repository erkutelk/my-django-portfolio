from django.http import HttpResponse # type: ignore
from django.shortcuts import render,get_object_or_404,redirect # type: ignore
from home.models import menu,blog,portfoy_kategori,blog_kategori,portfoy_project,title,servic,about,contact
from ..forms import admin_servic_form
from django.template.defaultfilters import slugify # type: ignore
from django.shortcuts import render, get_object_or_404, redirect
from home.models import title
from django.contrib import messages
class admin_servic:
    @staticmethod
    def ekle(request):
        servis_object_all=servic.objects.all()
        if request.method=='POST':
            form=admin_servic_form(request.POST)
            if form.is_valid():
                form.save()
        
        else:
            form=admin_servic_form()
        return render(request,'admin_app/pages/_servic/servis_ekle.html',{'form':form,'value':servis_object_all})

    @staticmethod
    def guncelle(request,id):
        servic_object=get_object_or_404(servic,pk=id)
        if request.method=='POST':
            form=admin_servic_form(request.POST,instance=servic_object)
            if form.is_valid():
                form.save()
                return redirect('servis_ekle')
        else:
            form = admin_servic_form(instance=servic_object)
        
        return render(request, 'admin_app/pages/_servic/servis_guncelle.html', {'form': form})

    @staticmethod
    def sil(request,id):
        servis_objects_delete_id=get_object_or_404(servic,pk=id)
        if request.method=='POST':
            servis_objects_delete_id.delete()
            return redirect('servis_ekle')
        
        return render(request,'admin_app/pages/_servic/servis_sil.html',{'servis_sil':servis_objects_delete_id})
