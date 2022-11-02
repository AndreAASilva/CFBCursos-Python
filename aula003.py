#Escopo de variáveis

#Quando declaramos uma variável fora da função ela é uma variável global, porém se declaramos dentro da função ela é uma variável local, mas utilizando o código GLOBAL dentro da função, podemos torna-la global como no exemplo abaixo.

def cn():
    global canal #Variável dentro da função transformada em uma variável global
    canal='CFB Cursos'

cn() #Chamando a função
print(canal) #para depois imprimir no programa