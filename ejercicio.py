animales=("oso","ardilla","gato")
buscar=input("que animal desea buscar: ")
if buscar in animales:
    print("el animal",buscar,"el animal se encuentra en la tupla: ")
else:
    print("el animal",buscar,"el animal no esta en la lista: ")