#========================================================
#Cargar librerias
#========================================================
from playwright.sync_api import sync_playwright
import requests                                          #Permite enviar mensajes a telegram

#========================================================
#Configurar telegram
#========================================================


#========================================================
#Configurar el navegador
#========================================================
def ():
  with sync_playwright() as p:
      browser = p.chromium.launch(
                                  headless=True          #Ejecutar sin vetana gráfica
                                )   
      page = browser.new_page()
      page.goto("https://example.com")
      
      # Extraer contenido tras la ejecución de JS
      titulo = page.locator("h1").inner_text()
      
      
      browser.close()
