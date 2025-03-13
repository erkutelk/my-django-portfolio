from django.http import HttpResponse # type: ignore
from django.shortcuts import render,get_object_or_404,redirect # type: ignore
from home.models import menu,blog,portfoy_kategori,blog_kategori,portfoy_project,title,servic,about,contact
from ..forms import admin_contact_form
from django.template.defaultfilters import slugify # type: ignore
from django.shortcuts import render, get_object_or_404, redirect
from home.models import title
from django.contrib import messages

class admin_contact():
    @staticmethod
    def guncelle(request):
        admin_contact_objects = contact.objects.first()
        
        if request.method == 'POST':
            if admin_contact_objects:
                form = admin_contact_form(request.POST, instance=admin_contact_objects)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Bilgiler başarıyla güncellendi.")  
                    return redirect('contactGuncelle')
                else:
                    messages.error(request, "Hata verdi, lütfen tekrar deneyiniz...")
            else:
                form = admin_contact_form(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Bilgiler başarıyla eklendi.")
                    return redirect('contactGuncelle')
                else:
                    messages.error(request, "Hata verdi, lütfen tekrar deneyiniz...")
        else:
            form = admin_contact_form(instance=admin_contact_objects)
        
        return render(request, 'admin_app/pages/_contact/contact.html', {'form': form,})
