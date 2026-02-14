mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
minusculas = "abcdefghijklmnñopqrstuvwxyz"

desplazamiento = 0

def cifrar(texto):
    resultado = ""
    
    for letra in texto:
        if letra in mayusculas:
            pos = mayusculas.find(letra)
            nueva_pos = (pos + desplazamiento) % len(mayusculas)
            resultado += mayusculas[nueva_pos]
            
        elif letra in minusculas:
            pos = minusculas.find(letra)
            nueva_pos = (pos + desplazamiento) % len(minusculas)
            resultado += minusculas[nueva_pos]
            
        else:
            resultado += letra
            
    return resultado


def descifrar(texto):
    resultado = ""
    
    for letra in texto:
        if letra in mayusculas:
            pos = mayusculas.find(letra)
            nueva_pos = (pos - desplazamiento) % len(mayusculas)
            resultado += mayusculas[nueva_pos]
            
        elif letra in minusculas:
            pos = minusculas.find(letra)
            nueva_pos = (pos - desplazamiento) % len(minusculas)
            resultado += minusculas[nueva_pos]
            
        else:
            resultado += letra
            
    return resultado


print("Cifrado César personalizado")
print("Cifrar")
print("Descifrar")

opcion = input("Elige una opcion (1 o 2): ")

entrada = input("Introduce el desplazamiento: ")
desplazamiento = int(entrada)

if opcion == "1":
    texto = input("Texto a cifrar: ")
    print("Resultado: " + cifrar(texto))

elif opcion == "2":
    texto = input("Texto a descifrar: ")
    print("Resultado: " + descifrar(texto))

else:
    print("Opción no válida")
