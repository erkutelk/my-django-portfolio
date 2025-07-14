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

def test_blog_kategori(driver):
    import time
    tarih = str(int(time.time()))[:9]
    test_value = SeleniumTest(driver)

    url = 'http://127.0.0.1:8000/yonetim/blog_kategori/'
    driver.get(url)

    print("Sayfa Başlığı:", driver.title)
    assert test_value.text_giris_islemleri('#id_kategori', f"Deneme{tarih}")
    assert test_value.tıklama('#id_isActive')
    assert test_value.tıklama('.btn.btn-primary.w-100')
    tum_satirlar = test_value.driver.find_elements(By.CSS_SELECTOR,'.tablo > table > tbody > tr>td:nth-child(2)')
    print(tum_satirlar)
    gelmesi_gereken_deger = tum_satirlar[-1].text.strip()
    print("Gelen Değer:", gelmesi_gereken_deger)
    print("Beklenen Değer:", f"Deneme{tarih}")
    assert f"Deneme{tarih}" in gelmesi_gereken_deger
