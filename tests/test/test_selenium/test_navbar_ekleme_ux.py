import time
import pytest
from selenium import webdriver
from tests.test.test_selenium.selenium_sites import SeleniumTest
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_navbar_ekleme(driver):
    import time
    tarih = str(int(time.time()))[:9]#9 u tarih tam turmuyordu o yüzden 9 basamaklı al dedik
    test_value = SeleniumTest(driver)

    url = 'http://127.0.0.1:8000/yonetim/navbar_ekle'
    driver.get(url)

    print("Sayfa Başlığı:", driver.title)
    assert test_value.text_giris_islemleri('#id_title', f"Deneme{tarih}")
    assert test_value.tıklama('#id_isActive')
    assert test_value.tıklama('.btn.btn-primary.w-100')
    tum_satirlar = test_value.driver.find_elements(By.CSS_SELECTOR,'.tablo > table > tbody > tr>td:nth-child(2)')
    print(tum_satirlar)
    gelmesi_gereken_deger = tum_satirlar[-1].text.strip()
    print("Gelen Değer:", gelmesi_gereken_deger)
    print("Beklenen Değer:", f"Deneme{tarih}")
    try:
        assert f"Deneme{tarih}" in gelmesi_gereken_deger
        print('🟩 Navbar Ekleme Başarıyla Gerçekleşti.')
    except:
        print('🟥 Navbar Eklenirken Hata Meydana Geldi.')
        