from bs4 import BeautifulSoup

with open('index.html', 'r') as archivo:
    contenido = archivo.read()
    
    soup = BeautifulSoup(contenido, 'lxml')
    
    # Podemos filtrar para buscar una etiqueta HTML en específico, por ejemplo <h5>.
    tags = soup.find_all('h5') # Esto, nos retornará una lista conteniendo todas las etiquetas encontradas. 
    #print(tags)
    # Para un mejor manejo de datos, podemos imprimir cada una de las etiquetas de forma separada.
    for tag in tags: 
        print(tag.text )