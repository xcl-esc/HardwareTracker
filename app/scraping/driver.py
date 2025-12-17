from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class DriverPadrao:
    def __init__(self, headless:bool = False):
        self.headless = headless

    def _config_opcoes(self) -> Options:
        options = Options()

        if self.headless:
            options.add_argument("--headless=new")

        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--start-maximized")

        return options

    def criar_driver(self) -> webdriver.Chrome:
        '''- Tentar não misturar inlges com portugues'''

        options = self._config_opcoes()
        
        service = Service(ChromeDriverManager().install())

        driver= webdriver.Chrome(
            service=service,
            options=options
        )

        return driver