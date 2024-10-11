import speech_recognition
r=speech_recognition.Recognizer()
while True:
    try:
        with speech_recognition.Microphone() as source:
            print('Please speak...')
            r.adjust_for_ambient_noise(source,duration=1)
            audio=r.listen(source)
            text=r.recognize_google_cloud(audio)
            print(text)
    except:
        print('Error. Please speak again')