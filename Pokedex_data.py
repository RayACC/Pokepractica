""""" 
Programa para crear un archivo y agregar los datos de los pokemon
Numero:
Nombre:
Descripcion:
  
funcion open("nombre del archivo","modo")
modos: w , a , r
w: crear y escribe archivo
a: si el archivo existe agrega al final
r: solo lectura

  
"""""
pokenum=0     "numero del pokemon"
pokenom=""    "nombre del pokemon"
pokedes=""    "descripcion del pokedex"

pokenum = input("Numero del pokemon: ")
pokenom = input("Nombre del pokemon: ")
pokedes = input("Descripcion: ")

pokearchivo = open('{}'.format(pokenom) ,'w', 'txt') 

pokearchivo.close()
