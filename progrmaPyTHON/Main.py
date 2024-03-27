import time #biblioteca para controlar el tiempo y poder hacer el time.sleep
import RPi.GPIO as GPIO
import serial

from loopNutrientes import loopNutrientes
from loopSol import loopSol #para los puertos serie del sensor de nutrientes




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

    global medialluvia
    medialluvia=0

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

    #Sensor de radiacion solar

    global ANALOG_PIN_7
    ANALOG_PIN_7 = 7 # Definir el pin analogico del sensor de radiacion solar
    GPIO.setup(ANALOG_PIN_7, GPIO.IN)
    pass

def loop():
    while True:
        loopTiempoLluvia()

        loopNutrientes()    

        loopSol()
    

#definir un loop para cada dato despues meterlo todo en un loop y al final devolver los datos a
#la base de datos        

def loopTiempoLluvia () :
    
    # Leer los datos del pin analógico (simulado)
    analogValue = GPIO.input(ANALOG_PIN)

    medialluvia +=analogValue

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

        #Imprimir la cantidad de lluvia
#Para esto hay que comparar el rango de bits(ej 0-1023) del sensor con cuantos ml representa un
#bit que le el sensor, o la capacidad maxima de lectura de ml ==  la capacidad de mandar bits
# entonces se divide el numero de bits que envia por los ml maximos de lectura y eso es son los
        #ml que vale cada bit. Por ahora pondre una division estandar de los bits del sensor
        
        medialluvia=medialluvia/60#Ejemplo cada bit son 60 ml

        print("Han llovido 60 ml de media")
        # Reiniciar el tiempo total
        totalTime = 0
    else:
        # Incrementar el tiempo total
        totalTime += 1

    time.sleep(1)  # Esperar 1 segundo antes de repetir el bucle

    pass

