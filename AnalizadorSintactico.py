# Importo la libreria sys #
import sys

#------------------------#
#   Funcion principal    #
#------------------------#
def main():

    # Declaro una variable y le asigno un archivo de texto con el codigo fuente #
    nombreArchivo = "A.Semantico\test.txt"

    # Abro el archivo #
    with open(nombreArchivo, "r") as archivo:
        for line in archivo: # Recorro todas las lineas del archivo #
            for palabra in line.split(): # Recorro todas las lineas del archivo #
                palabraList.append(palabra) # Agrego a la lista de palabras #
    
    # Si el codigo fuente esta bien entonces #
    if(programa()):
        print("El programa es valido") # Le mando un mensaje al usuario #
    else: # Caso contrario #
        print("Programa no valido") # Le mando un mensaje al usuario #

#------------------------------------------------------------------------------------------#
#   Funcion que va a analizar y mostrar todo el contenido del txt incluyendo los errores   #
#------------------------------------------------------------------------------------------#
def programa():

    # Verifico que esté la palabra begin para que funcione el programa #
    palabra = palabraList.pop(0)

    # Si la palabra es begin entonces #
    if(palabra == "begin"):


        print(palabra, "{") # Muestro la palabra osea begin seguido de una llave { #

        # Verifico las declaraciones #
        declaraciones()

        # Verifico las ordenes #
        ordenes()

        # Le asigno el valor a la palabra #
        palabra = palabraList.pop(0)

        # Pregunto si la palabra es end #
        if(palabra == "end"):
            print(palabra, "}") # Muestro la palabra osea end seguido de una llave } #
            return True # Retorno un valor verdadero indicando que la sintaxis esta correcta #
        else: # Caso contrario #
            sys.exit('Error, el programa no contiene end') # Le mando un mensaje al usuario indicandole que falta la palabra end #

    else: # caso contrario #
        sys.exit('Error, el programa no contiene begin') # Le mando un mensaje al usuario indicandole que falta la palabra begin #
        return False # Retorno un valor falso indicando que la sintaxis esta correcta #

#------------------------------------#
#   Funcion para las declaraciones   #
#------------------------------------#
def declaraciones():

    # Veo lo que se declaro #
    declaracion()

    if(palabraList[0] == ";"): # Verifico que las declaraciones terminen con punto y coma ; #
            print(";") # Imprimo el punto y coma #
            palabraList.pop(0) # Remuevo el punto y coma de la lista de palabras #
            nextDeclaraciones() # Verifico la siguiente declaracion #
    else: # Caso contrario #
        sys.exit('Error: declaracion no tiene ; al final') # Le mando un mensaje al usuario indicandole que falta el punto y coma #

#-----------------------------------------------#
#   Funcion para las siguientes declaraciones   #
#-----------------------------------------------#
def nextDeclaraciones():

    # Pregunto por el tipo #
    if(tipo()):

        # Veo lo que se declaro #
        declaracion() 

        # Verifico si la lista de palabras termina con punto y coma y hago lo mismo que en declaraciones #
        if(palabraList[0] == ";"):
                print(";")
                palabraList.pop(0)
                nextDeclaraciones()
        else:
            sys.exit('Error, declaracion no tiene ;') # Le mando un mensaje al usuario #
            exit
    else:
        return # No retorno nada #

#--------------------------------------------#
#   Funcion para mostrar las declaraciones   #
#--------------------------------------------#
def declaracion():
    if(tipo()):
        palabra = palabraList.pop(0)
        print(palabra, end = ' ')
        listaVariables()
    else:
        raise SystemExit('Error: El tipo de variable no es valida')

#------------------------------#
#   Funcion para las ordenes   #
#------------------------------#
def ordenes():

    orden()
    
    palabra = palabraList.pop(0)

    if(palabra == ";"):
        nextOrdenes()
    else:
        sys.exit('Error: La orden debe terminar con ;')

#-----------------------------------------#
#   Funcion para las siguientes ordenes   #
#-----------------------------------------#
def nextOrdenes():

    palabra = palabraList[0]
    
    if("end" in palabra or "else" in palabra):
        return
    else:
        orden()
        palabra = palabraList.pop(0)

        if(palabra == ";"):
            nextOrdenes()
        else:
            sys.exit('Error: La orden debe terminar con ;')

#--------------------------------------#
#   Funcion para mostrar las ordenes   #
#--------------------------------------#
def orden():
    palabra = palabraList[0]
    print(palabra)

    if(palabra.find("if") != -1):
        palabra = palabra.replace('if', '')
        palabraList.pop(0)

        if(len(palabra) > 0):
            palabraList.insert(0,palabra)
        condicion()

    elif(palabra.find("while") != -1):
        palabra = palabra.replace('while', '')
        palabraList.pop(0)

        if(len(palabra) > 0):
            palabraList.insert(0,palabra)
        bucle_while()

    else:
        asignar()

