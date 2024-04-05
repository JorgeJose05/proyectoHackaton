import time #biblioteca para controlar el tiempo y poder hacer el time.sleep
#import RPi.GPIO as GPIO
#Instalar con 
#pip install RPi.GPIO

#import serial
#pip install pyserial

import mysql.connector #para conectar con la base de datos
#hay que instalar con este comando 
#pip install mysql-connector-python

from loopNutrientes import loopNutrientes
from loopSol import loopSol #para los puertos serie del sensor de nutrientes

#La base de datos tendra 5 + 3 + 1 = 9 columnas

# Configuración de la base de datos
db_config = {
    "host": "taxistahosting.com",
    "port": 3306,
    "user": "testing",
    "password": "digital!",
    "database": "basePyt" 
}

# Función para inicializar la conexión a la base de datos
def connect_database():
    try:
        conexion = mysql.connector.connect(**db_config)#asignarle la base de datos configurada
        print("Conexión exitosa a la base de datos")
        return conexion
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        return None
    #Comprobacion de conexion 

# Función para insertar datos de lluvia en la base de datos
def insert_lluvia_data(conexion, dias, horas, minutos, segundos, medialluvia):
    cursor = conexion.cursor() #Crea objeto cursor que hace consultas a la base de datos
    consulta = "INSERT INTO datos_lluvia (dias, horas, minutos, segundos, medialluvia) VALUES (%s, %s, %s, %s, %s)"
    #Se hace una consulta de insrcion
    valores = (dias, horas, minutos, segundos, medialluvia)#los valores que vamos a meter en orden
    try:
        cursor.execute(consulta, valores)#el cursor ejecuta la consulta
        conexion.commit()#asegura la conexion hhaciendo que se guarden en la base de datos permanentemente
        print("Datos de lluvia insertados en la base de datos")
    except mysql.connector.Error as err:
        print(f"Error al insertar datos de lluvia: {err}")
    cursor.close()


def insert_nutrient_data(conexion, nitrogen, phosphorous, potassium):
    cursor = conexion.cursor()
    consulta = "INSERT INTO datos_nutrientes (nitrogeno, fosforo, potasio) VALUES (%s, %s, %s)"
    valores = (nitrogen, phosphorous, potassium)
    try:
        cursor.execute(consulta, valores)
        conexion.commit()
        print("Datos de nutrientes insertados en la base de datos")
    except mysql.connector.Error as err:
        print(f"Error al insertar datos de nutrientes: {err}")
    cursor.close()

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



    # Conectar a la base de datos
    global conexion_db
    conexion_db = connect_database()

    #Creo que al final tiene que llamar al loop para que se le llame
    loop()
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


    analogValue = (analogValue* 60)/256  #Ejemplo cada bit son 60 ml
    
    medialluvia = medialluvia+ analogValue

    # Leer los datos de los pines digitales (simulado)
    dig1 = GPIO.input(DIGITAL_PIN_1)
    dig2 = GPIO.input(DIGITAL_PIN_2)

    # Si no llueve, calcular el tiempo total de lluvia
    if dig1 <= 1:
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
        
        medialluvia/=totalTime
        insert_lluvia_data(conexion_db, dias, horas, minutos, segundos, medialluvia)

        print("Han llovido 60 ml de media")
        # Reiniciar el tiempo total
        totalTime = 0
        medialluvia= 0
    else:
        # Incrementar el tiempo total
        totalTime += 1

    time.sleep(1)  # Esperar 1 segundo antes de repetir el bucle

    pass

