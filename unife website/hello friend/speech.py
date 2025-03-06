import speech_recognition as sr

r = sr.Recognizer()
with sr.AudioFile("output.wav") as source:
    audio = r.record(source)

text = r.recognize_google(audio)
print("Testo estratto:", text)
