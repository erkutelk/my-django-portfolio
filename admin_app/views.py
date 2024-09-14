from django.http import HttpResponse # type: ignore
from django.shortcuts import render,get_object_or_404,redirect # type: ignore
from home.models import menu,blog,portfoy_kategori,blog_kategori,portfoy_project,title,servic,about,contact
from .forms import blog_ekle_forms,UploadForm,Menu_ekle_form,blog_kategori_form,admin_portfoy_form,admin_info_form,admin_servic_form,admin_about_form,admin_contact_form
from django.template.defaultfilters import slugify # type: ignore


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

class Admin_Blog:
    @staticmethod
    def blog_ekle(request):
        if request.method == 'POST':
            blog_form = blog_ekle_forms(request.POST, request.FILES)
            if blog_form.is_valid():
                blog_form.save()
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

        return render(request, 'admin_app/pages/_blog_kategori/blog_kategori.html', {'form': blog_kategori_objects,
                                                                      'menü':manu})

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

class Admin_info:
    @staticmethod
    def guncelle(request):
        admin_info_edit = get_object_or_404(title, pk=1)
        if request.method == 'POST':
            form = admin_info_form(request.POST, request.FILES, instance=admin_info_edit)
            if form.is_valid():
                form.save()
                return redirect('info_guncelle')
            else:
                print("Form errors:", form.errors)
        else:
            form = admin_info_form(instance=admin_info_edit)

        return render(request, 'admin_app/pages/_info/admin_info.html', {'form': form})
    
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

from django.contrib import messages

class admin_contact():
    @staticmethod
    def guncelle(request):
        admin_contact_objects = get_object_or_404(contact, pk=1)
        
        if request.method == 'POST':
            form = admin_contact_form(request.POST, instance=admin_contact_objects)
            if form.is_valid():
                form.save()
                messages.success(request, "Bilgiler başarıyla güncellendi.")  
                return redirect('contactGuncelle')  # redirect sonrası mesaj saklanır
            else:
                messages.error(request, "Hata verdi, lütfen tekrar deneyiniz...")  # Hata mesajı
        else:
            form = admin_contact_form(instance=admin_contact_objects)
        
        return render(request, 'admin_app/pages/_contact/contact.html', {
            'form': form,
        })




def admin_page_funcation(request):
    return render(request,'admin_app/admin_layout.html')

def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  
            return redirect('some_success_url')
    else:
        form = UploadForm()
    return render(request, 'upload_template.html', {'form': form})
    
# def info_guncelle(request):
#     return redirect('')