import pytest
from admin_app.forms import blog_kategori_form,admin_info_form,admin_contact_form,admin_servic_form
from home.models import portfoy_kategori
from django.core.files.uploadedfile import SimpleUploadedFile
from admin_app.forms import admin_info_form
def test_blog_kategori_form_ile_ekleme():
    form_data={'kategori':'Aslinur','slug':'kalem','isActive':True}
    form=blog_kategori_form(data=form_data)
    assert form.is_valid(),'Eklenen değerler gönderilen dosya formatına uygun değil.'
    print(f'🟩 Kullanıcı blog kategori eklendi.{form.cleaned_data}')


def test_form_ile_info_sayfasini_guncelleme():
    with open(r"C:\Users\erkut\my-django-portfolio\uploads\images\Python_5.png", "rb") as img:
        image_file = SimpleUploadedFile("Python_5.png", img.read(), content_type="image/png")
        #SimpleUploadedFile dosya yüklemek için kullanmamız gereken yardımcı sınıftır.
    form = admin_info_form(data={'title': 'Erkut-Elik','description': 'Erkut-Elik','linkedin': 'Erkut-Elik','instagram': 'Erkut-Elik','git': 'Erkut-Elik',
    }, files={'images': image_file})

    assert form.is_valid(), form.errors

    # Başarı mesajı
    print("🟩 Test başarılı: Dosya ve veriler forma eklendi.")

def test_contact_güncelleme():
    form_data = {'title': 'Kalem', 'konum': 'Konum', 'konum2': 'Konum2', 'telefon': '11111111111', 'mail': 'test@gmail.com'}
    contact_object=admin_contact_form(data=form_data)
    assert contact_object.is_valid()
    print(f'🟩 İletişim sayfsı sorunsuz bir şekilde çalışıyor{contact_object.cleaned_data}')

def test_servis_guncelleme():
    form_data={'title':'Naber','description':'Naber','isActive':True}
    form=admin_servic_form(data=form_data)
    assert form.is_valid()
    print(f'Servis güncelleme işlemleri yapıldı.')