#import pyttsx3
from gtts import gTTS

voiceoverDir = "Voiceovers"

def create_voice_over(fileName, text):
    filePath = f"{voiceoverDir}/{fileName}.mp3"
    #engine = pyttsx3.init()
    #engine.save_to_file(text, filePath)
    #engine.runAndWait()
    #del engine
    tts = gTTS(text=text, lang='en')
    tts.save(filePath)
    return filePath