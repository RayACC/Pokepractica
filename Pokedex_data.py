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

C:/Users/tsuku/PycharmProjects/Pokepractica/Dex/ ubicacion pc ray

"""""
pathdatadex= input("introduce la ubicacion en la que guardaras la informacion: ")
salir_programa=""
contador_descripcion = 0
poke_des = ""
puntuacion = [".",","," "]
longitud = 0
menos_de_30 = 0

while salir_programa != "no" :

    diferencia = 0
    salir_programa = ""
    contador_descripcion = 0
    poke_des = ""
    puntuacion = [".", ",", " "]
    longitud = 0
    menos_de_30 = 0

    poke_num = input("Numero del pokemon: ")
    poke_nom = input("Nombre del pokemon: ")
    poke_desA = input("Descripcion: ")

    longitud= len(poke_desA)
    residuo_longitud = longitud%40

    if residuo_longitud > 0 :
        menos_de_30 = False
        if longitud < 40:
         menos_de_30 = True
    else:
        if longitud < 40:
         menos_de_30 = True

    pokearchivo = open(pathdatadex + poke_num + '.-' + poke_nom +'.txt' ,'w')
    pokearchivo.write("Numero: {} \n".format(poke_num))
    pokearchivo.write("Nombre: {} \n" .format(poke_nom))
    pokearchivo.write("Descripcion:\n")
    pokearchivo.close()

    if menos_de_30 == True:
        for letra in poke_desA:
            poke_des += letra

        pokearchivo = open(pathdatadex + poke_num + '.-' + poke_nom + '.txt', 'a')
        pokearchivo.write("{} \n".format((poke_des)))
        pokearchivo.close()
        contador_descripcion = 0
        poke_des = ""
    else:
        for letra in poke_desA:
            poke_des += letra
            if contador_descripcion >=40:
                contador_descripcion += 1
                if letra in puntuacion :
                    pokearchivo = open(pathdatadex + poke_num + '.-' + poke_nom + '.txt', 'a')
                    pokearchivo.write("{} \n".format((poke_des)))
                    pokearchivo.close()
                    poke_des = ""
                    contador_descripcion = 0
            else:
             contador_descripcion +=1

        pokearchivo = open(pathdatadex + poke_num + '.-' + poke_nom + '.txt', 'a')
        pokearchivo.write("{} \n".format((poke_des)))
        pokearchivo.close()
        poke_des = ""
    salir_programa= input("Si/No: ")
    salir_programa = salir_programa.lower()
