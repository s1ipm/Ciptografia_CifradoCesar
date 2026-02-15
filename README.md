# Ciptografia_CifradoCesar

## ¿Qué es el Cifrado César?

El cifrado César es un tipo de **cifrado por sustitución**. Debe su nombre a Julio César, quien lo usaba para comunicarse con sus generales. 

Funciona desplazando cada letra del alfabeto un número determinado de posiciones. Por ejemplo, con un **desplazamiento de 3**:
- La **A** se convierte en **D**.
- La **B** se convierte en **E**.
- La **Z** se "da la vuelta" y se convierte en **C**.

Es un sistema de clave simétrica, lo que significa que necesitas la misma "llave" (el número de desplazamiento) tanto para ocultar el mensaje como para leerlo.

## Código

### 1. Definición del abecedario
El script define dos variables: `mayusculas` y `minusculas`. donde ademas se incluye la Ñ por ser el abecedario español

### 2. Funciones `cifrar` y `descifrar`
Ambas funciones recorren el texto letra por letra usando un bucle `for`.
- Utiliza `if letra in mayusculas` para saber si debe tratar el carácter como mayúscula, minúscula o ignorarlo (si es un espacio o signo de puntuación).
- Para **cifrar**, suma el desplazamiento: `(pos + desplazamiento)`.
- Para **descifrar**, resta el desplazamiento: `(pos - desplazamiento)`.

### 3. El Operador de Módulo (`%`)

```
nueva_pos = (pos + desplazamiento) % len(mayusculas)
El operador % (módulo) asegura que si el desplazamiento supera el límite del alfabeto (posición 27), el conteo vuelva a empezar desde el cero. Esto crea un efecto de "rueda" o círculo infinito sin necesidad de especificar la cantidad de carácteres en el "pos".
```

### 4. Preservación de Caracteres
Si el carácter no es una letra (por ejemplo, un espacio, un número o un punto), el código ejecuta el bloque else, añadiendo el carácter tal cual al resultado sin modificarlo. Esto mantiene la estructura de las frases original.
