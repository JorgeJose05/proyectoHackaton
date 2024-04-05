def loopSol():

    #Radiacion solar comun y sana para las plantas de dia 200-400 µmol micromoles
    #Radiacion solar dañina para las plantas en general 1000 µmol
    #La radiacion solar que llega de noche es casi nulo por lo que con un sensor barato no se
    #podra detectar por lo que mientras el sensor no detecte nada sera de noche y si detecta 
    #algo es de dia

    radiacion = GPIO.input(ANALOG_PIN_7)

    if radiacion>0:
#Para saber cuanta radiacion hay habra que hacer igual que con los otros sensores y multiplicar
#la variable radiacion por cuantos micromoles son un bit (ej 1 bit = 7micromoles)
        radiacion=radiacion*(7*8)#porque 1 byte son 8 bits y 7 es lo que vale cada bit

        if radiacion>400:
            if radiacion >=1000:
                  print("La radiacion llega a 1000 micromoles activar toldo")
            else:
                print("La radiacion solar es " + radiacion + " esta dentro del nivel estable")    
        
        else:
            if radiacion <200:
                print("La radiacion es muy poca no hay suficiente luz solar")

    else:
            print("No se detecta radiacion solar o es de noche o hay un problema")

    pass