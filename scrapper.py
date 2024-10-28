import requests
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from get_clasifications import get_clasifications
from get_matches import get_matches

options = Options()
options.add_argument("--disable-dev-shm-usage")  # Evita problemas de memoria compartida
options.add_argument("--no-sandbox")  # Necesario si se ejecuta como root
options.add_argument("--headless")  # Ejecuta Chrome en modo sin cabeza (opcional)

URL = 'https://datos.madrid.es/portal/site/egob/menuitem.c05c1f754a33a9fbe4b2e4b284f1a5a0/?vgnextoid=1d72f30d4a95b410VgnVCM2000000c205a0aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD&vgnextfmt=default#two'

# Configura el navegador (asegúrate de tener el controlador adecuado, como chromedriver)
driver = webdriver.Chrome(options=options)

# Abre la página web
driver.get(URL)

# Encuentra el cuarto párrafo dentro de los elementos con la clase 'content-box'
paragraphs = driver.find_elements(By.CSS_SELECTOR, '.content-box p')
if len(paragraphs) >= 5:
    date = paragraphs[4].text
else:
    print("No se encontró el cuarto párrafo")

# Comparamos nuestros datos con los nuevos datos
with open('date.json', 'r', encoding='utf-8') as json_file:
    datos = json.load(json_file)

if (datos['date'] == date):
    print('No hacemos nada')
else:
  # Guardamos resultados en un json
  with open('date.json', 'w', encoding='utf-8') as json_file:
    json.dump({ 'date': date }, json_file, ensure_ascii=False, indent=2)
  
  print('Resultados guardados en date.json')

  # Encuentra los botones de descarga
  links = driver.find_elements(By.CSS_SELECTOR, '.asociada-link.ico-csv')

  # Extraer los hrefs y descargar los archivos
  for idx, link in enumerate(links):
    href = link.get_attribute('href')
    response = requests.get(href)
    
    # Guardar cada archivo con un nombre único
    if idx == 0:
       filename = 'clasificaciones.csv'
    else:
       filename = 'partidos.csv'

    with open(filename, 'wb') as file:
        file.write(response.content)
    
    print(f'Archivo descargado como {filename}')

  get_clasifications()

  get_matches()
  
# Cierra el navegador
driver.quit()