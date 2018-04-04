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
salir=""

while salir != "no" :
    pokenum= 0
    pokenom=""    "nombre del pokemon"
    pokedes=""    "descripcion del pokedex"

    pokenum = input("Numero del pokemon: ")
    pokenom = input("Nombre del pokemon: ")
    pokedes = input("Descripcion: ")
    
    pokearchivo = open('C:/Users/tsuku/PycharmProjects/Pokepractica/Dex/'+ pokenum + '.-' + pokenom +'.txt' ,'w')
    pokearchivo.write("Numero: {} \n".format(pokenum))
    pokearchivo.write("Nombre: {} \n" .format(pokenom))
    pokearchivo.write("Descripcion: ")
    
      desantes= pokedes
      cont1 = 0
      pokedes= ""
      
       for letra in desantes:
        pokedes.append(letra)
        
          if cont1 >= 40:
        
            if letra = "." or "," or " "
            pokearchivo.write("{} \n".format(pokedes))
            pokedes = ""
            cont1=0
          
       cont1 += 1
      
    pokearchivo.close()
    salir=input("Desea agregar otro pokemon?(si/no) : ")
    salir = salir.lower()
