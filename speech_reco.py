import speech_recognition as sp

reco=sp.Recognizer()

with sp.Microphone() as src:
	print("Listening....")
	audio=reco.listen(src)
try:
	text=reco.recognize_google(audio)
except:
	print("exception caught!")
print(text)
