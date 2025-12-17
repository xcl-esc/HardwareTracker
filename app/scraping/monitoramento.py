from core.criacao_bd import ProdutoRaw
from app.scraping.driver import DriverPadrao


class ColetarProdLojas:
    def __init__(self, url: str):
        self.url = url
        self.driver_padrao = DriverPadrao(headless=False)
    
    def acessar_kabum(self):
        driver = self.driver_padrao.criar_driver()
        driver.get(self.url)
