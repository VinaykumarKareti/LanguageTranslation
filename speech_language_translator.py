import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS  # Used for text to speech conversion

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak something in Tamil:")
    audio = recognizer.listen(source)


try:
    spoken_text = recognizer.recognize_google(audio, language='ta-IN')
    print("Spoken text Tamil):", spoken_text)
except sr.UnknownValueError:
    print("Could not understand the audio")
except sr.RequestError as e:
    print("Error making the request: {0}".format(e))

translator = Translator()

translated_text = translator.translate(spoken_text, src='ta', dest='en')

print("Translated text (English):", translated_text.text)

