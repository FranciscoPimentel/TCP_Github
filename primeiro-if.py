velocidade =  float(input("Qual a velocidade atual do carro?  "))
if velocidade > 80:
    print ("multado")
    multa =  (velocidade-80) * 7
    print("vc deve pagar a multa de R${:.2f}!" .format(multa))
print("dirija com segurança")    
----
numero = int(input("digite um numero: "))
resultado = numero % 2
if resultado == 0:
    print (" o número {} é PAR ".format(numero))
else:
    print (" o número {} é IMPAR ".format(numero))