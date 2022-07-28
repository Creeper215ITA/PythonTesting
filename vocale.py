from pyttsx3 import init
from speech_recognition import Recognizer, Microphone
from datetime import datetime
import webbrowser
from random import choice

while True:

    engine = init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    engine.say("Ciao, sono PIni e sono qui per ")
    engine.runAndWait()
    r = Recognizer()

    with Microphone() as source:
        print("Pronto ad ascoltare")
        audio = r.listen(source)
        testo = r.recognize_google(audio, language="it-IT").lower()
        risposta = "Non ho capito"
        print(testo)
        if "ricestta" in testo:
            with open("ricetta.txt", "w") as f:
                f.write("scemo chi legge")
            risposta = "ho creato per te la ricetta"
        elif any(parola in testo for parola in["apri youtube", "youtube", "voglio vedere un video", "sono annoiato", "voglio vedere youtube"]):
            webbrowser.open("www.youtube.com")
            risposta = "Ecco a te YouTube, divertiti"
        if "chiuditi" in testo:
            break
        engine.say(risposta)
        engine.runAndWait()

