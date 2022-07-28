
from time import sleep
import pyttsx3

engine = pyttsx3.init()

# Escribe en consola las voces disponibles para pode rnumerar en las propiedades que voz queremos usar. El orden es en el que las escribe comenzando a contar desde cero.
for voice in engine.getProperty('voices'):
    print(voice)
    
voices = engine.getProperty('voices')

engine.setProperty('rate', 150)
engine.setProperty('voice',voices[2].id)
engine.setProperty('volume', 1)


def saySomething(somethingToSay):
    print ('Listo para iniciar la transmisión de voz ...')
    engine.say(somethingToSay)
    engine.runAndWait()

#while True:
#   saySomething("Éste es un módulo que es capaz de leer en castellano lo que le pasemos como parámetro. La voz de Elena, leera diligentemente, aquello que le pasemos como string.")
    
#   sleep(1000)
