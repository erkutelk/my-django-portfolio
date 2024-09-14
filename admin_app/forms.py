from django import forms # type: ignore
from home.models import blog,menu,blog_kategori,portfoy_project,title,servic,about,contact

class blog_ekle_forms(forms.ModelForm):  
    class Meta:
        model = blog
        fields = ('title_blog', 'description_blog', 'isBlog_blog', 'blog_kategori', 'image','slug') 
        labels = {
            'title_blog': 'Başlık',
            'description_blog': 'Açıklama',
            'isBlog_blog': 'Blog İçeriği',
            'blog_kategori': 'Kategori',
        }
        widgets = {
            'title_blog': forms.TextInput(attrs={"class": 'form-control'}),
            'description_blog': forms.Textarea(attrs={"class": 'form-control'}),
            'isBlog_blog': forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            'blog_kategori': forms.Select(attrs={"class": 'form-control'}),
            'slug':forms.TextInput(attrs={"class": 'form-control', 'readonly': 'readonly'}),  # Make the slug field read-only
        }
        error_messages = {
            'title_blog': {
                'required': 'Başlık gereklidir.',
                'max_length': 'Başlık maksimum 50 karakter olmalıdır.',
            },
            'description_blog': {
                'required': 'Açıklama gereklidir.',
            },
            
            'isBlog_blog':{
            'required':'Lütfen bir durum seçiniz',}
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['blog_kategori'].queryset = blog_kategori.objects.filter(isActive=True)

class Menu_ekle_form(forms.ModelForm):
    class Meta:
        model = menu
        fields = ('title', 'isActive')
        labels = {
            'title': 'Başlık',
            'link': 'Açıklama',
            'isActive': 'Durumu',
        }
        widgets = {
            'title': forms.TextInput(attrs={"class": 'form-control'}),
            'link': forms.TextInput(attrs={"class": 'form-control'}),
            'isActive': forms.CheckboxInput(attrs={"class": 'form-check-input'}),
        }
        error_messages = {
            'title': {
                'required': 'Lütfen geçerli bir menü başlığı giriniz'
            }
        }

class blog_kategori_form(forms.ModelForm):
    class Meta:
        model = blog_kategori
        fields = ('kategori', 'isActive',)
        labels = {
            'kategori': 'Kategori',
            'slug': 'link',
            'isActive': 'Durum'
        }
        widgets = {
            'kategori': forms.TextInput(attrs={"class": 'form-control'}),
            'slug': forms.TextInput(attrs={"class": 'form-control'}),
            'isActive': forms.CheckboxInput(attrs={"class": 'form-check-input'}),
        }
        error_messages = {
            'kategori': {
                'required': 'Kategori Eklenyiniz'
            },
            'slug': {
                'required': 'Lütfen slug değeri giriniz'
            },
        }

class admin_portfoy_form(forms.ModelForm):
    class Meta:
        model = portfoy_project
        fields = ('title','description','isActive','categories','images')
        labels = {
            'title':'Başlık',
            'description':'Açıklama',
            'isActive':'Durum',
            'categories':'Kategori',  
        }
        widgets = {
            'title': forms.TextInput(attrs={"class": 'form-control'}),
            'description' : forms.CharField(widget=forms.Textarea(attrs={"class": 'form-control'})),
            'isActive': forms.CheckboxInput(attrs={"class": 'form-check-input'}),
            'slug':forms.TextInput(attrs={"class": 'form-control','readonly': 'readonly'}),
            'categories':forms.Select(attrs={"class": 'form-control'})
        }
        error_messages = {
            'title': {
                'required': 'Kategori Eklenyiniz'
            },
            'description': {
                'required': 'Lütfen slug değeri giriniz'
            },
        }

class admin_info_form(forms.ModelForm):
    class Meta:  # Corrected from 'meta' to 'Meta'
        model = title
        fields = ('title', 'description', 'linkedin', 'instagram', 'git', 'images')
        labels = {
            'title': 'Başlık',
            'description': 'Açıklama',
            'linkedin': 'Linkedin',
            'instagram': 'Instagram Adresiniz',
            'git': 'Git Hesabınız',
        }
        widgets = {
            'title': forms.TextInput(attrs={"class": 'form-control'}),
            'description': forms.Textarea(attrs={"class": 'form-control'}),
            'linkedin': forms.TextInput(attrs={"class": 'form-control'}),
            'instagram': forms.TextInput(attrs={"class": 'form-control', 'readonly': 'readonly'}),
            'git': forms.TextInput(attrs={"class": 'form-control'}),
        }
        error_messages = {
            'title': {
                'required': 'Lütfen geçerli bir başlık giriniz.'
            },
            'description': {
                'required': 'Lütfen bir açıklama giriniz.'
            },
        }

class admin_servic_form(forms.ModelForm):
    class Meta:
        model = servic
        fields = ('title', 'description', 'isActive')
        labels = {
            'title': 'Başlık',
            'description': 'Açıklama Giriniz',
            'isActive': 'Durum'
        }
        widgets = {
            'title': forms.TextInput(attrs={"class": 'form-control'}),
            'description': forms.TextInput(attrs={"class": 'form-control'}),
            'isActive': forms.CheckboxInput(attrs={"class": 'form-check-input'})
        }
        error_messages = {
            'title': {
                'required': 'Please enter a valid title.'
            },
            'description': {
                'required': 'Please enter a description.'
            }
        }

class admin_about_form(forms.ModelForm):
    class Meta:
        model=about
        fields=('about_title','about_description','about_image')
        labels={
            'about_title':'Title',
            'about_description':'Açıklama Yaz',
            'about_image':'Resim Yaz'
        }
        widgets={
            'about_title': forms.TextInput(attrs={"class": 'form-control'}),
            'about_description': forms.Textarea(attrs={"class": 'form-control'}),
        }
        error_messages={
            'about_title': {
                'required': 'Please enter a valid title.'
            },
            'about_description': {
                'required': 'Please enter a description.'
            }
        }

class admin_contact_form(forms.ModelForm):
    class Meta:
        model=contact
        fields=('title','konum','konum2','telefon','mail')
        labels={
            'title':'Başlık',
            'konum':'Konum',
            'konum2':'konum2',
            'telefon':'Telefon',
            'mail':'mail',
        }
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'konum':forms.TextInput(attrs={'class':'form-control'}),
            'konum2':forms.TextInput(attrs={'class':'form-control'}),
            'telefon':forms.TextInput(attrs={'class':'form-control'}),
            'mail':forms.TextInput(attrs={'class':'form-control'}),
        }
        error_mesages={'title':'lütfen title başlığını doldururunz'}

class UploadForm(forms.Form):
    image = forms.ImageField()
