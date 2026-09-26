#====================================================================
#Cargar librerias
#====================================================================
import os                                                              #Permite interactuar con el sistema operativo 
import requests                                                        #Permite enviar mensajes a telegram
import time
import sys                                                             #Interactuar con el intérprete de Python (manejo de argumentos de consola sys.argv, salidas controladas sys.exit y flujos de error sys.stderr)
from bs4 import BeautifulSoup                                          #Parser HTML/XML para navegar, buscar y extraer datos del árbol DOM de una página web 
from playwright.sync_api import sync_playwright                        #Importar el administrador de contexto sincrono

#====================================================================
#Configurar telegram
#====================================================================
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")                    #Leer las credenciales (TOKEN/CHAT_ID) 
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")                        #desde las variables de entorno

def enviar_alerta_telegram(mensaje: str) -> bool:
    """Envía un mensaje formateado a Telegram mediante la API HTTP."""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
                "chat_id": TELEGRAM_CHAT_ID,
                "text": mensaje,
                "parse_mode": "HTML"
                }
    try:
        response = requests.post(url, json=payload, timeout=10)
        return response.status_code == 200                                #Devuelve True si el status code es 200
    except Exception as e:
        print(f"Error al enviar a Telegram: {e}")
        return False


#====================================================================
#Estadisticas Principales
#====================================================================



#====================================================================
#Estadisticas principales
#====================================================================
def ():
    
    estadisticas = {}
    #==================================================================
    #1. Filas métricas estándar (xG, Posesión, Grandes ocasiones, Toques, Remates totales)    
    #================================================================== 
    for fila in soup_bloque.select('div[data-testid="wcl-statistics"]'):

    #==================================================================
    #2. Remates fuera y Remates a puerta (bloque de portería)   
    #==================================================================
    shot_container = soup_bloque.select_one('[class*="shotOnTargetStats_"]')
        
    #==================================================================
    #3. Córneres, Tarjetas amarillas y rojas (Badges SVG inferiores)    
    #==================================================================    
    for badge in soup_bloque.select('[class*="incidentValueBadge_"]'):    

  return estadisticas

#====================================================================
#Cuota del evento
#====================================================================
def partidos():
    data = {
            "Partido" : ""
            "Marcador" : ""
            "Cuotas" : ""
            "Tiempo" : ""
            "Minuto" : ""
            "Estadisticas" : {}
            }

    try:
        #==================================================================
        #Cabecera
        #==================================================================   
        soup_resumen = BeautifulSoup(page.content(), "html.parser")

        #==================================================================
        #Extraer Marcador, Estado y Minuto    
        #================================================================== 
        score = soup_resumen.select_one("div.detailScore__wrapper")
        if score:
            datos_partido["Marcador"] = score.get_text(separator=" ", strip=True)
    
        status = soup_resumen.select_one("span.fixedHeaderDuel__detailStatus")
        if status:
            datos_partido["Tiempo/Estado"] = status.get_text(strip=True)
    
        minuto = soup_resumen.select_one("span.eventTime")
        if minuto:
            datos_partido["Minuto"] = minuto.get_text(strip=True)
        
        #==================================================================
        #Extraer Cuotas 1X2
        #================================================================== 
        botones = soup_resumen.find_all("button", attrs={"data-analytics-bookmaker-id": True})
        valores_cuotas = []
        for btn in botones:
            span = btn.find("span", {"data-testid": "wcl-oddsValue"})
            if span and span.get_text(strip=True):
                valores_cuotas.append(span.get_text(strip=True))
            if len(valores_cuotas) == 3:
                break

        if len(valores_cuotas) >= 3:
            datos_partido["Cuotas"] = f"1: {valores_cuotas[0]} | X: {valores_cuotas[1]} | 2: {valores_cuotas[2]}"    
            
        #==================================================================
        #Extraer Estadísticas Principales
        #================================================================== 
        tab_stats = page.locator(
                                    'a[data-analytics-alias="match-statistics"], '
                                    'a:has-text("ESTADÍSTICAS"), '
                                    'button:has-text("ESTADÍSTICAS")'
                                ).first




