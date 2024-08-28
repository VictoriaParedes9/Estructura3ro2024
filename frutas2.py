frutas={"manzana":{"precio":1500}, "pera": {"precio":800}}
        
total=0
fruta=input("ingrese la fruta que desea vender: ")
cantidad=float(input("ingrese la cantidad a vender: "))
               

if fruta in frutas:
    total=frutas[fruta]["precio"] * cantidad
    print("el total a pagar por {cantidad}kilos de {fruta} es: {total}")
    print("el precio de ",cantidad,"kg","de",fruta,"es de:",total)
else:
    print("la fruta ingresada no existe en en diccionario")