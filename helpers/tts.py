from gtts import gTTS as gtts


def transform(text, f='record.mp3', slow=False):
    record = gtts(text=text, lang='en', slow=slow)
    record.save(f)
    return f