#====================================================================
#Configurar el navegador
#====================================================================
def ():
  with sync_playwright() as p:
      browser = p.chromium.launch(
                                  headless=True                         #Ejecutar sin vetana gráfica
                                  args=["--no-sandbox",                 #Desactiva el aislamiento de seguridad de Chromium; necesario para correr como root o en contenedores Docker / CI
                                        "--disable-setuid-sandbox",     #Deshabilita la capa de sandbox basada en setuid; evita fallos de permisos en sistemas Linux restringidos
                                        "--disable-dev-shm-usage"]      #Fuerza el uso de /tmp en disco en lugar de la memoria compartida (/dev/shm), evitando cierres por falta de memoria RAM
                                )   
    
      context = browser.new_context(
                                  #El navegador se identifique ante las páginas web como un usuario humano común navegando en Google Chrome sobre Windows 10/11 de 64 bits.
                                  user_agent=(
                                              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "              #Mozilla/5.0, es un prefijo estándar por razones de compatibilidad histórica en la web
                                              "AppleWebKit/537.36 (KHTML, like Gecko) "                 #El motor de renderizado base del navegador.
                                              "Chrome/122.0.0.0 Safari/537.36"                          #Informa que el navegador es Google Chrome versión 122.
                                              )
                                  )
      main = context.new_page()
      
      try:
            main.goto(
                        "https://www.flashscore.pe/",                                                    #URL de destino a la que navegará el navegador
                        timeout=35000,                                                                   #Tiempo máximo de espera (35 segundos) antes de lanzar un error
                        wait_until="domcontentloaded"                                                    #Considera la carga completa apenas el DOM esté listo (sin esperar imágenes ni estilos)
                    )
            btn_live = "//div[contains(@class, 'filters__text') and text()='EN DIRECTO']"                #<div class="filters__text filters__text--short">EN DIRECTO</div>
            main.wait_for_selector(btn_live, timeout=15000)                                              #Esperar hasta 15 segundos a que el botón 'Live' esté disponible en el DOM  
            main.locator(btn_live).click()                                                               #Hacer clic en el botón 'Live'     
            main.wait_for_timeout(3000)                                                                  #Pausa breve (3 segundos) para permitir que cargue la interfaz tras la acción  

            soup = BeautifulSoup(main.content(), "html.parser")                                          #Obtener el HTML renderizado de la página  
            partidos = soup.find_all("div", id=lambda x: x and x.startswith("g_1_"))                     #Buscar todos los <div> cuyo atributo 'id' comience con 'g_1_'
                                                                                                         #<div elementtiming="SpeedCurveFRP" id="g_1_jLduogbE" class="event__match event__match--withRowLink event__match--live event__match--last event__match--twoLine" data-event-row="true"><a title="¡Haga click para detalles del partido!" href="https://www.flashscore.pe/partido/futbol/municipal-r5ooNVip/suchitepequez-jcRuUgp4/?mid=jLduogbE" target="_self" class="eventRowLink" aria-label="Municipal - Suchitepéquez" id="match-row-g_1_jLduogbE"></a><button data-state="closed" type="button" class="wcl-favorite_ggUc2 wcl-favoriteL_XlIW4 wcl-favoriteGray_LZl1A eventSubscriber__star--event" aria-label="¡Agregar este partido a Favoritos!" aria-describedby="match-row-g_1_jLduogbE" aria-pressed="false" data-testid="wcl-favorite-inactive"><svg fill="currentColor" viewBox="0 0 20 20" data-testid="wcl-icon-action-state-favorite" class="wcl-icon_WGKvC" width="18" height="18" aria-hidden="true"><path fill-rule="evenodd" class="action-state-favorite" d="m9.35 0-2.1 6.85L.4 6.83 0 8.14l5.54 4.21-2.13 6.84 1.06.81L10 15.76 15.53 20l1.05-.8-2.12-6.85L20 8.15l-.4-1.32-6.85.02L10.65 0h-1.3ZM8.4 7.8 10 2.57l1.6 5.21.66.5h5.2l-4.22 3.2-.25.81 1.63 5.21-4.22-3.23h-.8l-4.22 3.23 1.63-5.2-.26-.82-4.22-3.2h5.21l.66-.5Z"></path></svg></button><div class="event__stage"><div class="event__stage--block">Descanso</div></div><div class="wcl-participant_bctDY event__homeParticipant" data-testid="wcl-matchRow-participant"><div class="wcl-participants_ASufu"><div class="wcl-item_DKWjj"><img crossorigin="anonymous" data-testid="wcl-participantLogo" data-size="xxs" aria-hidden="true" class="wcl-assetContainer_KJQf9 wcl-logo_UrSpU wcl-logo_nYoLs wcl-sizeXXS_CNb8a" alt="Municipal" loading="lazy" src="https://static.flashscore.com/res/image/data/tdFtpxhT-vTLj5hDm.png"><span class="wcl-simple-text-01_EaZ9- wcl-scores_Na715 wcl-name_jjfMf" data-testid="wcl-simple-text-01">Municipal</span></div></div></div><div class="wcl-participant_bctDY event__awayParticipant" data-testid="wcl-matchRow-participant"><div class="wcl-participants_ASufu"><div class="wcl-item_DKWjj"><img crossorigin="anonymous" data-testid="wcl-participantLogo" data-size="xxs" aria-hidden="true" class="wcl-assetContainer_KJQf9 wcl-logo_UrSpU wcl-logo_nYoLs wcl-sizeXXS_CNb8a" alt="Suchitepéquez" loading="lazy" src="https://static.flashscore.com/res/image/data/IawfsfA6-SrRYQ9rd.png"><span class="wcl-simple-text-01_EaZ9- wcl-scores_Na715 wcl-name_jjfMf" data-testid="wcl-simple-text-01">Suchitepéquez</span></div></div></div><span class="wcl-bold_NZXv6 wcl-simple-text-01_EaZ9- wcl-scores_Na715 wcl-tableScore_FdKIN wcl-isLive_OkJtj wcl-isBold_eKUSd wcl-isPrimary_P3ji- event__score event__score--home" data-testid="wcl-tableScore" data-type="primary" data-highlighted="false" data-live="true" data-side="1">2</span><span class="wcl-bold_NZXv6 wcl-simple-text-01_EaZ9- wcl-scores_Na715 wcl-tableScore_FdKIN wcl-isLive_OkJtj wcl-isBold_eKUSd wcl-isPrimary_P3ji- event__score event__score--away" data-testid="wcl-tableScore" data-type="primary" data-highlighted="false" data-live="true" data-side="2">0</span><a href="https://www.flashscore.pe/partido/futbol/municipal-r5ooNVip/suchitepequez-jcRuUgp4/?mid=jLduogbE" class="event__icon event__icon--tv" aria-label="TV / Streaming en directo: 1xBet" aria-describedby="match-row-g_1_jLduogbE" data-state="closed"><svg fill="currentColor" viewBox="0 0 20 20" data-testid="wcl-icon-incidents-tv" class="wcl-icon_WGKvC wcl-matchRowIcon_HmASY" width="14" height="14" aria-hidden="true" data-live="false"><path fill-rule="evenodd" class="incidents-tv" d="M2.47 2 0 4.47v7.47l2.47 2.47h6.84v2.08H2.07v1.38h15.87v-1.38h-7.25v-2.08h6.84L20 11.94V4.47L17.53 2H2.47Zm-1.1 9.37V5.04l1.67-1.67h13.92l1.67 1.67v6.33l-1.67 1.67H3.04l-1.67-1.67Z"></path></svg></a><a class="event__icon event__icon--standing" aria-label="¡Haga click para ver alineaciones!" aria-describedby="match-row-g_1_jLduogbE"><svg fill="currentColor" viewBox="0 0 20 20" data-testid="wcl-icon-incidents-lineup" class="wcl-icon_WGKvC wcl-matchRowIcon_HmASY" width="14" height="14" aria-hidden="true" data-live="false"><path fill-rule="evenodd" class="incidents-lineup" d="m10.75 3.58 2.07-2.08h4.02L20 4.67v7.18h-4.14v-1.38h2.77V5.23l-2.36-2.36h-2.88l-2.07 2.08H8.68L6.61 2.87H3.73L1.38 5.24v5.23h2.76v1.37H0V4.67L3.16 1.5h4.02l2.07 2.08h1.5Zm3.74 13.79V7.7h1.37v11.03H4.14V7.71H5.5v9.66h8.98Z"></path></svg></a><div class="liveBetWrapper" data-bookmaker-id="417"><a aria-describedby="match-row-g_1_jLduogbE" class="wcl-badgeLiveBet_8XqLc wcl-isActive_n3xPi wcl-isAnimated_8eufS" aria-label="¡Apueste ahora en este partido EN DIRECTO!" data-testid="wcl-badgeLiveBet-animated"><svg viewBox="1 1 24 20" aria-hidden="true"><defs><clipPath id="clip"><path d="M0,22v-22h26v22z"></path></clipPath></defs><g clip-path="url(#clip)" transform="matrix(1,0,0,1,0,0)"><g transform="matrix(1,0,0,1,-15,5)" opacity="0"><path d="M4.74949,9h-3.573v-5.841h1.08v4.896h2.493zM6.65532,9h-1.08v-5.841h1.08zM10.6918,9h-1.18804l-2.043,-5.841h1.143l1.52104,4.482l1.521,-4.482h1.08zM17.228,8.055v0.945h-3.69v-5.841h3.654v0.954h-2.574v1.467h2.385v0.936h-2.385v1.539z"></path><animateTransform attributeName="transform" type="translate" values="0 0;16 0;16 0;0 0;0 0" dur="3.2s" repeatCount="indefinite" calcMode="spline" keyTimes="0;0.13;0.37;0.5;1" keySplines="0.5 0.35 0.15 1;0.5 0.35 0.15 1;0.5 0.35 0.15 1;0.5 0.35 0.15 1" additive="sum" fill="freeze"></animateTransform><animate attributeName="opacity" values="0;1;1;0;0" dur="3.2s" repeatCount="indefinite" calcMode="spline" keyTimes="0;0.13;0.37;0.5;1" keySplines="0.5 0.35 0.15 1;0.5 0.35 0.15 1;0.5 0.35 0.15 1;0.5 0.35 0.15 1" additive="sum" fill="freeze"></animate></g><g transform="matrix(1,0,0,1,-12,5)" opacity="0"><path d="M3.63777,9h-2.277v-5.841h2.178c0.354,0 0.669,0.066 0.945,0.198c0.282,0.132 0.504,0.321 0.666,0.567c0.162,0.24 0.243,0.522 0.243,0.846c0,0.3 -0.069,0.561 -0.207,0.783c-0.132,0.222 -0.309,0.375 -0.531,0.459c0.288,0.084 0.519,0.246 0.693,0.486c0.18,0.234 0.27,0.519 0.27,0.855c0,0.492 -0.177,0.891 -0.531,1.197c-0.354,0.3 -0.837,0.45 -1.449,0.45zM3.48477,4.077h-1.044v1.503h1.044c0.246,0 0.435,-0.069 0.567,-0.207c0.138,-0.138 0.207,-0.318 0.207,-0.54c0,-0.228 -0.069,-0.411 -0.207,-0.549c-0.132,-0.138 -0.321,-0.207 -0.567,-0.207zM3.61977,6.489h-1.179v1.602h1.179c0.27,0 0.48,-0.072 0.63,-0.216c0.15,-0.15 0.225,-0.342 0.225,-0.576c0,-0.234 -0.075,-0.426 -0.225,-0.576c-0.15,-0.156 -0.36,-0.234 -0.63,-0.234zM10.4867,8.055v0.945h-3.68999v-5.841h3.65399v0.954h-2.57399v1.467h2.38499v0.936h-2.38499v1.539zM13.6692,9h-1.089v-4.887h-1.692v-0.954h4.491v0.954h-1.71z"></path><animateTransform attributeName="transform" type="translate" values="0 0;0 0;15 0;15 0;0 0" dur="3.2s" repeatCount="indefinite" calcMode="spline" keyTimes="0;0.5;0.63;0.87;1" keySplines="0.5 0.35 0.15 1;0.5 0.35 0.15 1;0.5 0.35 0.15 1;0.5 0.35 0.15 1" additive="sum" fill="freeze"></animateTransform><animate attributeName="opacity" values="0;0;1;1;0" dur="3.2s" repeatCount="indefinite" calcMode="spline" keyTimes="0;0.5;0.63;0.87;1" keySplines="0.5 0.35 0.15 1;0.5 0.35 0.15 1;0.5 0.35 0.15 1;0.5 0.35 0.15 1" additive="sum" fill="freeze"></animate></g><g transform="matrix(6.123233995736766e-17,1,-1,6.123233995736766e-17,25,7)"><g transform="matrix(-1,2.4492935982947064e-16,-2.4492935982947064e-16,-1,7,4.5)"><path class="wcl-arrow_xSabT" d="M5.70688,0l-2.70704,2.46585l-2.70674,-2.4653l-0.29311,0.26721l2.99985,2.73224l3.00015,-2.73279l-0.29251,-0.26721z"></path></g></g></g></svg></a></div></div>
            for p_div in partidos[:10]:
                id_p = p_div.get('id').split('_')[-1]
                h_team = p_div.find("div", class_=lambda c: c and "home" in c.lower() and "participant" in c.lower())
                a_team = p_div.find("div", class_=lambda c: c and "away" in c.lower() and "participant" in c.lower())
                nombre_partido = f"{h_team.get_text(strip=True) if h_team else 'Local'} vs {a_team.get_text(strip=True) if a_team else 'Visitante'}"

      
      except Exception as e:
            print(f"Error durante el escaneo general: {e}")          
      finally:
            browser.close()
    
if __name__ == "__main__":                                             #Asegurar que el bloque de código debajo de ella solo se ejecute
                                                                       #cuando el archivo se corre directamente, y no cuando se importa 
                                                                       #como un módulo desde otro script de Python.

