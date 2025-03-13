from django.http import HttpResponse # type: ignore
from django.shortcuts import render,get_object_or_404,redirect # type: ignore
from home.models import menu,blog,portfoy_kategori,blog_kategori,portfoy_project,title,servic,about,contact
from ..forms import admin_portfoy_form
from django.template.defaultfilters import slugify # type: ignore
from django.shortcuts import render, get_object_or_404, redirect
from home.models import title
from django.contrib import messages
class admin_portfoy:
    @staticmethod
    def ekle(request):
        if request.method=='POST':
            portfoy_objects=admin_portfoy_form(request.POST, request.FILES)
            if portfoy_objects.is_valid():
                portfoy_objects.save()
        else:
            portfoy_objects=admin_portfoy_form()
        return render(request,'admin_app/pages/_portfoy/portfoy_ekle.html',{'form':portfoy_objects})
    @staticmethod
    def tablo(request):
        portfoy_all=portfoy_project.objects.all()
        return render(request,'admin_app/pages/_portfoy/portfoy_tablo.html',{'portfoy_all':portfoy_all})
    @staticmethod
    def sil(request,id):
        portfoy_delete_id=get_object_or_404(portfoy_project,id=id)
        if request.method=='POST':
            portfoy_delete_id.delete()
            return redirect('protfoy_all')
        return render(request,'admin_app/pages/_portfoy/portfoy_sil.html',{'portfoy_sil':portfoy_delete_id})
    @staticmethod
    def guncelle(request,id):
        admin_portfoy_form_object = get_object_or_404(portfoy_project, pk=id)
        if request.method=='POST':
            form = admin_portfoy_form(request.POST,request.FILES, instance=admin_portfoy_form_object)
            if form.is_valid():
                form.instance.slug = slugify(form.cleaned_data['title'])
                form.save()
                return redirect('protfoy_all')
        else:
            form = admin_portfoy_form(instance=admin_portfoy_form_object)
        return render(request, 'admin_app/pages/_portfoy/portfoy_guncelle.html', {'form': form})
