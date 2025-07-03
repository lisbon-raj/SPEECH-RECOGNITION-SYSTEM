import speech_recognition as sr

def transcribe_speech(file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        print("Listening to the audio...")
        audio = recognizer.listen(source, timeout=10, phrase_time_limit=30)

    try:
        print("Transcribing...")
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Could not understand audio."
    except sr.RequestError as e:
        return f"API error: {e}"


if _name_ == "_main_":
    audio_path = "sample.wav"  # replace with your .wav file
    result = transcribe_speech(audio_path)
    print("Transcribed Text:\n", result)
