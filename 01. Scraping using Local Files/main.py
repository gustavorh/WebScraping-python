from bs4 import BeautifulSoup

with open('index.html', 'r') as archivo:
    contenido = archivo.read()
    
    soup = BeautifulSoup(contenido, 'lxml')
    print(soup)