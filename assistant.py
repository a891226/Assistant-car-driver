import speech_recognition as sr
text1='print'#
r = sr.Recognizer()
try:
    with sr.Microphone() as source:
        print('Please speak...')
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        text = r.recognize_google(audio)
        if text==text1:
            print('l') #
        else:          #
            print(text)#
except sr.UnknownValueError:
    print('Google Speech Recognition could not understand audio')
except sr.RequestError as e:
    print(f'Could not request results from Google Speech Recognition service; {e}')
except Exception as e:
    print(f'Error: {e}. Please speak again')