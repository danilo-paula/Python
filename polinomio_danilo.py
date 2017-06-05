#-*-coding:cp1252-*-
import numpy as np 
import matplotlib.pyplot as plt

#Intro: apresenta o programa
print("Este programa, uma atividades de Problemas Integrados")
print("calcula o valor do X que voc� decidir, de um polin�omio qualquer,")
print("e depois gera seu gr�fico")
print("------------------------------------------------------------")


#1a parte: Lista de N
#Gera o vetor  dos numeros inteiros (que v�o de 0 � N, indo de 1 em 1) que X ser� elevado
#e guarda os coeficientes pra cada um deles
n_g=int(input("Por favor, diga qual o grau do polin�mio: "))
n=n_g+1
lista_pol=np.linspace(0,n_g,n)
coef=np.linspace(0,0,n)
ini=list(range(n))
print("Favor digite o coeficiente de")
for indice in ini:
  print("X elevado � %i:"%(indice))
  coef[indice]=float(input("--> "))

#2a parte: Calculo pedido de f(x)
#Gera um vetor com todos os valores iguais a X, depois os eleva ao numero respectivo e multiplica pelo coeficiente
#somando todos os valores do vetor resultante no final, obtendo assim f(x)
x_i=float(input("Diga o valor do x que quer calcular: "))
x=np.linspace(0,0,n)
for indice in ini:
  x[indice]=x_i
pol=np.sum(coef*x**(lista_pol))
print("O valor obtido para o seu x foi: %f"%(pol))
print("------------------------------------------------------------")

#3a parte: Plot do gr�fico
#Gera um vetor crescente com grande numero de elementos, e calcula(em outro vetor com range igual) o f(x) pra cada um deles
#depois plota  o gr�fico de X em fun��o de Y
x_graf=np.linspace(-10*n,10*n,100*n)
y_graf=np.linspace(0,0,100*n)
ini2=list(range(100*n))
for indice in ini2:
  y_graf[indice]=np.sum(coef*(x_graf[indice]**(lista_pol)))
plt.plot(x_graf,y_graf)
plt.title("O gr�fico da sua fun��o �: ")
plt.xlabel("Valores de X")
plt.ylabel("Valores de f(x)")
plt.show()
#***Programa por Danilo de Paula***
