s= int(input("Insira seu sexo sendo 1 para Masculino e 2 para Feminino: "))
fem= 1 
mas= 2 
alt= float(input("Insira sua altura: "))
fem= int((62.1 * alt) - 44.7)
mas= int((72.7 * alt) - 58)
if s==1:
    print("Seu peso idela é: ", fem)

if s==2:
    print("Seu peso ideal é: ", mas)
