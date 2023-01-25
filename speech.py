import speech_recognition as sr

input_device_index = 1

r = sr.Recognizer()
with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source)
	print("Say Something!")
	audio = r.listen(source)

try:
	print("I think you said " + r.recognize_google(audio))
except sr.UnknownValueError:
	print("I could not understand")
except sr.RequestError as e:
	print("Error")