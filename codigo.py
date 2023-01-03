# Esto es un comentario
import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urlparse

## PRIMERA PARTE DEL CÓDIGO

# URL del repositorio PUCP: tesis de Ingeniería Informática
url = 'https://repositorio.pucp.edu.pe/index/handle/123456789/9139/recent-submissions'
parsed_url = urlparse(url)

# Hacer solicitud HTTP a la URL y obtener el contenido HTML
response = requests.get(url)
html = response.content

# Procesar el HTML con BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Buscamos 
ps = soup.find('a', class_ = 'next-page-link').get('href')

# Obtiene el dominio principal
domain = parsed_url.netloc

# Obtiene el esquema
scheme = parsed_url.scheme

# Construye el URL del dominio principal
url2 = f'{scheme}://{domain}'

lista = []
lista.append(url2 + ps)
url3 = None
i = 0
while lista[-1] != url2:
    
    url3 = lista[i]

    # Solicitud
    r = requests.get(url3)
    h = r.content
    
    # Procesar
    s = BeautifulSoup(h, 'html.parser')
    
    # Buscamos
    p = s.find('a', class_ = 'next-page-link').get('href')
    
    # Agregamos a la lista
    lista.append(url2 + p)
    #print(lista)
    i += 1

lista.pop(-1)

## SEGUNDA PARTE DEL CÓDIGO

handle = []

for i in lista:
    # URL del repositorio PUCP: tesis de Ingeniería Informática
    url4 = i

    # Hacer solicitud HTTP a la URL y obtener el contenido HTML
    response2 = requests.get(url4)
    html2 = response2.content

    # Procesar el HTML con BeautifulSoup
    soup2 = BeautifulSoup(html2, 'html.parser')

    # Extraer todos los enlaces con la etiqueta <h4>
    h4s = soup2.find_all('h4')

    # Iterar sobre cada etiqueta <h4>
    for h4 in h4s:
        # Extraer el enlace de la etiqueta <a> dentro de la etiqueta <h4>
        link = h4.find('a').get('href')
        handle.append(link)

## TERCERA PARTE DEL CÓDIGO

etiquetas = []
rutas = []

for j in handle:
    
    # Obtén el contenido HTML de la página web
    url5 = url2 + j
    page3 = requests.get(url5)
    soup3 = BeautifulSoup(page3.content, 'html.parser')
    # Buscar todos los enlaces que tengan el texto "Show full item record"
    enlaces = soup3.find_all('a', text='Show full item record')

    # Si se encontraron enlaces, obtener el valor del atributo href del primer enlace
    if enlaces:
        href = enlaces[0]['href']
        rutas.append(href)  # imprime el valor del atributo href
