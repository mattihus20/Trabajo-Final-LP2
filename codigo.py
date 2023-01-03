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
        
        
universidad = []
titulo = []
autor = []
grado = []
asesor = []
resumen = []
anio = []

v = ['dc.publisher','dc.title','dc.contributor.author','thesis.degree.name','dc.contributor.advisor',
    'dc.description.abstract','dc.date.issued']

for o in rutas:

    q = url2 + o
    p = requests.get(q)
    ss = BeautifulSoup(p.content, 'html.parser')
    ls = ss.find_all('td', class_= 'label-cell')
    tds = ss.find_all('td', class_= 'word-break')

    m = []
    for td in tds:
        c = td.text
        m.append(c)

    l = []
    for g in ls:
        u = g.text
        l.append(u)
    
    diccionario = dict(zip(l,m))
  
    if v[0] in diccionario:
        universidad.append(diccionario[v[0]])
    else:
        universidad.append('Sin registro')

    if v[1] in diccionario:
        titulo.append(diccionario[v[1]])
    else:
        titulo.append('Sin registro')

    if v[2] in diccionario:
        autor.append(diccionario[v[2]])
    else:
        autor.append('Sin registro')

    if v[3] in diccionario:
        grado.append(diccionario[v[3]])
    else:
        grado.append('Sin registro')

    if v[4] in diccionario:
        asesor.append(diccionario[v[4]])
    else:
        asesor.append('Sin registro')

    if v[5] in diccionario:
        resumen.append(diccionario[v[5]])
    else:
        resumen.append('Sin registro')

    if v[6] in diccionario:
        anio.append(diccionario[v[6]])
    else:
        anio.append('Sin registro')

        

datos = {
    'Universidad': universidad,
    'Titulo': titulo,
    'Autor': autor,
    'Grado': grado,
    'Asesor': asesor,
    'Resumen': resumen,
    'Año': anio
}

df = pd.DataFrame(datos)
df.to_csv('tesis.csv', sep = ';', encoding = 'utf-8')
