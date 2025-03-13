from django.http import HttpResponse # type: ignore
from django.shortcuts import render,get_object_or_404,redirect # type: ignore
from home.models import menu,blog,portfoy_kategori,blog_kategori,portfoy_project,title,servic,about,contact
from ..forms import Menu_ekle_form
from django.template.defaultfilters import slugify # type: ignore
from django.shortcuts import render, get_object_or_404, redirect
from home.models import title
from django.contrib import messages
class Admin_Menu:
    @staticmethod
    def admin_page_funcation(request):
        return render(request, 'admin_app/admin_layout.html')

    @staticmethod
    def navbar_ekle_funcation(request):
        manu = menu.objects.all()
        if request.method == 'POST':
            menu_values = Menu_ekle_form(request.POST)
            if menu_values.is_valid(): 
                menu_values.save()
        else:
            menu_values = Menu_ekle_form()
        return render(request, 'admin_app/pages/_menu/navbar-ekle.html', {'menu_form': menu_values, 'menü': manu})

    @staticmethod
    def navbar_sil(request, id):
        menu_delete_object = get_object_or_404(menu, pk=id)
        if request.method == 'POST':
            menu_delete_object.delete()
            print('Silme işlemi başarıyla gerçekleşti')
            return redirect('navbar_ekle')
        return render(request, 'admin_app/pages/_menu/menu_sil.html', {'menu_objects': menu_delete_object})

    @staticmethod
    def navbar_düzenle(request, id):
        menu_düzenle = get_object_or_404(menu, pk=id)
        if request.method == 'POST':
            form = Menu_ekle_form(request.POST, instance=menu_düzenle)
            if form.is_valid():
                form.instance.link = slugify(form.cleaned_data['title'])
                form.save()
                return redirect('navbar_ekle')
        else:
            form = Menu_ekle_form(instance=menu_düzenle)
        return render(request, 'admin_app/pages/_menu/menu_düzenle.html', {'menu_form': form})
