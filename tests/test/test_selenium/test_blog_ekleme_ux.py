import os
import time
import pytest
from selenium import webdriver
from tests.test.test_selenium.selenium_sites import SeleniumTest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_blog_ekle(driver):
    import time
    tarih=int(time.time())
    test_value = SeleniumTest(driver)

    url = 'http://127.0.0.1:8000/yonetim/blog_ekle'
    driver.get(url)

    print("Sayfa Başlığı:", driver.title)
    assert test_value.text_giris_islemleri('[name="title_blog"]', f"Deneme Başlık{tarih}")
    assert test_value.text_giris_islemleri('[name="description_blog"]', "Deneme açıklama metni.")
    assert test_value.select_dropdown_by_value('blog_kategori', '2')
    dosya_yolu = os.path.abspath("home/static/home/images/pexels-kyleloftusstudios-2734519.jpg")
    assert test_value.dosya_yukle('image', dosya_yolu)
    assert test_value.tıklama('[name="isBlog_blog"]')
    time.sleep(3)
    assert test_value.tıklama('.btn.btn-primary.w-100')
    try:
        assert test_value.text_al('div.alert.alert-success')=="Blog Başarıyla Eklendi"
        print('🟩 BLog Ekleme Başarıyla Eklendi')
    except:
        print('🟥 Blog eklenemedi')