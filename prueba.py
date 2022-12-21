import pyfirmata
import speech_recognition as sr
import pyttsx3

# Configuracion de arduino
board = pyfirmata.Arduino('COM3') # Definir el puerto de arduino
iter8 = pyfirmata.util.Iterator(board) # Inicializar el iterador
iter8.start() # Iniciar el iterador

led1=board.digital[13] # Definir el pin 13 como salida
led2=board.digital[12] # Definir el pin 12 como salida
led3=board.digital[11] # Definir el pin 11 como salida
led4=board.digital[10] # Definir el pin 10 como salida
led5=board.digital[9] # Definir el pin 9 como salida

# Iinicializar Speech Recognition
escuchar = sr.Recognizer() # Inicializar el reconocedor de voz

# Inicializar pyttsx3
inicializar = pyttsx3.init() # Inicializar el motor de voz
velocidad_de_voz = 130 # Definir la velocidad de la voz
inicializar.setProperty('rate', velocidad_de_voz) # Establecer la velocidad de la voz

# ---Definir las clases---
class Voz_arduino:
    def hablar(self, texto):
        inicializar.say(texto) # Establecer el texto a decir
        inicializar.runAndWait() # Ejecutar el motor de voz

class Comando:
    def tomar_comando(self):
        try:
            with sr.Microphone() as voz: # Definir el microfono como fuente de voz
                print('Escuchando...') # Mostrar el mensaje en la consola
                voice = escuchar.listen(voz) # Escuchar la voz
                command = escuchar.recognize_google(voice, language='es-ES') # Reconocer la voz
                command = command.lower() # Convertir la voz a minusculas
                print(command) # Mostrar el comando en la consola
            return command # Retornar el comando
        except:
            pass # Si no se reconoce la voz, no hacer nada

class Ejecutar:  
    def run(self):
        self.command=Comando() # Definir el comando
        command=self.command.tomar_comando() # Tomar el comando
        
        if 'encender todos' in command: # Si el comando es 'encender todos' prende todos los leds
            led1.write(1)
            led2.write(1)
            led3.write(1)
            led4.write(1)
            led5.write(1)
            Voz_arduino.hablar(self,'Encendiendo led')
            
        elif 'primero' in command: # Si el comando es 'primero' prende el led 1
            led1.write(1)
            led2.write(0)
            led3.write(0)
            led4.write(0)
            led5.write(0)
            Voz_arduino.hablar(self,'Encendiendo led 1')
        
        elif 'segundo' in command: # Si el comando es 'segundo' prende el led 2
            led1.write(0)
            led2.write(1)
            led3.write(0)
            led4.write(0)
            led5.write(0)
            Voz_arduino.hablar(self,'Encendiendo led 2')
        
        elif 'tercero' in command: # Si el comando es 'tercero' prende el led 3
            led1.write(0)
            led2.write(0)
            led3.write(1)
            led4.write(0)
            led5.write(0)
            Voz_arduino.hablar(self,'Encendiendo led 3')
        
        elif 'cuarto' in command: # Si el comando es 'cuarto' prende el led 4
            led1.write(0)
            led2.write(0)
            led3.write(0)
            led4.write(1)
            led5.write(0)
            Voz_arduino.hablar(self,'Encendiendo led 4')
        
        elif 'quinto' in command: # Si el comando es 'quinto' prende el led 5
            led1.write(0)
            led2.write(0)
            led3.write(0)
            led4.write(0)
            led5.write(1)
            Voz_arduino.hablar(self,'Encendiendo led 5')
            
        elif 'parpadear' in command: # Si el comando es 'parpadear' parpadea los leds
            Voz_arduino.hablar(self,'Parpadeando led')
            for i in range(8):
                led1.write(1)
                led2.write(1)
                led3.write(1)
                led4.write(1)
                led5.write(1)
                board.pass_time(0.5)
                led1.write(0)
                led2.write(0)
                led3.write(0)
                led4.write(0)
                led5.write(0)
                board.pass_time(0.5)
        
        elif 'apagar' in command: # Si el comando es 'apagar' apaga todos los leds
            led1.write(0)
            led2.write(0)
            led3.write(0)
            led4.write(0)
            led5.write(0)
            Voz_arduino.hablar(self,'Apagando led')
          
        elif 'semáforo' in command: # Si el comando es 'semaforo' enciende el led 1 y apaga los otros dos
            led1.write(1)
            led2.write(1)
            led3.write(0)
            led4.write(0)
            led5.write(0)
            Voz_arduino.hablar(self,'Semaforo en rojo')
            board.pass_time(3)
            led1.write(0)
            led2.write(0)
            led3.write(1)
            led4.write(0)
            led5.write(0)
            Voz_arduino.hablar(self,'Semaforo en amarillo')
            board.pass_time(3)
            led1.write(0)
            led2.write(0)
            led3.write(0)
            led4.write(1)
            led5.write(1)
            Voz_arduino.hablar(self,'Semaforo en verde')
        
        elif 'salir' in command: # Si el comando es 'salir' sale del programa
            Voz_arduino.hablar(self,'Saliendo')
            exit()
        
        else:
            Voz_arduino.hablar("No te entiendo, repite por favor")

miArduino=Ejecutar()

while True: 
    miArduino.run() # Ejecutar la funcion Run en un cliclo infinito
