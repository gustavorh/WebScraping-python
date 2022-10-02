from calendar import month
from bs4 import BeautifulSoup
from datetime import date
import time
import requests

def encontrar_trabajos():
    url = requests.get('https://www.getonbrd.com/empleos-Python').text # URL de la página que queremos realizar un Scrap.
    soup = BeautifulSoup(url, 'lxml')

    trabajos = soup.find_all('div', class_='remote') # Buscará todas las etiquetas div con la clase 'remote'.

    for index, trabajo in enumerate(trabajos):
        titulo = trabajo.find('strong', class_='color-hierarchy1').text
        nivel = trabajo.find('span', class_='color-hierarchy3').text
        empresa = trabajo.find('div', class_='size0').text.split()[0]
        ubicacion = trabajo.find('span', class_='tooltipster').text.replace(' ', '')
        fecha_publicacion = trabajo.find('div', class_='gb-results-list__date color-hierarchy3').text
        link_publicacion = trabajo  .a['href']

        with open(f'publicaciones/{index}.txt', 'w') as archivo:
            archivo.write(f'Titulo: {titulo}\n')
            archivo.write(f'Nivel: {nivel}\n')
            archivo.write(f'Empresa: {empresa}\n')
            archivo.write(f'Ubicacion: {ubicacion.strip()}\n')
            archivo.write(f'Fecha Publicacion: {fecha_publicacion.strip()}\n')
            archivo.write(f'Link: {link_publicacion}\n')


if __name__ == '__main__':
    while True:
        encontrar_trabajos()
        espera = 10
        print(f'Esperando {espera} minutos...')
        time.sleep(espera * 60)