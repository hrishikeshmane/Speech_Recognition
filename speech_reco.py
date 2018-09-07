import speech_recognition as sp

reco=sp.Recognizer()

with sp.Microphone() as src:
	print("Listening....")
	audio=reco.listen(src)

text=reco.recognize_google(audio)
print(text)
