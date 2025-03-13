from django.http import HttpResponse # type: ignore
from django.shortcuts import render,get_object_or_404,redirect # type: ignore
from home.models import menu,blog,portfoy_kategori,blog_kategori,portfoy_project,title,servic,about,contact
from ..forms import admin_info_form
from django.template.defaultfilters import slugify # type: ignore
from django.shortcuts import render, get_object_or_404, redirect
from home.models import title
from django.contrib import messages
class Admin_info:
    def guncelle(request):
        admin_info_first_item = title.objects.first()

        if request.method == 'POST':
            form = admin_info_form(request.POST, request.FILES, instance=admin_info_first_item)
            if form.is_valid():
                form.save()
                return redirect('info_guncelle')
            else:
                print("Form errors:", form.errors)
        else:
            if admin_info_first_item:
                form = admin_info_form(instance=admin_info_first_item)
            else:
                form = admin_info_form()

        return render(request, 'admin_app/pages/_info/admin_info.html', {'form': form})