#---------------------------------------------------------------#
#   Funcion para determinar si una palabra es un tipo de dato   #
#---------------------------------------------------------------#
def tipo():
    palabra = palabraList[0]
    if(palabra == "entero" or palabra == "real"):
        return True
    else:
        return False

#-------------------------------------------------------------------------------------#
#   Funcion para cuando se declaren una lista de variables ejemplo: entero a, b, c;   #
#-------------------------------------------------------------------------------------#
def listaVariables():

    palabra = palabraList.pop(0)

    # Verifico las palabras #
    identificador(palabra)
    if(palabra.find(",") != -1):
        palabra = palabra.replace(',', '')
        identificadores.append(palabra)

    if(palabra.find(";") != -1):
        palabra = palabra.replace(';', '')
        identificadores.append(palabra)

    nextListaVariables()

#-----------------------------------------------------------------------------------------------#
#   Funcion para cuando se declaren una lista de variables siguiente ejemplo: entero d, e, f;   #
#-----------------------------------------------------------------------------------------------#
def nextListaVariables():
    if(palabraList[0] == ","):
        palabraList.pop(0)
        print(", ", end="")
        listaVariables()
    else:
        return

#-----------------------------------------------------------#
#   Funcion para saber su una palabra es un identificador   #
#-----------------------------------------------------------#
def identificador(palabra):
    cont = 0
    letra(palabra[cont])
    cont = cont + 1
    resto_letras(palabra, cont)

#------------------------------------------------------------------------#
#   Funcion para saber si el identificador contiene caracteres validos   #
#------------------------------------------------------------------------#
def letra(letter):
    if(letter.isalnum()):
        print(letter, end= '')
        return 
    else:
        sys.exit('Error: el identificador no contiene caracteres validos')
        exit

#-------------------------------------------------------------------------#
#   Funcion para verificar el resto de letras despyes del identificador   #
#-------------------------------------------------------------------------#
def resto_letras(palabra, cont):

    if(palabra[cont] == ";"):
        newpalabra = palabra[cont]
        palabraList.insert(0,newpalabra)
        return

    elif(palabra[cont] == ","):
        newpalabra = palabra[cont]
        palabraList.insert(0,newpalabra)
        return

    elif(cont == len(palabra)-1):
        return

    else:
        letra(palabra[cont])
        cont = cont + 1
        resto_letras(palabra, cont)

#--------------------------------------------#
#   Funcion para verificar las condiciones   #
#--------------------------------------------#
def condicion():
    palabra = palabraList.pop(0)

    if(palabra[0] == '('):

        # Si la palabra es mas larga que la del ( entonces la divido #
        if(len(palabra) > 1):
            newpalabra = palabra.replace('(', '')
            palabraList.insert(0, newpalabra)

        # Verifico la comparacion #
        comparacion()

        palabra = palabraList.pop(0)
        if(palabra == ')'):
            ordenes()
            nextCondicion()
            return
        else:
            sys.exit('Error: La comparacion del if no esta entre parentesis')
    else:
        sys.exit('Error: La comparacion del if no esta entre parentesis')

#-------------------------------------------------------#
#   Funcion para verificar las siguientes condiciones   #
#-------------------------------------------------------#
def nextCondicion():
    palabra = palabraList[0]

    if("end" in palabra):
        palabra = palabraList.pop(0)
        if(";" in palabra):
            palabra = palabra.replace(";", '')
            palabraList.insert(0, ";")
        return
    else:
        if("else" in palabra):
            palabra = palabraList.pop(0)
            ordenes()

            palabra = palabraList[0]
            if("end" in palabra):
                palabra = palabraList.pop(0)
                if(";" in palabra):
                    palabra = palabra.replace(";", '')
                    palabraList.insert(0, ";")
                    return
                else:
                    sys.exit('Error: El end del if no tiene ;')
            else:
                sys.exit('Error: El if no tiene end')
        else:
            sys.exit('Error: El if no tiene end')

