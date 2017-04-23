try:
    import speech_recognition
except ImportError:
    listen = None
    
else:
    recognizer = speech_recognition.Recognizer()

    def listen():
        with speech_recognition.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            return recognizer.recognize_sphinx(audio)
            # or: return recognizer.recognize_google(audio)

        except speech_recognition.UnknownValueError:
            print("Could not understand audio")
        except speech_recognition.RequestError as e:
            print("Recog Error; {0}".format(e))

        return ""
