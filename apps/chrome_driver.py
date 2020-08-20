from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from apps.settings import CHROME_DRIVER_PATH, CHROME_BINARY_PATH, TRANSLATE_URL
from apps.utils import time_sleep as _


class ChromeDriver:

    def __init__(self, *args, **kwargs):
        # options = Options()
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        # options.add_argument('--disable-dev-shm-usage')
        # options.add_argument('--disable-gpu')
        options.binary_location = CHROME_BINARY_PATH

        self.driver = webdriver.Chrome(executable_path = CHROME_DRIVER_PATH, options = options)
        self.driver.get(TRANSLATE_URL)
        _()

    def translate(self, text: str) -> str:
        self.driver.find_element_by_id('input-wrap').find_element_by_tag_name('textarea').clear()
        self.driver.find_element_by_id('input-wrap').find_element_by_tag_name('textarea').send_keys(text)
        _(2)

        result = self.driver.find_element_by_class_name('tlid-translation').find_element_by_tag_name('span').text
        print('{} -> {}'.format(text, result))
        return result

    def run(self, translate_data: list) -> list:
        translate_result = []

        for data in translate_data:
            translate = self.translate(data['value'])
            data.update({ 'translate': translate })
            translate_result.append(data)

        self.driver.quit()
        return translate_result