#---------------------------------------------------------------------#
#   Funcion para verificar la sintaxis del bucle while sea correcta   #
#---------------------------------------------------------------------#
def bucle_while():
    palabra = palabraList.pop(0)

    if(palabra[0] == '('):

        # Si la palabra es mas larga que la del ( entonces la divido #
        if(len(palabra) > 1):
            newpalabra = palabra.replace('(', '')
            palabraList.insert(0, newpalabra)

        # Verifico la comparacion #
        comparacion()

        palabra = palabraList.pop(0)
        if(palabra == ')'):
            ordenes()
            palabra = palabraList.pop(0)
            if(";" in palabra):
                palabra = palabra.replace(";", '')
                palabraList.insert(0, ";")
            if(palabra == "endwhile"):
                print("endwhile")
                return
            else:
                sys.exit('Error: Falta el endwhile')
        else:
            sys.exit('Error: La comparacion del while no esta entre parentesis')
    else:
        sys.exit('Error: La comparacion del while no esta entre parentesis')

#-------------------------------------------------#
#   Llamo o ejecuto las funciones antes creadas   #
#-------------------------------------------------#
def comparacion():
    operador()
    condicion_op()
    operador()

#------------------------------------------------------#
#   Funcion para saber si una palabra es un operador   #
#------------------------------------------------------#
def operador():
    id = False
    palabra = palabraList.pop(0)

    if(existsIdentificadores(palabra)):
        return
    else:
        if ')' in palabra:
            palabra = palabra.replace(')', '')
            palabraList.insert(0, ')')
        numeros(palabra)

#----------------------------------------------------#
#   Funcion para sabes si existen indentificadores   #
#----------------------------------------------------#
def existsIdentificadores(palabra):
    if palabra in identificadores:
        return True

    else:
        for i in range(1,len(palabra)): # Verifico si es un identificador #
            if palabra[:i] in identificadores:        
                new = palabra.replace(palabra[:i], '')
                palabraList.insert(0,new)
                return True

    return False

#---------------------------------------------------------------------#
#   Funcion para saber si hay algun operador de mas en la condicion   #
#---------------------------------------------------------------------#
def condicion_op():
    palabra = palabraList.pop(0)
    if(palabra[0] == '=' or palabra[0] == '<=' or palabra[0] == '>=' or palabra[0] == '<>' or  palabra[0] == '<' or palabra[0] == '>'):
        if(len(palabra)> 1):
            new = palabra[1:len(palabra)]
            palabraList.insert(0,new)
            return
        else:
            return
    else:
         sys.exit('Error: La comparacion no tiene operador condicional')

#----------------------------------------------------#
#   Funcion para asignarle valores a las variables   #
#----------------------------------------------------#
def asignar(): # FALTA EXPRESION ARITMETICA #

    palabra = palabraList.pop(0)
    index_asign = palabra.find(':=')

    if(index_asign != -1):
        palabra = palabra.replace(':=', '')
        palabraList.insert(0,":=")
        if(len(palabra) > index_asign):
            newpalabra = palabra[index_asign:len(palabra)]
            palabraList.insert(1,newpalabra)
            palabra = palabra[0:index_asign]

    # Verifico si el identificador fue declarado anteriormente #
    if(palabra in identificadores):
        palabra = palabraList.pop(0)
        if(palabra == ":="):
            expresion_arit()
        else:
            sys.exit('Error: Se intento asignar valor si el operador correcto :=')

    else:
        sys.exit('Error: Se intento asignar valor a un identificador no declarado')

#--------------------------------------------------------------------------------------#
#   Funcion para verificar que las expresiones aritmeticas terminen con punto y coma   #
#--------------------------------------------------------------------------------------#
def expresion_arit():
    palabra = palabraList.pop(0)
    if(";" in palabra):
        palabra = palabra.replace(";", '')
        palabraList.insert(0,";")

    # Inicia con el identificador #
    if(existsIdentificadores(palabra)): 
        expArit()
    elif(numeros(palabra)):
        expArit()

#----------------------------------------------#
#   Funcion para las expresiones aritmeticas   #
#----------------------------------------------#
def expArit():
    palabra = palabraList[0]
    if(operador_arit(palabra[0])):
        palabraList.pop(0)
        if(len(palabra)>1):
            new = palabra[1:]
            palabraList.insert(0,new)
        expresion_arit()
        expArit()
    else:
        return

#-----------------------------------------------------------#
#   Funcion para las verificar los operadores aritmeticas   #
#-----------------------------------------------------------#
def operador_arit(palabra):
    if(palabra == '+' or palabra == '*' or palabra == '-' or palabra == '/'):
        return True
    else:
        return False

#---------------------------------------------------#
#   Funcion para saber si la palabra es un numero   #
#---------------------------------------------------#
def numeros(palabra):
    num = is_number(palabra)
    return num

#--------------------------------------------------------------------------#
#   Funcion para saber si la palabra es un numero y convertirlo a numero   #
#--------------------------------------------------------------------------#
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

# Inicializo la lista de palabras y los identificadores #
palabraList = []
identificadores = []

# Llamo la funcion principal #
main()