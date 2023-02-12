p = int(input("Escolha quantos lados em o polígono: "))
at = ((2*3)/2)
aq = (2*2)
if p == 3:
 print ("Esse é um triângulo e a área é: ", at ,"considerando a altura: 3 e a base: 2")
if p == 4:
 print ("Esse é um quadrado e a área é: ", aq, "considerando o lado: 2")
if p == 5:
    print ("Esse é um quadrilátero")
if (p < 3):
    print("Não é um polígino")
if (p > 5):
    print("Não é um polígino")