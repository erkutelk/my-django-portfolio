from home.models import contact 

class IletisimPage:
    @staticmethod
    def iletisim_page_deger_girme():
        try:
            contact.objects.create(
                title='baslik-test',
                konum='baslik-test',
                konum2='baslik-test',
                telefon='11111111111',
                mail='erkutelik@gmail.com'
            )
            return True
        except Exception as e:
            return False  
    
    @staticmethod
    def iletisim_page_guncelleme():
        deger = contact.objects.filter(pk=1)
        if deger.exists():
            deger.update(
                title='test_erkut',
                konum='test_erkut',
                konum2='test_erkut',
                telefon='11111111111',
                mail='test_erkut@gmail.com'
            )
            return True
        return False
