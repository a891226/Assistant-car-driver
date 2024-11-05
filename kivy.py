from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import speech_recognition as sr
from gtts import gTTS
import os
class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # ایجاد کلید "دستیار"
        btn_assistant = Button(text='asistant')
        btn_assistant.bind(on_press=self.assistant)
        layout.add_widget(btn_assistant)

        # ایجاد کلید "صوت به متن"
        btn_speech_to_text = Button(text='text')
        btn_speech_to_text.bind(on_press=self.speech_to_text)
        layout.add_widget(btn_speech_to_text)

        # ایجاد کلید "متن به صوت"
        btn_text_to_speech = Button(text='audio')
        btn_text_to_speech.bind(on_press=self.text_to_speech)
        layout.add_widget(btn_text_to_speech)

        return layout

    def assistant(self, instance):
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
    def speech_to_text(self, instance):
        text=''
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print('Please speak...')
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source)
                text = r.recognize_google(audio)
                print(text)
        except sr.UnknownValueError:
            print('Google Speech Recognition could not understand audio')
        except sr.RequestError as e:
            print(f'Could not request results from Google Speech Recognition service; {e}')
        except Exception as e:
            print(f'Error: {e}. Please speak again')
    def text_to_speech(self, instance):
        from gtts import gTTS
        import os

        # متنی که می‌خواهید به صوت تبدیل شود را تعریف کنید
        text = input()

        # زبان متن را مشخص کنید (برای فارسی 'fa' و برای انگلیسی 'en')
        language = 'en'

        # یک شیء gTTS ایجاد کنید
        speech = gTTS(text=text, lang=language, slow=False)

        # فایل صوتی را ذخیره کنید
        speech.save("output.mp3")

        # فایل صوتی را پخش کنید (اختیاری)
        os.system("start output.mp3")    
if __name__ == '__main__':
    MyApp().run()