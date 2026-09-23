#========================================================
#Cargar librerias
#========================================================
import os                                                #Permite interactuar con el sistema operativo 
from playwright.sync_api import sync_playwright          #Importar el administrador de contexto sincrono
import requests                                          #Permite enviar mensajes a telegram

#========================================================
#Configurar telegram
#========================================================
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")      #Leer las credenciales (TOKEN/CHAT_ID) 
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")          #desde las variables de entorno

def ():

  return 

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
