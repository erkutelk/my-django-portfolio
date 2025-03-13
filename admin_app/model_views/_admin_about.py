from django.http import HttpResponse # type: ignore
from django.shortcuts import render,get_object_or_404,redirect # type: ignore
from home.models import menu,blog,portfoy_kategori,blog_kategori,portfoy_project,title,servic,about,contact
from ..forms import admin_about_form
from django.template.defaultfilters import slugify # type: ignore
from django.shortcuts import render, get_object_or_404, redirect
from home.models import title
from django.contrib import messages
class admin_about():
    @staticmethod
    def guncelle(request):
        admin_about=get_object_or_404(about,pk=1)
        if request.method=='POST':
            form=admin_about_form(request.POST,request.FILES,instance=admin_about)
            if form.is_valid():
                form.save()
                return redirect('about_update')
            else:
                print('Hata verdi')
        else:
            form=admin_about_form(instance=admin_about)
        return render(request, 'admin_app/pages/_about/html.html', {'form': form})
