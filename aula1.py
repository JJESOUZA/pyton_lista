#lista = [10,20,30,40,50]
#print (lista)
#lista = [0] *10
#print (lista)
#lista = lista + [5]*2
#print (lista)

#lista = [10,20,30,40,50]
#print (lista)
#print (f'Tamanho da lista = {len(lista)}')
#print (f'Maior elemento da lista = {max(lista)}')
#print (f'Menor da lista = {min(lista)}')

#del apaga o elemento da referida posicao
#del lista [3]
#print(f'a nova lista retirando o elemento que estava na 3 posicao = {lista}') 

#cls para limpar o terminal.

#i é elemento ex:numero

#for i in range (2,7):
  #  print (i, end=' ')
#print () 

#for i in range (1,9,2):
 #   print (i, end=' ')
#print ()

#lista=[10,20,30,40,50]
#for i in lista:
#    print (i, end=' ')
#print ()

#lista=[10,20,30,40,50]
#print(lista[0])
#print(lista[1])
#print(lista[2])
#print(lista[-1])
#print(lista[-4])
#print(lista)
#lista=[3]*15
#print(lista)
#print(f'tamanho da lista = {len(lista)}')
#print(f'maior elemento = {max(lista)}')
#print(f'menor elemento = {min(lista)}')
#del lista[3]
#del apaga o elemento da referida posição
#print(f'A nova lista sem o terceiro elemento que estava na 3 posicao={lista}')

#for i in range(2,7):
#    print(i, end='  ')
#print()
#for i in range(1,11,3):
#    print(i, end='  ')
#print()
#lista=[10,20,30,40,50]
#for i in lista:
#    print(i, end='  ')
#print()

#for i in range(len(lista)):
#    print(lista[i], end='  ')
#lista=[10,20,30,40,50]
#print(lista)
#lista1=[5,5,5]
#lista.append(lista1)
#print(lista)
#lista.extend(lista1)
#print(lista)
#cl=lista.count(5)
#print(f'quantidade de elementos na lista')
#print (cl)

lista=[10,20,30,40,50]
print(lista)
x=lista.pop()
print(lista.pop(0))
print(lista)
try:
    lista.remove(20)
except:
    print(f"elemento 20 nao esta na lista")
    prnt(lista)
    n=int(input("entre com o numero a ser retirado"))
    try:
        lista.remove(n)
    except:
        print(f"elemento {n} nao esta na lista")
    print(lista)
    