# ابتدا کتابخانه gtts و os را وارد کنید
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