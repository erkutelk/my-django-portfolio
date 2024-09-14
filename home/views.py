from django.http import HttpResponse # type: ignore
from django.shortcuts import render # type: ignore
from .models import title  # Corrected import
from .models import about as hakkimda  # Corrected import
from .models import servic as servisCard_
from .models import menu as menuler
from .models import blog as blog_page
from .models import contact as iletisim
from .models import portfoy_kategori as pr_kategori
from .models import portfoy_project 
from .models import blog_kategori
def home_(request):
    portfoy_project_count = pr_kategori.objects.annotate(portfoy_project_count=Count('portfoy_project'))#Protfoy ile portfoy kategori arasındaki değerleri birbirine bağlıyor ve bir kaategoride kaç adet proje olduğunu bu şekilde görüyoruz.

    value=title.objects.all()
    bolum_hakkimda=hakkimda.objects.all()
    servis=servisCard_.objects.all()
    menuValue = menuler.objects.filter(isActive=True)
    blog=blog_page.objects.filter(isBlog_blog=True)
    contact=iletisim.objects.all()
    portfoy_kategori=pr_kategori.objects.all()
    portfoy_projeler=portfoy_project.objects.filter(isActive=True)
    blog_kategoriler=blog_kategori.objects.filter(isActive=True)
    portfoy_kategori=pr_kategori.objects.all()
    portfoy_adet=zip(portfoy_project_count,portfoy_kategori)
    portfoy_toplam=portfoy_project.objects.all().count()



    return render(request, 
        'home/home.html',{
        'site_baslangic':value,
        'bolum_hakkimda':bolum_hakkimda,
        'value':servis,
        'menu':menuValue,
        'blog':blog,
        'contact':contact,
        'portfoy_kategori':portfoy_kategori,
        'blog_kategoriler':blog_kategoriler,
        'portfoy_projeler':portfoy_projeler,
        'portfoy_adet':portfoy_adet,
        'Portfoy_toplam':portfoy_toplam})


def about(request):
    return HttpResponse('<h1>about page</h1>')

from django.db.models import Count # type: ignore

def detay(request,slug):
    blog_detay=blog_page.objects.filter(slug=slug)
    blog_kategori_all=blog_kategori.objects.all()

    categories_with_blog_counts = blog_kategori.objects.annotate(blog_count=Count('blog'))
    allop=zip(blog_kategori_all,categories_with_blog_counts)
    return render(request,'home/blog_detay.html',{'blog_detay_slug':blog_detay,
                                                  'blog_kategori':categories_with_blog_counts,
                                                  'allop':allop})



   

