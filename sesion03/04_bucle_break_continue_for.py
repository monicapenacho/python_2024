#break

frutas = ["manzana", "banana", "cereza", "sandía", "uva"]
for fruta in frutas:
    print(fruta)
    if fruta == "sandía":
        break



#continue

numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    if numero % 2 == 0:
        continue
    print(numero)