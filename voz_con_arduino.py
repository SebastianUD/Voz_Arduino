import pyfirmata
import speech_recognition as sr
import pyttsx3

# Configuracion de arduino
board = pyfirmata.Arduino('COM3')
iter8 = pyfirmata.util.Iterator(board)
iter8.start()

led1=board.digital[13]
led2=board.digital[12]
led3=board.digital[11]


# Iinicializar Speech Recognition
escuchar = sr.Recognizer()

# Inicializar pyttsx3
inicializar = pyttsx3.init()
velocidad_de_voz = 130
inicializar.setProperty('rate', velocidad_de_voz)

# Nombre del asistente de voz
nombre = "alexa"

def hablar(texto):
    inicializar.say(texto)
    inicializar.runAndWait()

def tomar_comando():
    try:
        with sr.Microphone() as voz:
            print('Escuchando...')
            voice = escuchar.listen(voz)
            command = escuchar.recognize_google(voice, language='es-ES')
            command = command.lower()
            if nombre in command:
                command = command.replace(nombre, '')
                print(command)
        return command
    except:
        pass


def alexa():
    command=tomar_comando()

    if 'encender todos' in command:
        led1.write(1)
        led2.write(1)
        led3.write(1)
        hablar('Encendiendo led')
        
    elif 'primero' in command:
        led1.write(1)
        led2.write(0)
        led3.write(0)
        hablar('Encendiendo led 1')
    
    elif 'segundo' in command:
        led1.write(0)
        led2.write(1)
        led3.write(0)
        hablar('Encendiendo led 2')
    
    elif 'tercero' in command:
        led1.write(0)
        led2.write(0)
        led3.write(1)
        hablar('Encendiendo led 3')
        
    elif 'parpadear' in command:
        hablar('Parpadeando led')
        for i in range(8):
            led1.write(1)
            led2.write(1)
            led3.write(1)
            board.pass_time(0.5)
            led1.write(0)
            led2.write(0)
            led3.write(0)
            board.pass_time(0.5)
    
    elif 'apagar' in command:
        led1.write(0)
        led2.write(0)
        led3.write(0)
        hablar('Apagando led')
    
    elif 'salir' in command:
        hablar('Saliendo')
        exit()
    
while True:
    alexa()
