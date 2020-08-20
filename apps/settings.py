import os

APP_NAME = 'Translate Excel'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_PATH = os.path.join(BASE_DIR, 'assets')
CHROME_DRIVER_PATH = os.path.join(ASSETS_PATH, 'chromedriver.exe')
CHROME_BINARY_PATH = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'

TRANSLATE_URL = 'https://translate.google.co.kr/?hl=ko#view=home&op=translate&sl=auto&tl=ko'
