# Ejercicio de calculadora
# x = int(input('Enter the first number: '))
# y = int(input('Enter the second number: '))
# resultado = x + y
# print(str(x), '+ ' + str(y), '= ' + str(resultado))
# *************************
# Ejercicio con cadenas: bucle con while y rebanado,
# fruta = 'banana'
# indice = 0
# while indice < len(fruta):
#     letra = fruta[indice]
#     print (letra)
#     indice = indice + 1
#     print(indice)

# print (fruta[2:6])
# print (fruta[0:5])
# print (fruta[:6])
# print (fruta[3:])
# *************************
# Ejercicio con cadenas: Bucles y contadores

# palabra = 'banana de luis'
# contador = 0
# for letra in palabra:
#     letra = palabra[contador]
#     contador = contador + 1
# print (contador)
# *************************
# Ejercicio con cadenas: Bucles y contadores
# usando una funcion para contar letras
# cadena = 'banana de luis'
# contador = 0
# letra = 'de'
# def contador_letras(contador, cadena, letra):
#     for letras in cadena:
#         if letras == letra:
#             contador = contador + 1
#     print (contador)

# contador_letras(contador, cadena, letra)
# *************************
# Ejercicio con cadenas: Bucles y contadores
# usando una funcion para buscar y contar la palabra que mas aparecen
# en un archivo de texto


cadena = open('poder.txt', encoding = 'utf-8')
texto = cadena.read()
palabras = texto.split()
contadores = dict()

for palabra in palabras:
        contadores[palabra] = contadores.get(palabra,0) + 1
print (palabras)

for linea in palabras:
        linea = cadena.readline(1)
        if not linea: break
        print(linea)

mayorcantidad = None
mayorpalabra = None
for palabra,contador in contadores.items():
    if mayorcantidad is None or contador > mayorcantidad:
        mayorpalabra = palabra
        mayorcantidad = contador
print (mayorpalabra, mayorcantidad)