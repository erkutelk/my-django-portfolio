import os
import django
import pytest

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfoy_app_mian.settings")
django.setup()

@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    """Tüm testlerde veritabanı erişimini etkinleştirir."""
    pass

