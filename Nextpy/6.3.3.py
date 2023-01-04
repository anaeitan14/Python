from gtts import gTTS
import os


text = "first time i'm using a package in next.py course"
language = "en"

my_recording = gTTS(text=text, lang=language, slow=False)

my_recording.save("Test.mp3")


os.system("Test.mp3")