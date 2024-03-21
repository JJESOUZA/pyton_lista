#random biblioteca, time 
#numero=random.randint (1,100)
#tempo=time.time () 
#tentativas= int.input()
#tentativas

#random biblioteca, 
#time 
#numero=random.randint (1,100)
#tempo=time.time () 
#tentativas=0 
#while true=
#tentativas +=1
#papite=int (input ("qual sua sugestão"))
#if palpite <> numero
#print("tente outra vez")
#else:
#tempofinal=time.time()
#tempototal=time.time ()
#tempototal=tempofina-tempo 
#"print (parabens..{numero}em {tentativa} tentativas num tempo de {tentativas} )""
#TEST
import time
import random
numero=  random.randint(1,100)

tempo_start= time.time ()

resposta = 0
tentativa = 0
print("Palpite gerado!")

chute= 0
while chute is not numero:
    tentativa +=1
    chute = int(input("Qual seu chute: "))
    if chute > numero:
        print("Errou! É um valor menor que ", chute)
    elif chute < numero:
        print("Errou! É um valor maior que ", chute)
    else:
        print(f"Parabéns! O número gerado foi ", {numero}, 
        "Acertou em ",{tentativa}," tentativas!")
        break

tempofinal= time.time()
tempototal= tempofinal - tempo_start
print (f" SEU TEMPO FINAL FOI: em {numero:.2f} segundos ")


