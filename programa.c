/*
Tienes que incluir estas librerias
#include <stdio.h>

#include <wiringPi.h> Esta sirve para comunicarse con pines GPIO 
WiringPi es una biblioteca en C que te permitirá leer los valores analógicos y digitales de los pines GPIO de la Raspberry Pi.

#include <modbus.h> Esto sirve para controlar los MODBUS y la comunicacion entre sensores la placa y la base de datos


*/

/*
Tambien hay que crear un json que es un archivo que dice mas o menos los datos que tendran los 
sensores y su configuracion y datos de los sensores como estos ejemplos
{
  "name": "Sensor de Temperatura",
  "type": "Analógico",
  "model": "LM35",
  "connection": {
    "gpio_pin": 17
  },
  "options": {
    "units": "Celsius",
    "resolution": 0.1
  }
}
o el ejemplo de david: los coils se refiere a coils de MODBUS

192.168.1.10{
    coils{};
    coils WR{
        0
        1
        2
        3
    ney_hold[];
    ney_read;

192.168.1.10{.......}
    }
}




*/

//Defino los pines para saber de donde me viene la informacion el ANALOG_PIN_1 es el nombre del
//pin y el 0 es el numero del puerto al que lo he conectado (creo que hace falta definir mejor
//los pines )
#define ANALOG_PIN 0//poner el pin analogico si lo hago analogico
#define DIGITAL_PIN_1 //poner el pin digital si se hace por pin digital
#define DIGITAL_PIN_//poner el pin digital si se hace por pin digital



void loop ();

int main ()
{
    wiringPiSetup();//para iniciar la biblioteca y la configuracion de la pines GPIO

    //****Tengo problemas con las variables porque si las declaro no las puedo volver a usar
    //abajo y por lo tanto en cada loop estoy volviendo a crear variables





  while (1)
	{
        




	  loop ();
	}

  return 0;
}

void loop ()
{

//leer los datos de la lluvia que hay en ese momento
        float analogValue = analogRead(ANALOG_PIN);

//Lectura de los pines digitales que son menos precisos, sesupone que solo van a devolver un
//high o un low de lo poco precisos que son por lo que tambien se recomienda usar un bool(boolean)
        int dig1 = digitalRead(DIGITAL_PIN_);
        int dig2 = digitalRead(DIGITAL_PIN_1);
//estos pines digitales seria para comprobar si llueve o no llueve incluso se podria hacer un
//while con contador para que mientras los digs sean high o no sean low se registre que este lloviendo
//cuando se llege a low y en un corto tiempo no vuelva a llegar a high pues el contador sera el
//tiempo que ha llovido y cuando acabe entonces se le enviara a la BBDD el resultado final del
//contador transformado a dias, horas, minutos seg(si se puede) para saber durante cuanto llueve


        float humedad;//= analgogValue (hacerle los calculos necesarios para sacar la humedad)


//no es mio
//Ejemplo de programa que dice durante cuanto a llovido


        
        static int totalTime;
        if(dig1 !=1){

            //pasar el totalTime a tiempo
            //ahhora si me deja declarar y abajo usarlas
            int horas, segundos,minutos, dias;

            //segundos no lo tengo
            dias = totalTime /86400000;//86400000 porque son los segundos que hay en un dia 
            horas = (totalTime % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60);
            minutos = (totalTime % (1000 * 60 * 60)) / (1000 * 60);
            segundos = (totalTime % (1000 * 60)) / 1000;

            printf("Ha llovido durante unos %d dias, %d horas, %d minutos y %d segundos ", dias, horas, minutos, segundos);

            static int totalTime = 0;
        }else{
            totalTime++;
        }


delay(1000);
//esto es una espera de un segundo esta porque es cada cuanto tiempo se reproducira el loop
//deberia estar al final porque es una espera
}
