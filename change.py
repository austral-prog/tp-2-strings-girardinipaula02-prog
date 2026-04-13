def change():
    
    gasto = float(input())

    dinero = int(input("Dinero recibido:"))

    vuelto = dinero - gasto

    pesos = int(vuelto)
    centavos = round((vuelto - pesos) * 100)

    print("Ingresar gasto:")
    print(gasto)
    print("Dinero recibido")
    print(dinero)
    print("")
    print("Vuelto")
    print("")
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)
#change()