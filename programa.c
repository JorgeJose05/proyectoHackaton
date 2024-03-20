import time #biblioteca para controlar el tiempo y poder hacer el time.sleep
import RPi.GPIO as GPIO
import serial

from loopNutrientes import loopNutrientes #para los puertos serie del sensor de nutrientes




def setup():

    GPIO.setmode(GPIO.BCM)
#Establece el modo de enumeracion de pines GPIO en numerico (para poder seleccionar los pines)
   
    #Pines de loopLluvia
    global ANALOG_PIN
    ANALOG_PIN = 0  # Define el pin analógico
    global DIGITAL_PIN_1 
    DIGITAL_PIN_1 = 1  # Define el primer pin digital
    global DIGITAL_PIN_2
    DIGITAL_PIN_2 = 2  # Define el segundo pin digital

    GPIO.setup(DIGITAL_PIN_1, GPIO.IN)
    GPIO.setup(DIGITAL_PIN_2, GPIO.IN)
    GPIO.setup(ANALOG_PIN, GPIO.IN)

    #Pines de loopNutrientes
    #2. Rango de medición: 0-1999 mg/kg (mg/l)
    global RE 
    RE = 8
    GPIO.setup(RE,GPIO.IN)
    ser = serial.Serial('/dev/ttyS0', 9600, timeout=1)  # Ajusta '/dev/ttyS0' según el puerto serie que estés utilizando
    # define un objeto como el puerto de seria, el 1er parametro es el puerto se debe cambiar, 
    #2nd '' es la velocidad pel puerto, y el utlimo es el tiempo de espera maximo
    # 0-285, 286-571, 572-857, 858-1143, 1144-1429,1430-1700,1701-1999
    


#Esto es para configurarlos para que los pines lean datos

    global totalTime
    totalTime=0

    pass

def loop():
    
    loopTiempoLluvia()

    loopNutrientes()    

    loop()

#definir un loop para cada dato despues meterlo todo en un loop y al final devolver los datos a
#la base de datos        

def loopTiempoLluvia () :
    
    # Leer los datos del pin analógico (simulado)
    analogValue = 50

    # Leer los datos de los pines digitales (simulado)
    dig1 = GPIO.input(DIGITAL_PIN_1)
    dig2 = GPIO.input(DIGITAL_PIN_2)

    # Si no llueve, calcular el tiempo total de lluvia
    if dig1 != 1:
        # Calcular el tiempo en días, horas, minutos y segundos
        dias = totalTime // 86400
        horas = (totalTime % 86400) // 3600
        minutos = (totalTime % 3600) // 60
        segundos = totalTime % 60

        # Imprimir el tiempo total de lluvia
        print(f"Ha llovido durante unos {dias} días, {horas} horas, {minutos} minutos y {segundos} segundos")

        # Reiniciar el tiempo total
        totalTime = 0
    else:
        # Incrementar el tiempo total
        totalTime += 1

    time.sleep(1)  # Esperar 1 segundo antes de repetir el bucle

    pass

