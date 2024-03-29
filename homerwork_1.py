import pytest
from selenium import webdriver


@pytest.fixture  # подготовительные работы
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("https://google.ru")
