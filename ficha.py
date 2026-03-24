def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)

    nombre = input("Ingrese su nombre completo: ")
    email = input("Ingrese su email: ")
    nota1 = input("Ingrese la primera nota: ")
    nota2 = input("Ingrese la segunda nota: ")
    nota3 = input("Ingrese la tercera nota: ")

    nombre = nombre.strip()
    nombre = nombre.title()

    email = email.strip()
    email = email.lower()

    nota1 = int(nota1)
    nota2 = int(nota2)
    nota3 = int(nota3)

    cantidad_caracteres = len(nombre)

    posicion_espacio = nombre.find(" ")

    inicial_nombre = nombre[0]
    inicial_apellido = nombre[posicion_espacio + 1]

    nombre_solo = nombre[:posicion_espacio]
    apellido = nombre[posicion_espacio + 1:]

    usuario = apellido.lower() + "." + nombre_solo.lower()

    contiene_arroba = "@" in email

    posicion_arroba = email.find("@")
    dominio = email[posicion_arroba + 1:]

    nombre_guion = nombre.replace(" ", "_")

    cantidad_a = nombre.lower().count("a")

    codigo_secreto = nombre[::-1].upper()

    suma = nota1 + nota2 + nota3
    promedio = suma / 3
    promedio_entero = suma // 3

    encabezado = """========================
FICHA DE ALUMNO
========================"""

    print(encabezado)
    print(f"Nombre limpio: {nombre}")
    print(f"Email en minúsculas: {email}")
    print(f"Cantidad de caracteres del nombre: {cantidad_caracteres}")
    print(f"Iniciales: {inicial_nombre}{inicial_apellido}")
    print(f"Usuario: {usuario}")
    print(f"¿El email contiene @?: {contiene_arroba}")
    print(f"Dominio del email: {dominio}")
    print(f"Nombre con guion bajo: {nombre_guion}")
    print(f"Cantidad de letras 'a' en el nombre: {cantidad_a}")
    print(f"Código secreto: {codigo_secreto}")
    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Nota 3: {nota3}")
    print(f"Suma de notas: {suma}")
    print(f"Promedio: {promedio}")
    print(f"Promedio entero: {promedio_entero}")
    print("=" * 24)

ficha()