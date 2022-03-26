import random as rn


minimo = int(input('El numero minimo es: '))
maximo = int(input('El numero maximo es: '))

x = rn.randint(minimo,maximo)
vidas = 7
intentos = 0
print(f'Tienes {vidas} intentos para resolver el acertijo.')

while intentos < vidas:
    adivinanza = int(input('Cual es el numero misterioso? '))

    
    if(adivinanza == x):
        print('Has ganado!!!')
        break
    elif adivinanza<x:
        print('Intente nuevamente, el numero secreto es mayor!')
    else:
        print('Intente nuevamente, el numero secreto es menor!')

    intentos += 1
    if(intentos >= vidas):
        print('Perdiste! Intenta nuevamente')