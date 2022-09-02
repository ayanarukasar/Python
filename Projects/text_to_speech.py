from gtts import gTTS #we have imported this module for conversion

text="Hello, Ayana Rukasar"

language='en' #en for english
obj=gTTS(text=text,lang=language,slow=False)

obj.save("sample.mp3")