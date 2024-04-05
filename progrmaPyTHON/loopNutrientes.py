#primero copiar el codigo a python y despues poner las funciones
import time
import serial
import mysql.connector
import RPi.GPIO as GPIO

def insert_nutrient_data(conexion, nitrogen, phosphorus, potassium):
    cursor = conexion.cursor()
    consulta = "INSERT INTO datos_nutrientes (nitrogeno, fosforo, potasio) VALUES (%s, %s, %s)"
    valores = (nitrogen, phosphorus, potassium)
    try:
        cursor.execute(consulta, valores)
        conexion.commit()
        print("Datos de nutrientes insertados en la base de datos")
    except mysql.connector.Error as err:
        print(f"Error al insertar datos de nutrientes: {err}")
    cursor.close()


def loopNutrientes():


    # Envía comandos para obtener las lecturas de nitrógeno, fósforo y potasio
    ser.write(b'\x01\x03\x00\x1e\x00\x01\xe4\x0c')  # Comando para nitrógeno
    time.sleep(0.1)  # Espera un poco antes de enviar el siguiente comando
    ser.write(b'\x01\x03\x00\x1f\x00\x01\xb5\xcc')  # Comando para fósforo
    time.sleep(0.1)
    ser.write(b'\x01\x03\x00\x20\x00\x01\x85\xc0')  # Comando para potasio
    time.sleep(0.1)

    # Lee las respuestas del sensor
    val_nitrogen = ser.read(7)
    val_phosphorous = ser.read(7)
    val_potassium = ser.read(7)
    # son site bits porque son los que manda el protocolo de comunicacion entre el sensor y la placa
    #pero otros sensores necesitaran otros protocolos y tal por lo que habra que cambiar el 7


    #2. Rango de medición: 0-1999 mg/kg (mg/l)
    #Como solo tiene de 0 a 7 tendra los posibles valores:
    # 0-285, 286-571, 572-857, 858-1143, 1144-1429,1430-1700,1701-1999

    nitrogenFinal = int (val_nitrogen,2)
    phosphorousFinal = int (val_phosphorous ,2)
    potasiumFinal = int (val_potassium ,2)
    #paso los valores en byte a decimal, el 2 es para indicar que es binario
        
    nitrogenFinal*=7.83921568627
    phosphorousFinal*=7.83921568627
    potasiumFinal*=7.83921568627
    #multiplico por 7.83921568627 porque son los mg que hay por cada bit de el byte de 7

    insert_nutrient_data(conexion_db, nitrogenFinal, phosphorousFinal, potasiumFinal)
    print("Ya sepuede enviar los datos a la base de datos")
    print("El nitrogeno es ", nitrogenFinal)
    print("El fosforo es ", phosphorousFinal)
    print("EL potasio es ", potasiumFinal)

    pass