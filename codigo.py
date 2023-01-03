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
