deportes=("futbol","tenis","basquet")
buscar=input("ingrese el elemento que desea buscar dentro de la tupla: ")
if buscar in deportes:
    print("el elemento",buscar," se enceuntra dentro de la tupla: ")
else:
    print("el elmento",buscar," no se encuentra dentro de la tupla")